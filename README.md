# Map Maker 🌍

A simple wrapper around geopandas and matplotlib to reduce boilerplate code and make the actual maps nice. The library is map_maker.

## Examples
```
import map_maker
import weather

url = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_FRA_2.json" # linnk to geodata of regions

def rainfall(centroid):
    # centroid.x longitude
    # centroid.y latitude
    # do whatever you want to colour in the map
    temp, rain =  weather.get_july_weather(centroid.y,centroid.x) # weather is just a wrapper around the open-meteo api
    return rain # return a number

map_maker.Map(
    title="Average millimetres rainfall per day of region",
    url=url, 
    on_draw=temperature
).render()
```

To get the geodata of somewhere go to: https://gadm.org/download_country.html and pick you country. They offer different levels, the higher the level the smaller and more regions there are.  
Weather uses the open-meteo api, which is free to use without any api keys, if you are doing weather maps try to only use Level 2 maps to avoid spamming them.

There are more examples in the repository that you can use/copy/modify for whatever you want:
- `france_hard_dist` - shows the regions which are within 60km of somewhere on a list of places
- `france_soft_dist` - shows the distance between a region and the closest of a list of places
- `france_temperature` - shows the average temperature of a region




## Gallery

![average_rainfall](https://github.com/Janjre/map_maker/blob/master/images/avg_rainfall.png?raw=true)
![avage_temperature](https://github.com/Janjre/map_maker/blob/master/images/avg_temp.png?raw=true)
![soft distance](https://github.com/Janjre/map_maker/blob/master/images/soft_dist.png?raw=true)
![hard distance](https://github.com/Janjre/map_maker/blob/master/images/hard_dist.png?raw=true)
