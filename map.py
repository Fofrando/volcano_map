from turtle import fillcolor
import folium
import pandas

#data = pandas.read_csv("C:\\Programovani\\Python\\mapping\\volcanoes.txt")
data = pandas.read_csv("vul.csv", sep=";")
lat = list(data["LAT"])
lon = list(data["LON"])
jmeno = list(data["Name"])
typ = list(data["Type"])
#vyska = list(data["ELEV"])

map = folium.Map(location=[50.09, 14.47], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Map of Volcanoes")

for lt, ln,nam, typ  in zip(lat, lon, jmeno, typ):
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius = 7,color='red',fill = True,fillcolor = 'red',popup="Name:"+str(nam)+"\nType:"+str(typ)))
#icon=folium.Icon(color='red',icon_color='orange'
#fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("Map1.html")
