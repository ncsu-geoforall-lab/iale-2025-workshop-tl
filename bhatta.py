import grass.script as gs

# modify here
# change function name
def topidx(elevation):
    #Compute topographic wetness index with r.topoidx
    gs.run_command("r.watershed", elevation="elevation", accumulation="accumulation", drainage="drainage")
    gs.run_command("r.topidx", input="elevation", output="topo_map")

if __name__ == "__main__":
    elevation = "elevation"
    topidx(elevation=elevation)
