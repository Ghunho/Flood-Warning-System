

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from floodsystem.analysis  import *

def plot_water_levels(station, dates, levels):
    ## Plots water level data against time for a given station.##


    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title("station: " + station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    
    datesConverted = matplotlib.dates.date2num(dates)


    datesShifted = []
    for date in datesConverted:
        datesShifted.append(date - datesConverted[-1])

    #Calculate polynomial and shift
    poly, d0 = polyfit(datesShifted, levels, p)
    
    # Plot original data points
    plt.plot(dates, levels, '.')

    #Plot polynomial fit at 30 points along interval
    x1 = np.linspace(datesShifted[0], datesShifted[-1], 30)
    plt.plot(np.linspace(datesConverted[0], datesConverted[-1], 30), poly(x1))

    plt.axhline(y=station.typical_range[0], color='grey', linestyle='--')
    plt.axhline(y=station.typical_range[1], color='grey', linestyle='--')
    

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.show()