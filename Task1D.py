
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():

    #builds station input list
    stations = build_station_list()

    #creates a set of rivers using the function and sorts it, then prints the required data
    rivers = rivers_with_station(stations)
    rivers = sorted(rivers)
    print( len(rivers), 'rivers. First 10 - ', rivers[:10] )
    
    

