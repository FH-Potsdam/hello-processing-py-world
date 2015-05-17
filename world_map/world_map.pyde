# world map image taken from here
# http://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/World_location_map_(equirectangular_180).svg/1280px-World_location_map_(equirectangular_180).svg.png
# checkout http://dbsgeo.com/latlon/ 
# for locations

worldmap = None

def setup():
    global worldmap
    worldmap = loadImage("world.png")
    size(worldmap.width,worldmap.height)
    worldmap.filter(GRAY)
    worldmap.filter(INVERT)
    
def draw():
    image(worldmap,0,0)
    #Berlin
    #float lon = 13.0
    #float lat = 52.0
    #San Francisco
    #Latitude, Longitude: 37.77493, -123.47410
    lon = -123
    lat = 37
    x = map(lon,-180,180,0,worldmap.width)
    y = map(lat,90,-90,0,worldmap.height)
    fill(255,255,0)
    ellipse(x,y,10,10)
