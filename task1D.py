from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    print("\n {} stations. First 10 - {}".format(len(rivers), rivers[:10]))

    rivers_stations_dict = stations_by_river(stations)
    print("\n Stations next to River Aire: {}".format(rivers_stations_dict['River Aire']))
    print("\n Stations next to River Cam: {}".format(rivers_stations_dict['River Cam']))
    print("\n Stations next to River Thames: {}".format(rivers_stations_dict['River Thames']))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()