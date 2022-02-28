from floodsystem.stationdata import update_water_levels
from .utils import sorted_by_key

def stations_level_over_threshold(stations,tol):
    ##returns a list of tuples (Stations, relative water level) in descending water level for all stations with its water level bigger than the tolerance ##
    output_tuples = []
    update_water_levels(stations)

    for station in stations:
        if station.relative_water_level() == None or station.relative_water_level() < tol:
            pass ##only stations with consistent typical high / low data is considered##
        elif station.relative_water_level() > tol:
            output_tuples.append((station.name, station.relative_water_level()))
    output_tuples_sorted = sorted_by_key(output_tuples,1,reverse=True) ##sorted by the relative level in descending order##
    return output_tuples_sorted 
        
def stations_highest_rel_level(stations, N):
    return stations_level_over_threshold(stations,0)[:N] ##since stations_level_order_threshold is in descending order, starts from 0 till the nth station##