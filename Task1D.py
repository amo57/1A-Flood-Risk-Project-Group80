
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():

    #builds station input list
    stations = build_station_list()

    #creates a set of rivers using the function and sorts it, then prints the required data
    rivers = rivers_with_station(stations)
    rivers = sorted(rivers)
    print( len(rivers), 'rivers. First 10 - ', rivers[:10] )
    
    stations_on_rivers = stations_by_river(stations)
    print("River Are Stations")
    print(stations_on_rivers["River Are"])
    print("River am Stations")
    print(stations_on_rivers["River Cam"])
    print("River Thames Stations")
    print(stations_on_rivers["River Thames"])

if __name__ == "__main__":
    print(" Task1D")
    run()

