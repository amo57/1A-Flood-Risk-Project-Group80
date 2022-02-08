from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
MonitoringStation

def run():
    stations = build_station_list()
    r = 10
    centre = (52.2053, 0.1218)
    x = stations_within_radius(stations, centre, r)
    print(x)

run()
