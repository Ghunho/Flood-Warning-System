from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    stations = build_station_list()
    number_of_stations = len(stations)
    distances_from_cambridge = stations_by_distance(stations, (52.2053, 0.1218))

    print("Closest 10 stations:")
    print([(entry[0].name, entry[0].town, entry[1]) for entry in distances_from_cambridge[:10]])

    print("Furthest 10 stations:")
    print([(entry[0].name, entry[0].town, entry[1]) for entry in distances_from_cambridge[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
