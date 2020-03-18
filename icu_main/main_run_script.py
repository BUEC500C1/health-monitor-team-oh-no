'''
This script is meant to organize all function calls into one location
'''

from storage_jp.save_sensor_data import sensorDataSaver
from sensors_brian.sensorData import genNumbers

from datetime import datetime
from time import sleep

csvClass = sensorDataSaver()
while True:
    vitals = genNumbers()
    print(vitals) # Debug
    timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    csvClass.appendrow(timestamp, 
                       heartRate=f'{vitals["heartRate"]}',
                       bloodPressure=f'{vitals["bloodPressure"]}',
                       oxygenLevel=f'{vitals["footPressure"]}')
    sleep(1)