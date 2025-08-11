import map_maker
from math import radians, sin, cos, sqrt, atan2

url = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_FRA_4.json"

points = map_maker.import_points("places.txt")

def min_dist(centroid):
    distances = []
    for p in points:
        distances.append(centroid.distance(p))
    
    def haversine(lon1, lat1, lon2, lat2):
        R = 6371  # Earth radius in kilometers
        dlon = radians(lon2 - lon1)
        dlat = radians(lat2 - lat1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    km_distances = []
    for p in points:
        lon1, lat1 = centroid.x, centroid.y
        lon2, lat2 = p.x, p.y
        km_distances.append(haversine(lon1, lat1, lon2, lat2))
    return 0 if min(km_distances) > 60 else 1

map_maker.Map(
    url=url,
    on_draw=min_dist,
    title = "Regions which centres are less the 60 km from a property"
).render()

