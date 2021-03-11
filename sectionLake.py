from geojson import Point
import json
from shapely import geometry
import random

# To the West is more negative longitude
# North is higher latitude

# Generate random points to initialise K-means 
def generate_random(number, polygon):
    points = []
    minx, miny, maxx, maxy = polygon.bounds
    while len(points) < number:
        pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(pnt):
            points.append(pnt)
    return points


def main():
    with open("C:\\Users\\adamh\\OneDrive - University of Edinburgh\\Year3\\Semester 2\\System design project\\Navigation\\Example lochs\\StMargaretsLochSplit.GEOJSON", 'r') as f:
        data = f.read()
    
    oth = json.loads(data)
    coords = oth['features'][0]['geometry']['coordinates'][0]

    # Create polygon of lake...
    ShapelyPts = []
    for cord in coords:
        ShapelyPts.append(geometry.Point(cord[0],cord[1]))
    poly = geometry.Polygon(ShapelyPts)

    # Generate random points within the lake 
    points = generate_random(10000, poly)

    # Turn shapely points into geojson points 
    geojsonPts = []
    for point in points:
        geoJsonPts.append(Point(point.coords[0]))

if __name__ == '__main__':
    
    main()
    