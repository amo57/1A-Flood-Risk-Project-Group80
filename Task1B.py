from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Function to produce two lists, one for the 10 closest stations, the other one for the 10 furthest stations"""
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    print("The 10 closest stations from Cambridge are {}".format(x[:10]))
    print("The 10 furthest stations from Cambridge are {}".format(x[-10:]))
run()
