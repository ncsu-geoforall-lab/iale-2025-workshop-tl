import grass.script as gs

# modify here
# change function name
def myanalysis(viewshed):
    """Assembles viewshed from max point"""
    univar = gs.parse_command("r.univar", map="elevation", flags="g")
    gs.parse_command("r.stats", input="peak", flags ="gn")
    gs.run_command("r.viewshed", input="elevation", output="viewshed", observer_elevation=1.75, coordinates=[703012.5,131923.5])

if __name__ == "__main__":
    viewshed = "viewshed"
    myanalysis(viewshed=viewshed)
