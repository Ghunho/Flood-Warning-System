# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation

def stations_by_distance(stations, p):
    return sorted_by_key([(station, haversine(station.coord, p)) for station in stations], 1)

def stations_within_radius(stations, centre, r):
    station_distances = stations_by_distance(stations, centre)
    return [entry[0] for entry in station_distances if entry[1] <= r]
    
def rivers_with_station(stations):
    rivers=[]
    for station in stations:
        if not station.river in rivers:
            rivers.append(station.river)
    return rivers

def stations_by_river(stations):
    stations_in_river={}
    for river in rivers_with_station(stations):
        stations_list = []
        for station in stations_list:
            if station.river == river:
                stations_list.append(station)
        stations_in_river[river] = stations_list
    return stations_in_river

def rivers_by_station_number(stations, N):
    stations_list = list()


