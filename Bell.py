import grass.script as gs

# modify here
# change function name
def topidx(elevation):
    """Computes profile curvature"""
    gs.run_command("r.topidx", input="elevation", output="kool_map")

if __name__ == "__main__":
    elevation = "elevation"
    topidx(elevation=elevation)
