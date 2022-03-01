import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_level_with_fit


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 10

    stations_at_risk = stations_level_over_threshold(stations, 0.75)

    dates = []
    levels = []

    for station in stations_at_risk:
        results = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        dates.append(results[0])
        levels.append(results[1])

    plot_water_level_with_fit(stations_at_risk, dates, levels, 4)

    

if __name__ == "__main__":
    print("*** CUED Part IA Flood Warning System ***")
    run()
    