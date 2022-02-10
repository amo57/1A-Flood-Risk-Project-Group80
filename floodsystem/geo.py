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
        station_1 = []
        for station in stations:
            station_1.append(station.name)
        rivers.update({value: station_1})
    return rivers

def rivers_by_station_number(stations, N):
    rivers_name = []
    stations_number = []
    for station in stations:
        if station.river not in rivers_name:
            rivers_name.append(station.river)
        else:
             pass
    for i in rivers_name:  ## start looping through the river_name list
        a = 0  ## counting 
        for n in stations: ## double loop, to loop through the big stations list
            if i == n.river:
                a += 1
            else:
                pass
        stations_number.append(a)
    tuples = list(zip(rivers_name, stations_number))
    tuples = sorted_by_key(tuples, 1)
    tuples = tuples[::-1]
    """To set the number of outputs based on the number ranking of stations (intead of pre positions of river in rivers_name list) """
    """Assuming we start counting at 1, i.e 1,2,3.... Hence the N-1 is shown below"""
    Low_bound_station = tuples[N-1][1]
    count = 0
    for i in tuples:  ## start looping through the list of tuples
        if i[1] >= Low_bound_station:
            count += 1
        if i[1] < Low_bound_station:
            break

    return tuples[:count]
