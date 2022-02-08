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
    rivers_stations_dict={}
    for river in rivers_with_station(stations):
        rivers_stations_dict[river] = sorted([station.name for station in stations if station.river == river])
    return rivers_stations_dict


def rivers_by_station_number(stations, N):
    rivers = rivers_with_station(stations)
    rivers_counted = []
    for river in rivers:
        count = 0 
        for station in stations:
            if station.river ==river:
                count +=1
        rivers_counted.append((river,count))
        #sorting list according to the number of rivers in descending order 
    rivers_counted = sorted_by_key(rivers_counted,1,reverse=True)
    #when the next river has the sanme number of stations as the previous one, we include the next one too. 
    while rivers_counted[N-1][1] == rivers_counted[N][1]:
        N +=1
    return rivers_counted[:N]

