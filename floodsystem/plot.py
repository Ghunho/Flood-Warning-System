

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np


def plot_water_levels(station, dates, levels):
    ## Plots water level data against time for a given station.##


    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title("station: " + station.name)
    plt.tight_layout()
    plt.show()



def plot_water_level_with_fit(station, dates, levels, p, show_typical_range = True):
    """Plot water levels for a station with polyfit.
    Also accepts lists as input, showing up to the first 6 stations."""

    if isinstance(station, list):
        if len(station) >= 6:
            stations = station[0:6]
            length = 6
        else:
            stations = station
            length = len(stations)
        for i in range(length):
            plt.subplot(int(length / 3) + 1, (int(length / 2) > 0) + int(length / 5) + 1, i + 1)
            plt.plot(dates[i], levels[i])
            x = matplotlib.dates.date2num(dates[i])
            poly, shift = polyfit(dates[i], levels[i], 4)
            if not poly == None:
                plt.plot(x, poly(x - shift))
            if show_typical_range:
                plt.plot(x, [stations[i].typical_range[0]] * len(x), 'g--')
                plt.plot(x, [stations[i].typical_range[1]] * len(x), 'g--')
            plt.xlabel("Dates")
            plt.ylabel("Water Level (m)")
            plt.xticks(rotation=45);
            plt.title(stations[i].name)

            # Display plot
            plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()

    else:
        plt.plot(dates, levels)
        plt.xlabel("Dates")
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation=45);
        plt.title(station.name)
        poly, x1 = polyfit(dates, levels, 4)
        plt.plot(poly, x1)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()