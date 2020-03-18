'''
This script is meant to organize all function calls into one location
'''

from save_sensor_data import sensorDataSaver
from sensorData import genNumbers
from settings_generator import time_display_change
from processor import processData
import vitals_alert

from datetime import datetime
from time import sleep


global time_setting;
global current_alerts;
time_setting = time_display_change(); # Can create a thread that changes it periodically.
current_alerts = [['n', 0], ['n', 0], ['n', [0, 0]]];


if __name__ == '__main__':
    csvClass = sensorDataSaver();
    va = vitals_alert.vitals_alert();
    while True:
        vitals = genNumbers();
        print(vitals) # Debug
        va.set_vitals(vitals);
        current_alerts = va.check_vitals(); # Could run as thread;
        timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        csvClass.appendrow(timestamp, 
                           heartRate=f'{vitals["heartRate"]}',
                           bloodPressure=f'{vitals["bloodPressure"]}',
                           oxygenLevel=f'{vitals["footPressure"]}')
        processedData = processData(vitals,current_alerts,time_setting);
        print(processedData);
        # Display will have to run a function to append the processed data here.
        # Updating the display could probably be done from a thread.
        sleep(1); # Collects data every 1 second. 