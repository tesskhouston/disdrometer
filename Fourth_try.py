import Graph_in_py
import adc_code
import datetime

while True:
    start_time=datetime.now().timestamp()
    while datetime.now().timestamp()-start_time<10:
        adc_code.collect()
    adc_code.dataframe()
    Graph_in_py
    


