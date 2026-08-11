import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import pandas as pd
import datetime
import numpy as np


drops1 = 0
drops2 = 0
drop1_ct = []
drop2_ct = []
adc_data1 = []
adc_data2 = []
volts1 = []
volts2 = []
drop_time1 = []
drop_time2=[]
drops3 = 0
drops4 = 0
drop3_ct = []
drop4_ct = []
adc_data3 = []
adc_data4 = []
volts3 = []
volts4 = []
drop_time3 = []
drop_time4=[]
drops5 = 0
drops6 = 0
drop5_ct = []
drop6_ct = []
adc_data5 = []
adc_data6 = []
volts5 = []
volts6 = []
drop_time5 = []
drop_time6=[]
drops7 = 0
drops8 = 0
drop7_ct = []
drop8_ct = []
adc_data7 = []
adc_data8 = []
volts7 = []
volts8 = []
drop_time7 = []
drop_time8=[]

drops1_1 = 0
drops1_2 = 0
drop1_1_ct = []
drop1_2_ct = []
adc_data1_1 = []
adc_data1_2 = []
volts1_1 = []
volts1_2 = []
drop_time1_1 = []
drop_time1_2=[]
drops1_3 = 0
drops1_4 = 0
drop1_3_ct = []
drop1_4_ct = []
adc_data1_3 = []
adc_data1_4 = []
volts1_3 = []
volts1_4 = []
drop_time1_3 = []
drop_time1_4=[]
drops1_5 = 0
drops1_6 = 0
drop1_5_ct = []
drop1_6_ct = []
adc_data1_5 = []
adc_data1_6 = []
volts1_5 = []
volts1_6 = []
drop_time1_5 = []
drop_time1_6=[]
drops1_7 = 0
drops1_8 = 0
drop1_7_ct = []
drop1_8_ct = []
adc_data1_7 = []
adc_data1_8 = []
volts1_7 = []
volts1_8 = []
drop_time1_7 = []
drop_time1_8=[]

dates = []
total_drops_sec = []

sampling_time = 10
prev_total_drops_sec = 0

i=0
sample_id = []

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)
cs1 = digitalio.DigitalInOut(board.D6)

mcp = MCP.MCP3008(spi, cs)
mcp1 = MCP.MCP3008(spi, cs1)

chan1 = AnalogIn(mcp, MCP.P0)
chan2 = AnalogIn(mcp, MCP.P1)
chan3 = AnalogIn(mcp, MCP.P2)
chan4 = AnalogIn(mcp, MCP.P3)
chan5 = AnalogIn(mcp, MCP.P4)
chan6 = AnalogIn(mcp, MCP.P5)
chan7 = AnalogIn(mcp, MCP.P6)
chan8 = AnalogIn(mcp, MCP.P7)

chan1_1 = AnalogIn(mcp1, MCP.P0)
chan1_2 = AnalogIn(mcp1, MCP.P1)
chan1_3 = AnalogIn(mcp1, MCP.P2)
chan1_4 = AnalogIn(mcp1, MCP.P3)
chan1_5 = AnalogIn(mcp1, MCP.P4)
chan1_6 = AnalogIn(mcp1, MCP.P5)
chan1_7 = AnalogIn(mcp1, MCP.P6)
chan1_8 = AnalogIn(mcp1, MCP.P7)


def noise_filter(va_data, vo_data, dropnum, dropdata, timedata):
    global i
    start_ind = sample_id.index(i)
    end_ind = len(sample_id)-1
    sample_vaarray=[]
    sample_voarray=[]

    j=start_ind
    while end_ind>=j:
        sample_vaarray.append(va_data[j])
        sample_voarray.append(vo_data[j])
        j+=1
        
    Q1Va=np.percentile(sample_vaarray, 25, method='midpoint')
    Q1Vo=np.percentile(sample_voarray, 25, method='midpoint')
    Q3Va=np.percentile(sample_vaarray, 75, method='midpoint')
    Q3Vo=np.percentile(sample_voarray, 75, method='midpoint')
    VaIQR = Q3Va-Q1Va
    VoIQR=Q3Vo-Q1Vo
    lower_va=Q1Va-8*VaIQR #8 was just the value that worked best
    lower_vo=Q1Vo-8*VoIQR
    
    j=start_ind
    while end_ind>=j:
        if va_data[j]<=lower_va and va_data[j-1]>lower_va and vo_data[j]>lower_vo:
            dropnum+=1
            timedata.append(1)
        elif vo_data[j]<=lower_vo and vo_data[j-1]>lower_vo:
            dropnum+=1
            timedata.append(1)
        else:
            timedata.append(0)
        dropdata.append(dropnum)
        
        j+=1
        
        

def collect():

    global drops1
    global drops2
    global drops3
    global drops4
    global drops5
    global drops6
    global drops7
    global drops8
    global drops1_1
    global drops1_2
    global drops1_3
    global drops1_4
    global drops1_5
    global drops1_6
    global drops1_7
    global drops1_8
    global prev_total_drops_sec
    

    adc_data1.append(chan1.value)
    volts1.append(chan1.voltage)
    
    
    adc_data2.append(chan2.value)
    volts2.append(chan2.voltage)


    adc_data3.append(chan3.value)
    volts3.append(chan3.voltage)

    
    adc_data4.append(chan4.value)
    volts4.append(chan4.voltage)


    adc_data5.append(chan5.value)
    volts5.append(chan5.voltage)

    
    adc_data6.append(chan6.value)
    volts6.append(chan6.voltage)



    adc_data7.append(chan7.value)
    volts7.append(chan7.voltage)

    
    adc_data8.append(chan8.value)
    volts8.append(chan8.voltage)


    adc_data1_1.append(chan1_1.value)
    volts1_1.append(chan1_1.voltage)


    adc_data1_2.append(chan1_2.value)
    volts1_2.append(chan1_2.voltage)


    adc_data1_3.append(chan1_3.value)
    volts1_3.append(chan1_3.voltage)


    adc_data1_4.append(chan1_4.value)
    volts1_4.append(chan1_4.voltage)
    

    adc_data1_5.append(chan1_5.value)
    volts1_5.append(chan1_5.voltage)

    adc_data1_6.append(chan1_6.value)
    volts1_6.append(chan1_6.voltage)


    adc_data1_7.append(chan1_7.value)
    volts1_7.append(chan1_7.voltage)
    

    adc_data1_8.append(chan1_8.value)
    volts1_8.append(chan1_8.voltage)

    
    dates.append(datetime.datetime.now())
    total_drops_sec.append(prev_total_drops_sec)
    sample_id.append(i)
    
    
