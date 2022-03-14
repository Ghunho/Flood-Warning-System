# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, relative_risk

def test_create_monitoring_station():

    
    stations = build_station_list()
    for station in stations:
        numericalrisk = relative_risk(station)

        assert numericalrisk in [None, 0,1,2,3,4]
    print('done')
