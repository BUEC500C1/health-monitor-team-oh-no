from ai_jenny.ai_generator import ai_thoughts
from sensors_brian.sensorData import genNumbers
from settings_jenny.settings_generator.py import time_display_change
import time

global current_alerts;

def processData():
    global current_alerts;
    try:
        data = genNumbers();
    except:
        print('Error retrieving data.')
        return False;
    try: 
        time_setting = time_display_change();
    except:
        print('Error retrieving time settings.');
        return False;
    try:
        vital_trend = ai_thoughts(healthmonitor.csv);
    except:
        print('Error retrieving time settings.');
        # return False;
    # Any type of data manipulation
    
    # What is returned?
    return True;

def update_alert_status(alerts):
    # Updates a global variable with the current alert status
    # that the processor uses.
    # Could also write it to a file and read it so that this 
    # does not need to be run as a thread. 
    global current_alerts;
    current_alerts = alerts;
    return True;