import Graph_in_py
import adc_code
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

while True:
    start_time=datetime.now().timestamp()
    while datetime.now().timestamp()-start_time<10:
        adc_code.collect()
    plt.clf()
    plt.clf()
    plt.clf()
    plt.close('all')
    adc_code.dataframe()
    Graph_in_py.update_csv()

    #For most accurate results, do not make a plot during code running. However,
    #it is an option if live results are needed or user preference favors live

    #This string is code that makes a plot with three subplots, one for each
    #category. plt.pause needs to be at most 1 second so that code has time to
    #plot before continuing to take measurements (if doesn't work, up time)
    """fig, axs = plt.subplots(3)
    axs[0].plot("Datetime", "ADC Values Ch1", data=Graph_in_py.update_csv())
    axs[0].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[1].plot("Datetime", "Drop Occurences Ch1", data=Graph_in_py.update_csv())
    axs[1].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[2].plot("Datetime", "Cumulative Drops Ch1", data=Graph_in_py.update_csv())
    axs[2].xaxis.set_major_locator(MaxNLocator(nbins=5))"""

    #This line should be commented out if using the other graph setup.
    #Only graphs the cumulative raindrops over time, leaving out other two
    #If using this version, graph should need at most 0.1 seconds to process
    Graph_in_py.graph_cumulative()
    

    plt.draw()
    #change seconds in pause depending on version of graph chosen
    plt.pause(0.1)
    
    
    
        
    
    
