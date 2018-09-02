import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return "green"
    elif elevation >= 2000 and elevation <= 3000:
        return "blue"
    else:
        return "red"

map = folium.Map(location = [38.58,-99.09], zoom_start=4, tiles = "Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln] , popup = "Elevation: "+str(int(el)) +" metres", fill_color = color_producer(el), color = "grey", fill_opacity = 0.8, radius = 6))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
style_function= lambda x:{"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "yellow" if 1000000 <= x["properties"]["POP2005"] < 50000000
else "blue" if 5000000 <= x["properties"]["POP2005"] < 100000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("mapUSA.html")
