from ai_generator import ai_thoughts
from sensorData import genNumbers
from settings_generator import time_display_change
import time

# These two global variables need to be put into the main function. 
global current_alerts;
current_alerts = [['n', 0], ['n', 0], ['n', [0, 0]]];
global time_setting;
time_setting = time_display_change(); # Could be a thread that calls the function every t seconds. 

def processData():
	global current_alerts;
	global time_setting;
	try:
		data = genNumbers();
	except:
		print('Error retrieving data.')
		return False;
	try:
		vital_trend = ai_thoughts('output/healthmonitor.csv');
	except:
		print('Error retrieving AI thoughts.');
		return False;
	data.update({'time_setting' : time_setting});
	# This portion deals with the current alert status
	# For example '000' would be all normal
	# Another example '210' high hr, low fp, normal bp
	alert_code = '';
	for status in current_alerts:
		if current_alerts[0] == 'h':
			alert_code = alert_code + '2';
		elif current_alerts[0] == 'l':
			alert_code = alert_code + '1';
		else:
			alert_code = alert_code + '0';
	data.update({'alert_code' : alert_code});
	
	return data;

# Haven't tested this yet. 
def update_alert_status(alerts):
	# Updates a global variable with the current alert status
	# that the processor uses.
	global current_alerts;
	current_alerts = alerts;
	return True;
	
	
if __name__ == '__main__':
	print(processData());