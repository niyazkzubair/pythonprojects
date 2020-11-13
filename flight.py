import urllib.request
import json
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#SEND QUERY (IN THE FUNCTION)
fp=opener.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.639722&lng=-73.778889&fDstL=0&fDstU=20')
mybyte=fp.read()
mystr=mybyte.decode("utf8")
js_str=json.loads(mystr)
fp.close()