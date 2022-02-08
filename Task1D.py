
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():

    #builds station input list
    stations = build_station_list()

    #
    rivers = rivers_with_station(stations)
    rivers = sorted(rivers)

    
    

