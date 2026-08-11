
import pandas as pd
import matplotlib.pyplot as plt

data_name = 'precipitation.csv'

def update_csv():
    disdro_df = pd.read_csv(data_name)
    return disdro_df
    
def graph():
    #function not used in current code
    disdro_df = update_csv()

    values_plot = disdro_df.plot(x="Datetime", y="ADC Values Ch1")
    values_plot.set_xlabel("Datetime")
    values_plot.set_ylabel("Values Ch1")
    values_plot.set_title("Ch1 Values / Time")
    plt.gcf().autofmt_xdate()

    rainfall_plot = disdro_df.plot(x="Datetime", y="Cumulative Drops Ch1")
    rainfall_plot.set_xlabel("Datetime")
    rainfall_plot.set_ylabel("Drops Ch1")
    rainfall_plot.set_title("Cumulative Drops / Time")
    plt.gcf().autofmt_xdate()

    drops_plot = disdro_df.plot(x="Datetime", y="Drop Occurences Ch1")
    drops_plot.set_xlabel("Datetime")
    drops_plot.set_ylabel("Drops Ch1")
    drops_plot.set_title("Drops / Time")
    plt.gcf().autofmt_xdate()

def graph_cumulative():
    #function not used in current code
    disdro_df = update_csv()
    
    rainfall_plot = disdro_df.plot(x="Datetime", y="Cumulative Drops Ch1")
    rainfall_plot.set_xlabel("Datetime")
    rainfall_plot.set_ylabel("Drops Ch1")
    rainfall_plot.set_title("Drops / Time")
    plt.gcf().autofmt_xdate()
    