def increase_i():
    global i
    i+=1
    
def backfill_drops():
    
    if len(total_drops_sec) > 0:
        start = sample_id.index(i)
        end = len(dates)-1
        k=start
        while k<=end:
            total_drops_sec[k]=prev_total_drops_sec
            k+=1
    else:
        total_drops_sec.append(prev_total_drops_sec)
    


def drops_per_sec(channel):
    #"channel" input for this function is drop_ct list for chosen channel
    accumulation = 0
    start = sample_id.index(i)
    end = len(dates)-1
    accumulation = channel[end]-channel[start]
    return float(float(accumulation)/float(sampling_time))

def total_drops_per_sec():
    global prev_total_drops_sec
    prev_total_drops_sec = drops_per_sec(drop1_ct) + drops_per_sec(drop2_ct) + drops_per_sec(drop3_ct)+drops_per_sec(drop4_ct)+drops_per_sec(drop5_ct)+drops_per_sec(drop6_ct)+drops_per_sec(drop7_ct)+drops_per_sec(drop8_ct)+drops_per_sec(drop1_1_ct)+drops_per_sec(drop1_2_ct)+drops_per_sec(drop1_3_ct)+drops_per_sec(drop1_4_ct)+drops_per_sec(drop1_5_ct)+drops_per_sec(drop1_6_ct)+drops_per_sec(drop1_7_ct)+drops_per_sec(drop1_8_ct)
    return prev_total_drops_sec

def dataframe():
    df= pd.DataFrame(list(zip(dates, sample_id, volts1, volts2, volts3, volts4, volts5, volts6, volts7, volts8, volts1_1, volts1_2, volts1_3, volts1_4, volts1_5, volts1_6, volts1_7, volts1_8, adc_data1, adc_data2, adc_data3, adc_data4, adc_data5, adc_data6, adc_data7, adc_data8, adc_data1_1, adc_data1_2, adc_data1_3, adc_data1_4, adc_data1_5, adc_data1_6, adc_data1_7, adc_data1_8, drop_time1, drop_time2, drop_time3, drop_time4, drop_time5, drop_time6, drop_time7, drop_time8, drop_time1_1, drop_time1_2, drop_time1_3, drop_time1_4, drop_time1_5, drop_time1_6, drop_time1_7, drop_time1_8, drop1_ct, drop2_ct, drop3_ct, drop4_ct, drop5_ct, drop6_ct, drop7_ct, drop8_ct, drop1_1_ct, drop1_2_ct, drop1_3_ct, drop1_4_ct, drop1_5_ct, drop1_6_ct, drop1_7_ct, drop1_8_ct, total_drops_sec)),
                     columns = ["Datetime", "Sample ID", "ADC Volts Ch1","ADC Volts Ch2", "ADC Volts Ch3", "ADC Volts Ch4", "ADC Volts Ch5", "ADC Volts Ch6", "ADC Volts Ch7", "ADC Volts Ch8", "ADC Volts Ch1_1", "ADC Volts Ch1_2", "ADC Volts Ch1_3", "ADC Volts Ch1_4", "ADC Volts Ch1_5", "ADC Volts Ch1_6", "ADC Volts Ch1_7", "ADC Volts Ch1_8", "ADC Values Ch1", "ADC Values Ch2", "ADC Values Ch3", "ADC Values Ch4", "ADC Values Ch5", "ADC Values Ch6", "ADC Values Ch7", "ADC Values Ch8", "ADC Values Ch1_1", "ADC Values Ch1_2", "ADC Values Ch1_3", "ADC Values Ch1_4", "ADC Values Ch1_5", "ADC Values Ch1_6", "ADC Values Ch1_7", "ADC Values Ch1_8", "Drop Occurences Ch1", "Drop Occurences Ch2", "Drop Occurences Ch3", "Drop Occurences Ch4", "Drop Occurences Ch5", "Drop Occurences Ch6", "Drop Occurences Ch7", "Drop Occurences Ch8", "Drop Occurences Ch1_1", "Drop Occurences Ch1_2", "Drop Occurences Ch1_3", "Drop Occurences Ch1_4", "Drop Occurences Ch1_5", "Drop Occurences Ch1_6", "Drop Occurences Ch1_7", "Drop Occurences Ch1_8", "Cumulative Drops Ch1", "Cumulative Drops Ch2", "Cumulative Drops Ch3", "Cumulative Drops Ch4", "Cumulative Drops Ch5", "Cumulative Drops Ch6", "Cumulative Drops Ch7", "Cumulative Drops Ch8", "Cumulative Drops Ch1_1", "Cumulative Drops Ch1_2", "Cumulative Drops Ch1_3", "Cumulative Drops Ch1_4", "Cumulative Drops Ch1_5", "Cumulative Drops Ch1_6", "Cumulative Drops Ch1_7", "Cumulative Drops Ch1_8", "Total Drops per Second"])
    df.to_csv('precipitation.csv', index=False)
