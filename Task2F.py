from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import datetime
import matplotlib 
from floodsystem.utils import sorted_by_key
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
 



def run():

    stations = build_station_list()

    update_water_levels(stations)

    #Remove stations with no data
    stations_with_water = []
    for station in stations:
        if station.latest_level != None:
            stations_with_water.append(station)

    sorted_by_water = sorted(stations_with_water, key=lambda MonitoringStation: MonitoringStation.latest_level, reverse=True)
    i = 0
    j = 0
    while j < 5:
        dates, levels = fetch_measure_levels(sorted_by_water[i].measure_id, dt=datetime.timedelta(days=2))

        try:
            plot_water_level_with_fit(sorted_by_water[i], dates, levels, 4)
            i+=1
            j+=1
        except:
            print(sorted_by_water[i].name + 'not enough data for the past two days')
            i+=1

run()