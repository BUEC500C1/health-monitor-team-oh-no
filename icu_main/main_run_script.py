'''
This script is meant to organize all function calls into one location
'''

from save_sensor_data import sensorDataSaver
from sensorData import genNumbers
from settings_generator import time_display_change
from processor import processData
from basicgui import *
import vitals_alert
import csv
import pandas as pd
from multiprocessing import Process

from datetime import datetime
from time import sleep


global time_setting;
global current_alerts;
time_setting = time_display_change(); # Can create a thread that changes it periodically.
current_alerts = [['n', 0], ['n', 0], ['n', [0, 0]]];
def func1():
    
    fieldnames = ["x_value", "blood_pressure", "blood_pressureb", "heart_rate", "footPressure", "time_setting", "alert"]

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
    csvClass = sensorDataSaver();
    va = vitals_alert.vitals_alert();

    while True:
        vitals = genNumbers();
#        print(vitals) # Debug
        va.set_vitals(vitals);
        current_alerts = va.check_vitals(); # Could run as thread;
        timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        csvClass.appendrow(timestamp, 
                           heartRate=f'{vitals["heartRate"]}',
                           bloodPressure=f'{vitals["bloodPressure"]}',
                           oxygenLevel=f'{vitals["footPressure"]}')
                           
        processedData = processData(vitals,current_alerts,time_setting);
        
#        print(processedData)
        
        if processedData['alert_code'][0] == "2":
            print ("ALERT: HIGH BLOOD PRESSURE")
        if(processedData['alert_code'][1] == "2"):
            print ("ALERT: HIGH HEART RATE")
        if(processedData['alert_code'][2] == "2"):
            print ("ALERT: HIGH FOOT PRESSURE")
        print("\n")
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            info = {
               "x_value":  processedData['count'],
               "blood_pressure": processedData['bloodPressure'][0],
               "blood_pressureb": processedData['bloodPressure'][1],
               "heart_rate": processedData['heartRate'],
               "footPressure": processedData['footPressure'],
               "time_setting" : processedData['time_setting'],
               "alert": processedData['alert_code']
            }
               
            csv_writer.writerow(info)

        # Display will have to run a function to append the processed data here.
        # Can run this file to see what the processor outputs. 
        # Updating the display could probably be done from a thread.
        sleep(1); # Collects data every 1 second.
        
def func2():
    display_result(time_setting)

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p2.join()
  p1.join()
