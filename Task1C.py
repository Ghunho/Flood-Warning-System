from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()

    print("Stations within 10km of Cambridge City Centre:")
    print(sorted([station.name for station in stations_within_radius(stations, (52.2053, 0.1218), 10)]))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
