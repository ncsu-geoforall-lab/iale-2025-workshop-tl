import ast
import astor
import os

header = """
#!/usr/bin/env python
import grass.script as gs
import analyses
from tangible_utils import get_environment


def get_coordinates(points):
    data = gs.read_command("v.out.ascii", input=points, separator="comma").splitlines()
    return [[float(coor) for coor in point.split(",")[:2]] for point in data]


def run_change_detection(scanned_elev, env, **kwargs):
    #env = get_environment(rast=scanned_elev, n='n-20', s='s+20', e='e-20', w='w+20')
    analyses.change_detection(before='scan_saved',
                              after=scanned_elev,
                              change='change',
                              height_threshold=[10, 30],
                              cells_threshold=[7, 100],
                              add=True,
                              max_detected=3,
                              debug=True,
                              env=env,
                              )

"""


class GRASSCodeTransformer(ast.NodeTransformer):
    def __init__(self, file):
        self.env_param = ast.arg(arg="env", annotation=None)
        self.kwargs_param = ast.arg(arg="kwargs", annotation=None)
        self.rename_prefix = "_run_"
        self.rename_suffix = f"_{file[:-3]}"

    def visit_Name(self, node):
        if node.id == "elevation":
            return ast.Name(id="scanned_elev", ctx=node.ctx)

        return node

    def visit_FunctionDef(self, node):

        if node.name != "get_coordinates":
            node.name = self.rename_prefix + node.name + self.rename_suffix

        # Rename parameter 'elevation' to 'scanned_elev'
        for arg in node.args.args:
            if arg.arg == "elevation":
                arg.arg = "scanned_elev"

        if not any(arg.arg == "env" for arg in node.args.args):
            node.args.args.append(self.env_param)

        if node.args.kwarg is None:
            node.args.kwarg = self.kwargs_param

        for i, arg in enumerate(node.args.args):
            if arg.arg == "points":
                if node.args.defaults:
                    node.args.defaults.insert(0, ast.Constant("change"))
                else:
                    node.args.defaults = [
                        ast.Constant("change"),
                        ast.Constant(value=None),
                    ]

        self.generic_visit(node)
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and isinstance(
            node.func.value, ast.Name
        ):
            if node.func.value.id == "gs":
                if not any(kw.arg == "env" for kw in node.keywords):
                    node.keywords.append(
                        ast.keyword(arg="env", value=ast.Name(id="env", ctx=ast.Load()))
                    )

        # Rename 'elevation' keyword arguments to 'scanned_elev'
        for kw in node.keywords:
            if kw.value == "elevation":
                kw.value = "scanned_elev"
        return self.generic_visit(node)


def transform_code(source_code, file):
    tree = ast.parse(source_code)
    transformer = GRASSCodeTransformer(file)
    transformed_tree = transformer.visit(tree)
    functions = []
    for node in transformed_tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name == "get_coordinates":
                continue
            functions.append(astor.to_source(node).strip())
    return functions


def process_directory(input_dir, output_file):
    all_functions = []
    blacklist = ["postprocess.py", "participant_analyses.py"]

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".py") and file not in blacklist:
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    source = f.read()
                    transformed_function = transform_code(source, file)
                    if transformed_function:
                        all_functions.extend(transformed_function)

    with open(output_file, "w") as out:
        out.write(header)
        out.write("\n\n".join(all_functions))


if __name__ == "__main__":
    process_directory(".", "participant_analyses.py")
