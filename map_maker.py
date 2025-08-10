import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import requests
import tempfile
import os
from math import radians, sin, cos, sqrt, atan2

class Map:
    def __init__(self, title, url, on_draw):
        self.title = title
        self.url = url
        self.on_draw = on_draw
    
    def render (self):
        with tempfile.TemporaryDirectory() as tmpdir:
            geojson_path = os.path.join(tmpdir, "france_regions.geojson")

            # Download file
            r = requests.get(self.url)
            r.raise_for_status()
            with open(geojson_path, "wb") as f:
                f.write(r.content)

            gdf = gpd.read_file(geojson_path)

            # If CRS is not WGS84 (EPSG:4326), convert it
            if gdf.crs != "EPSG:4326":
                gdf = gdf.to_crs("EPSG:4326")

            gdf['centroid'] = gdf.geometry.centroid


            gdf['min_distance'] = gdf['centroid'].apply(self.on_draw)

            
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            gdf.plot(column='min_distance', ax=ax, legend=True,
                    cmap='viridis', edgecolor='black', linewidth=0.8)
            ax.set_title(self.title)
            ax.set_axis_off()
            plt.show()

def import_points(points_file):
    points = []
    places_file = open(points_file, "r")
    content = places_file.read()
    for line in content.split(";"):
        if line.strip():
            lon, lat = map(float, line.split(","))
            points.append(Point(lat, lon))
    places_file.close()
    print(f"Imported {len(points)} points from places.txt")
    return points
