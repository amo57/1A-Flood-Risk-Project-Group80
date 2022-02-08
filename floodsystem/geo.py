# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from haversine import haversine
from .utils import sorted_by_key  # noqa



def stations_by_distance(stations, p):
    stations_name = []
    stations_towns = []
    stations_distance = []
    for station in stations:
        distance = haversine(p, station.coord)
        if station is not stations:
            stations_name.append(station.name)
            stations_towns.append(station.town)
            stations_distance.append(distance)
        else:
            pass
    tuples = list(zip(stations_name, stations_towns, stations_distance))
    tuples = sorted_by_key(tuples, 2)
    return tuples

def stations_within_radius(stations, centre, r):
    station_list = []
    for i in stations:
        distance = haversine(centre, i.coord)
        if distance <= r:
            station_list.append(i.name)
        elif distance > r:
            pass
    station_list = sorted(station_list)
    return station_list

def rivers_with_station(stations):
    river_station = []
    for station in stations:
        if not station.river in river_station:
            river_station = river_station.append(station.river)
    river_station = sorted(river_station)  
    return river_station

def stations_by_river(stations):
    rivers = {}
    for value in rivers_with_station(stations):
        for station in stations:
            
        rivers.update({value: station})
    return