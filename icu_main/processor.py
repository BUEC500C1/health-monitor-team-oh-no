from ai_generator import ai_thoughts
from sensorData import genNumbers
from settings_generator import time_display_change
import time

def processData(data,current_alerts,time_setting):
	try:
		vital_trend = ai_thoughts('output/healthmonitor.csv'); # The file name could probably be an input
	except:
		print('Error retrieving AI thoughts.');
		return False; 
	data.update({'time_setting' : time_setting});
	# This portion deals with the current alert status
	# For example '000' would be all normal
	# Another example '210' high hr, low fp, normal bp
	alert_code = '';
	for status in current_alerts:
		if status[0] == 'h':
			alert_code = alert_code + '2';
		elif status[0] == 'l':
			alert_code = alert_code + '1';
		else:
			alert_code = alert_code + '0';
	data.update({'alert_code' : alert_code});
	
	return data;
	
# if __name__ == '__main__':
	# print(processData());