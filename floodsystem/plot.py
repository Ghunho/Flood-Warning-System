import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np



def plot_water_levels(station, dates, levels):
    ##function displaying the water levels at different timeline for different stations##

    plt.plot(dates,levels)
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.title("station: " + station.name) 
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()