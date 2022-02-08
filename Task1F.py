from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations_list = []
    for station in inconsistent_stations:
        stations_list.append(station.name)
    
    print(sorted(stations_list))

run() 