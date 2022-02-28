from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
##list of stations that have higher value than the tolerance##
    stations = build_station_list()
    tol = 0.8

##update the values for stations##
    update_water_levels(stations)

    print(stations_level_over_threshold(stations, tol))



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

