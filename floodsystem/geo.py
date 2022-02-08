# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

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