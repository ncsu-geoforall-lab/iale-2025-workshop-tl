import grass.script as gs

# modify here
# change function name
def radiation(elevation):
    """Computes profile curvature"""
    gs.run_command("r.sun", elevation="elevation", aspect="aspectLM", day=1, glob_rad="glob_rad_LM")

if __name__ == "__main__":
    elevation = "elevation"
    radiation(elevation=elevation)
