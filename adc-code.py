import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import pandas as pd
import datetime

drops = 0
adc_data = []
volts = []
drop_time = []
dates = []
index = 0
last_drop = 0

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0)

def noise_filter(data):
    global drops
    global last_drop
    #approximate normal (unimpeded) values are around 61000
    if data<55000 and adc_data[len(adc_data)-2]>50000:
        drops+=1
        last_drop = index
        drop_time.append(1)
    else:
        drop_time.append(0)
        
    

def collect():
    adc_data.append(chan.value)
    volts.append(chan.voltage)
    noise_filter(chan.value)
    index = len(adc_data)
    dates.append(datetime.datetime.now().replace(microsecond=0))
    print("Raw ADC Value: ", chan.value)
    print("ADC Voltage: " + str(chan.voltage) + "V")
    print(drops)
    print("--------------------------")
    time.sleep(.1)

while True:
    collect()

    df= pd.DataFrame(list(zip(dates, volts, adc_data, drop_time)), columns = ["Datetime", "ADC Volts", "ADC Values", "Drops"])

    df.to_csv('precipitation.csv', index=False)
