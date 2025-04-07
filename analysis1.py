import grass.script as gs

def get_
coordinates(points):
    """Function to get coordinate pairs from a vector point layer.
    Do not modify."""
    data = gs.read_command("v.out.ascii", input=points, separator="comma").splitlines()
    return [[float(coor) for coor in point.split(",")[:2]] for point in data]

# modify here
# change function name
def analysis1(elevation, points):
    """Traces a flow through an elevation model"""
    coordinates = get_coordinates(points)
    gs.run_command("r.drain", input=elevation, output="drain", output="drain_raster", drain="drain_vector", start_coordinates=coordinates)

if __name__ == "__main__":
    elevation = "elevation"
    points = "lagoon_points"
    analysis(elevation=elevation, points=points)