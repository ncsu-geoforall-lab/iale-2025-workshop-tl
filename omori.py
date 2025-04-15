import grass.script as gs

# modify here
# change function name
def analyze_watersheds (elevation, threshold):
    """Compute watersheds and average slope values for each watershed"""
#aspect    
    gs.run_command("r.slope.aspect", elevation=elevation, slope="slope", format="degrees")

# extract the raster cell
    gs.run_command("r.watershed", elevation=elevation, threshold=threshold, basin="watersheds", memory=300)

#average slope
    gs.run_command("r.stats.zonal", base="watersheds", cover="slope", method="average", output="avg_slope")

 
if __name__ == "__main__":
    elevation = "elevation"
    threshold = 10000
    analyze_watersheds(elevation, threshold)
