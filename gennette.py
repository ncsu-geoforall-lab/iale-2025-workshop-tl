import grass.script as gs

# modify here
# change function name
def depressions(elevation):
    """Compute terrain depressions"""
    gs.run_command("r.fill.dir", input= "elevation", output="filled", direction="dir")
    gs.mapcalc("elev_diff = filled - dir")
    gs.parse_command("r.colors", map="elev_diff", color="differences")
    
    gs.parse_command("r.univar", map="elev_diff")
    gs.run_command("r.to.vect", input="fill_area", output="fill_area", type="area")
    gs.run_command("r.relief", input="filled", output="filled_shade")

if __name__ == "__main__":
    elevation = "elevation"
    depressions(elevation=elevation)
