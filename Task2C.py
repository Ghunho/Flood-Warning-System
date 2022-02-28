from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
   ##list of 10 stations that has the highest level##
    stations = build_station_list() 

    #Update the values for stations
    update_water_levels(stations)
    print(stations_highest_rel_level(stations, 10)) ##list of 10 tuples (stations, water level)##


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()