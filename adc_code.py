import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import pandas as pd
import datetime

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
dates = []


spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

#yellow wire
chan1 = AnalogIn(mcp, MCP.P0)

#green wire
chan2 = AnalogIn(mcp, MCP.P1)


def noise_filter(data, channel):
    #approximate normal (unimpeded) values are around 61000
    if data<55000 and channel[len(channel)-2]>55000:
        return 1
    else:
        return 0
        

def collect():
    global drops1
    global drops2
    
    adc_data1.append(chan1.value)
    volts1.append(chan1.voltage)
    if noise_filter(chan1.value, adc_data1) == 1:
        drops1+=1
        drop_time1.append(1)
    else:
        drop_time1.append(0)

    drop1_ct.append(drops1)
    adc_data2.append(chan2.value)
    volts2.append(chan2.voltage)
    if noise_filter(chan2.value, adc_data2) == 1:
        drops2+=1
        drop_time2.append(1)
    else:
        drop_time2.append(0)

    drop2_ct.append(drops2)
    dates.append(datetime.datetime.now().replace(microsecond=0))
    print("Raw ADC Value Channel 1: ", chan1.value)
    print("ADC Voltage Channel 1: " + str(chan1.voltage) + "V")
    print(drops1)
    print("Raw ADC Value Channel 2: ", chan2.value)
    print("ADC Voltage Channel 2: " + str(chan2.voltage) + "V")
    print(drops2)
    print("--------------------------")
    time.sleep(.1)

def dataframe():
    df= pd.DataFrame(list(zip(dates, volts1, volts2, adc_data1, adc_data2, drop_time1, drop_time2, drop1_ct, drop2_ct)), columns = ["Datetime", "ADC Volts Ch1","ADC Volts Ch2", "ADC Values Ch1", "ADC Values Ch2", "Drop Occurences Ch1", "Drop Occurences Ch2", "Cumulative Drops Ch1", "Cumulative Drops Ch2"])
    df.to_csv('precipitation.csv', index=False)
