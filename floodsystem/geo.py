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
    return sorted(list(set([station.river for station in stations])))

def stations_by_river(stations):
    rivers_stations_dict = {}
    for river in rivers_with_station(stations):
        rivers_stations_dict[river] = sorted([station.name for station in stations if station.river == river])
    return rivers_stations_dict