from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    """ Test returning a sorted list of (station, relative water level) tuples"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of tuples from stations_level_over_threshold with tol = 0.8
    stationsover = stations_level_over_threshold(stations, 0.8)

    # checks
    assert stationsover[0][1] > stationsover [1][1] #checks whether it's sorted by checking if the first station's water level is higher than the second one 
    assert stationsover[-1][1] > 0.8 #checks the last one is above 0.8



def test_stations_highest_rel_level():
    """Test returning a sorted list of the N stations at which the relative water 
    level is highest"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of def stations_highest_rel_level with N = 10
    Nstations = stations_highest_rel_level(stations, 10)

    # checks
    assert len(Nstations) == 10
    assert Nstations[0].relative_water_level() > Nstations[1].relative_water_level() # check if the first station's water level is bigger the second
    assert Nstations[-1].relative_water_level() < Nstations[-2].relative_water_level() #check if the last station's water level is smaller than the second last 


























