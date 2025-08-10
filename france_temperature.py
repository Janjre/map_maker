import map_maker
import weather

url = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_FRA_2.json"

def temperature(centroid):
    # centroid.x longitude
    # centroid.y latitude
    temp, rain =  weather.get_july_weather(centroid.y,centroid.x)
    return temp

map_maker.Map(
    title="Average temperature of region",
    url=url,
    on_draw=temperature
).render()

