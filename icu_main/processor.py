from ai_generator import ai_thoughts
from sensorData import genNumbers
from settings_generator import time_display_change
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
	data.update({'time_setting' : time_setting});
	# This portion deals with the current alert status
	# For example '000' would be all normal
	# Another example '210' high hr, low fp, normal bp
	alert_code = '';
	for status in alerts:
        if current_alerts[0] == 'h':
			alert_code = alert_code + '2';
		elif current_alerts[0] == 'l':
			alert_code = alert_code + '1';
		else:
			alert_code = alert_code + '0';
	data.update({'alert_code' : alert_code});
    
	return data;

def update_alert_status(alerts):
	# Updates a global variable with the current alert status
	# that the processor uses.
	global current_alerts;
	current_alerts = alerts;
	return True;
	
# if __name__ == '__main__':
	# print(processData());