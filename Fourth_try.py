import Graph_in_py
import adc_code
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator


while True:
    start_time=datetime.now().timestamp()
    while datetime.now().timestamp()-start_time<adc_code.sampling_time:
        adc_code.collect()
    adc_code.noise_filter(adc_code.adc_data1, adc_code.volts1, adc_code.drops1, adc_code.drop1_ct, adc_code.drop_time1)
    adc_code.noise_filter(adc_code.adc_data2, adc_code.volts2, adc_code.drops2, adc_code.drop2_ct, adc_code.drop_time2)
    adc_code.noise_filter(adc_code.adc_data3, adc_code.volts3, adc_code.drops3, adc_code.drop3_ct, adc_code.drop_time3)
    adc_code.noise_filter(adc_code.adc_data4, adc_code.volts4, adc_code.drops4, adc_code.drop4_ct, adc_code.drop_time4)
    adc_code.noise_filter(adc_code.adc_data5, adc_code.volts5, adc_code.drops5, adc_code.drop5_ct, adc_code.drop_time5)
    adc_code.noise_filter(adc_code.adc_data6, adc_code.volts6, adc_code.drops6, adc_code.drop6_ct, adc_code.drop_time6)
    adc_code.noise_filter(adc_code.adc_data7, adc_code.volts7, adc_code.drops7, adc_code.drop7_ct, adc_code.drop_time7)
    adc_code.noise_filter(adc_code.adc_data8, adc_code.volts8, adc_code.drops8, adc_code.drop8_ct, adc_code.drop_time8)
    adc_code.noise_filter(adc_code.adc_data1_1, adc_code.volts1_1, adc_code.drops1_1, adc_code.drop1_1_ct, adc_code.drop_time1_1)
    adc_code.noise_filter(adc_code.adc_data1_2, adc_code.volts1_2, adc_code.drops1_2, adc_code.drop1_2_ct, adc_code.drop_time1_2)
    adc_code.noise_filter(adc_code.adc_data1_3, adc_code.volts1_3, adc_code.drops1_3, adc_code.drop1_3_ct, adc_code.drop_time1_3)
    adc_code.noise_filter(adc_code.adc_data1_4, adc_code.volts1_4, adc_code.drops1_4, adc_code.drop1_4_ct, adc_code.drop_time1_4)
    adc_code.noise_filter(adc_code.adc_data1_5, adc_code.volts1_5, adc_code.drops1_5, adc_code.drop1_5_ct, adc_code.drop_time1_5)
    adc_code.noise_filter(adc_code.adc_data1_6, adc_code.volts1_6, adc_code.drops1_6, adc_code.drop1_6_ct, adc_code.drop_time1_6)
    adc_code.noise_filter(adc_code.adc_data1_7, adc_code.volts1_7, adc_code.drops1_7, adc_code.drop1_7_ct, adc_code.drop_time1_7)
    adc_code.noise_filter(adc_code.adc_data1_8, adc_code.volts1_8, adc_code.drops1_8, adc_code.drop1_8_ct, adc_code.drop_time1_8)

    plt.clf()
    plt.close('all')
    adc_code.total_drops_per_sec()
    adc_code.backfill_drops()
    adc_code.dataframe()
    Graph_in_py.update_csv()

    #For most accurate results, do not use live plotting. However,
    #it is an option if live results are needed or user preference favors live
    
    fig, axs = plt.subplots(17)

    #Below lines should be commented out if using the other graph setup or not graphing live.
    #Graphs the cumulative raindrops over time
    
    axs[0].plot("Datetime", "Cumulative Drops Ch1", data=Graph_in_py.update_csv())
    axs[0].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[1].plot("Datetime", "Cumulative Drops Ch2", data=Graph_in_py.update_csv())
    axs[1].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[2].plot("Datetime", "Cumulative Drops Ch3", data=Graph_in_py.update_csv())
    axs[2].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[3].plot("Datetime", "Cumulative Drops Ch4", data=Graph_in_py.update_csv())
    axs[3].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[4].plot("Datetime", "Cumulative Drops Ch5", data=Graph_in_py.update_csv())
    axs[4].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[5].plot("Datetime", "Cumulative Drops Ch6", data=Graph_in_py.update_csv())
    axs[5].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[6].plot("Datetime", "Cumulative Drops Ch7", data=Graph_in_py.update_csv())
    axs[6].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[7].plot("Datetime", "Cumulative Drops Ch8", data=Graph_in_py.update_csv())
    axs[7].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[8].plot("Datetime", "Cumulative Drops Ch1_1", data=Graph_in_py.update_csv())
    axs[8].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[9].plot("Datetime", "Cumulative Drops Ch1_2", data=Graph_in_py.update_csv())
    axs[9].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[10].plot("Datetime", "Cumulative Drops Ch1_3", data=Graph_in_py.update_csv())
    axs[10].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[11].plot("Datetime", "Cumulative Drops Ch1_4", data=Graph_in_py.update_csv())
    axs[11].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[12].plot("Datetime", "Cumulative Drops Ch1_5", data=Graph_in_py.update_csv())
    axs[12].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[13].plot("Datetime", "Cumulative Drops Ch1_6", data=Graph_in_py.update_csv())
    axs[13].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[14].plot("Datetime", "Cumulative Drops Ch1_7", data=Graph_in_py.update_csv())
    axs[14].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[15].plot("Datetime", "Cumulative Drops Ch1_8", data=Graph_in_py.update_csv())
    axs[15].xaxis.set_major_locator(MaxNLocator(nbins=5))
    
    #alternative graph setups:
    #ADC Values
    """axs[0].plot("Datetime", "ADC Values Ch1", data=Graph_in_py.update_csv())
    axs[0].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[1].plot("Datetime", "ADC Values Ch2", data=Graph_in_py.update_csv())
    axs[1].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[2].plot("Datetime", "ADC Values Ch3", data=Graph_in_py.update_csv())
    axs[2].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[3].plot("Datetime", "ADC Values Ch4", data=Graph_in_py.update_csv())
    axs[3].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[4].plot("Datetime", "ADC Values Ch5", data=Graph_in_py.update_csv())
    axs[4].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[5].plot("Datetime", "ADC Values Ch6", data=Graph_in_py.update_csv())
    axs[5].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[6].plot("Datetime", "ADC Values Ch7", data=Graph_in_py.update_csv())
    axs[6].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[7].plot("Datetime", "ADC Values Ch8", data=Graph_in_py.update_csv())
    axs[7].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[8].plot("Datetime", "ADC Values Ch1_1", data=Graph_in_py.update_csv())
    axs[8].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[9].plot("Datetime", "ADC Values Ch1_2", data=Graph_in_py.update_csv())
    axs[9].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[10].plot("Datetime", "ADC Values Ch1_3", data=Graph_in_py.update_csv())
    axs[10].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[11].plot("Datetime", "ADC Values Ch1_4", data=Graph_in_py.update_csv())
    axs[11].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[12].plot("Datetime", "ADC Values Ch1_5", data=Graph_in_py.update_csv())
    axs[12].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[13].plot("Datetime", "ADC Values Ch1_6", data=Graph_in_py.update_csv())
    axs[13].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[14].plot("Datetime", "ADC Values Ch1_7", data=Graph_in_py.update_csv())
    axs[14].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[15].plot("Datetime", "ADC Values Ch1_8", data=Graph_in_py.update_csv())
    axs[15].xaxis.set_major_locator(MaxNLocator(nbins=5))"""
    
    #ADC Volts
    """axs[0].plot("Datetime", "ADC Volts Ch1", data=Graph_in_py.update_csv())
    axs[0].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[1].plot("Datetime", "ADC Volts Ch2", data=Graph_in_py.update_csv())
    axs[1].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[2].plot("Datetime", "ADC Volts Ch3", data=Graph_in_py.update_csv())
    axs[2].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[3].plot("Datetime", "ADC Volts Ch4", data=Graph_in_py.update_csv())
    axs[3].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[4].plot("Datetime", "ADC Volts Ch5", data=Graph_in_py.update_csv())
    axs[4].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[5].plot("Datetime", "ADC Volts Ch6", data=Graph_in_py.update_csv())
    axs[5].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[6].plot("Datetime", "ADC Volts Ch7", data=Graph_in_py.update_csv())
    axs[6].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[7].plot("Datetime", "ADC Volts Ch8", data=Graph_in_py.update_csv())
    axs[7].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[8].plot("Datetime", "ADC Volts Ch1_1", data=Graph_in_py.update_csv())
    axs[8].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[9].plot("Datetime", "ADC Volts Ch1_2", data=Graph_in_py.update_csv())
    axs[9].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[10].plot("Datetime", "ADC Volts Ch1_3", data=Graph_in_py.update_csv())
    axs[10].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[11].plot("Datetime", "ADC Volts Ch1_4", data=Graph_in_py.update_csv())
    axs[11].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[12].plot("Datetime", "ADC Volts Ch1_5", data=Graph_in_py.update_csv())
    axs[12].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[13].plot("Datetime", "ADC Volts Ch1_6", data=Graph_in_py.update_csv())
    axs[13].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[14].plot("Datetime", "ADC Volts Ch1_7", data=Graph_in_py.update_csv())
    axs[14].xaxis.set_major_locator(MaxNLocator(nbins=5))
    axs[15].plot("Datetime", "ADC Volts Ch1_8", data=Graph_in_py.update_csv())
    axs[15].xaxis.set_major_locator(MaxNLocator(nbins=5))"""

    #used in every graph setup
    axs[16].plot("Datetime", "Total Drops per Second", data=Graph_in_py.update_csv())
    axs[16].xaxis.set_major_locator(MaxNLocator(nbins=5))
    
    plt.gcf().autofmt_xdate()

    plt.draw() #change to plt.show() to stop program until plots are closed
    plt.pause(1) #change seconds in pause depending on version of graph chosen.
    #seconds may need to be increased the longer the program runs (the graphs will be more complex)
    
    adc_code.increase_i()
    
