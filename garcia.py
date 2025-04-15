import grass.script as gs

def get_coordinates(points):
    """Helper function to get coordinate pairs from a vector point layer.
    Do not modify."""
    data = gs.read_command("v.out.ascii", input=points, separator="comma").splitlines()
    return [[float(coor) for coor in point.split(",")[:2]] for point in data]

def create_lake(elevation, points, depth=5.0):
    """Creates a lake upstream of given point using an elevation model"""
    coordinates = get_coordinates(points)
    if coordinates:
        seed_loc = gs.raster.raster_what('elevation', [coordinates[10]])
        seed_elev = float(seed_loc[0]['elevation']['value'])
        water_level = seed_elev + depth
        gs.run_command("r.lake", elevation="elevation", lake="lake", coordinates=coordinates, water_level=water_level)

if __name__ == "__main__":
    elevation = "elevation"
    points = "lagoon_points"
    create_lake(elevation=elevation, points=points)
