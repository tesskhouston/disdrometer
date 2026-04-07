# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

data_name = 'precipitation.csv'



# %%
disdro_df = pd.read_csv(data_name)
disdro_df

# %%
values_plot = disdro_df.plot(x="Datetime", y="ADC Values Ch1")
values_plot.set_xlabel("Datetime")
values_plot.set_ylabel("Values Ch1")
values_plot.set_title("Ch1 Values / Time")
plt.gcf().autofmt_xdate()

# %%
drops_plot = disdro_df.plot(x="Datetime", y="Cumulative Drops Ch1")
drops_plot.set_xlabel("Datetime")
drops_plot.set_ylabel("Drops Ch1")
drops_plot.set_title("Drops / Time")
plt.gcf().autofmt_xdate()

# %%
drops_plot = disdro_df.plot(x="Datetime", y="Drop Occurences Ch1")
drops_plot.set_xlabel("Datetime")
drops_plot.set_ylabel("Drops Ch1")
drops_plot.set_title("Drops / Time")
plt.gcf().autofmt_xdate()


