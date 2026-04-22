# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

data_name = 'precipitation.csv'

def update_csv():
    disdro_df = pd.read_csv(data_name)
    return disdro_df
    
def graph():
    disdro_df = update_csv()

    # %%
    values_plot = disdro_df.plot(x="Datetime", y="ADC Values Ch1")
    values_plot.set_xlabel("Datetime")
    values_plot.set_ylabel("Values Ch1")
    values_plot.set_title("Ch1 Values / Time")
    plt.gcf().autofmt_xdate()

    # %%
    rainfall_plot = disdro_df.plot(x="Datetime", y="Cumulative Drops Ch1")
    rainfall_plot.set_xlabel("Datetime")
    rainfall_plot.set_ylabel("Drops Ch1")
    rainfall_plot.set_title("Drops / Time")
    plt.gcf().autofmt_xdate()

    # %%
    drops_plot = disdro_df.plot(x="Datetime", y="Drop Occurences Ch1")
    drops_plot.set_xlabel("Datetime")
    drops_plot.set_ylabel("Drops Ch1")
    drops_plot.set_title("Drops / Time")
    plt.gcf().autofmt_xdate()

def column(name):
    global disdro_df
    return disdro_df[name]



    



   
