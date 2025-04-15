import grass.script as gs

def get_coordinates(points):
    """Helper function to get coordinate pairs from a vector point layer.
    Do not modify."""
    data = gs.read_command("v.out.ascii", input=points, separator="comma").splitlines()
    return [[float(coor) for coor in point.split(",")[:2]] for point in data]

# modify here
# change function name
def TWI(elevation, points):
    """Traces a flow through an elevation model"""
    coordinates = get_coordinates(points)
    if coordinates:
        gs.run_command("r.drain", input=elevation, output="drain", drain="drain_vector", start_coordinates=coordinates)

if __name__ == "__main__":
    elevation = "elevation"
    points = "lagoon_points"
    TWI(elevation=elevation, points=points)
