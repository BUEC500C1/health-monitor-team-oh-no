from processor import update_alert_status

class vitals_alert():

    def __init__(self):
        self.heartRate = 0
        self.footPressure = 0
        self.bloodPressure = [0, 0]
        # lower, upper thresholds
        self.heartRateThreshold = [0, 0]
        self.footPressureThreshold = [0, 0]
        self.bloodPressureThresholdSys = [0, 0]
        self.bloodPressureThresholdDia = [0, 0]

    # Sets vitals value whenever avaiable
    def set_vitals(self, dict={'heartRate': 60, 'footPressure': 75, 'bloodPressure': [120, 80]}):
        self.heartRate = dict['heartRate']
        self.footPressure = dict['footPressure']
        self.bloodPressure = dict['bloodPressure']

    def get_vitals(self):
        d = {'heartRate': self.heartRate, 'footPressure': self.footPressure, 'bloodPressure': self.bloodPressure}

        return d

    # Set thresholds for vital alert module
    def set_thresholds(self, heartRateThreshold=[40, 200], footPressureThreshold=[0, 200],
                       bloodPressureThresholdSys=[50, 200], bloodPressureThresholdDia=[50, 150]):
        self.heartRateThreshold = heartRateThreshold
        self.footPressureThreshold = footPressureThreshold
        self.bloodPressureThresholdSys = bloodPressureThresholdSys
        self.bloodPressureThresholdDia = bloodPressureThresholdDia

    def get_thresholds(self):
        d = {'heartRateThreshold': self.heartRateThreshold, 'footPressureThreshold': self.footPressureThreshold,
             'bloodPressureThresholdSys': self.bloodPressureThresholdSys,
             'bloodPressureThresholdDia': self.bloodPressureThresholdDia}

        return d

    # check if vitals exceeded threshold. This should be run in a thread by the processor
    def check_vitals(self):
        vitals = self.get_vitals()
        thresholds = self.get_thresholds()
        alerts = [['n', 0], ['n', 0], ['n', [0, 0]]]

        if vitals['heartRate'] > thresholds['heartRateThreshold'][1]:
            alerts[0] = ['h', vitals['heartRate']]
        elif vitals['heartRate'] < thresholds['heartRateThreshold'][0]:
            alerts[0] = ['l', vitals['heartRate']]
        else:
            alerts[0] = ['n', vitals['heartRate']]

        if vitals['footPressure'] > thresholds['footPressureThreshold'][1]:
            alerts[1] = ['h', vitals['footPressure']]
        elif vitals['footPressure'] < thresholds['footPressureThreshold'][0]:
            alerts[1] = ['l', vitals['footPressure']]
        else:
            alerts[1] = ['n', vitals['footPressure']]

        if (vitals['bloodPressure'][0] > thresholds['bloodPressureThresholdSys'][1] or
            vitals['bloodPressure'][1] > thresholds['bloodPressureThresholdDia'][1]):
            alerts[2] = ['h', vitals['bloodPressure']]
        elif (vitals['bloodPressure'][0] < thresholds['bloodPressureThresholdSys'][0] or
            vitals['bloodPressure'][1] < thresholds['bloodPressureThresholdDia'][0]):
            alerts[2] = ['l', vitals['bloodPressure']]
        else:
            alerts[2] = ['n', vitals['bloodPressure']]
            
        # This function updates the global variable of alerts.
        # There needs to be a global variable in the main function called current_alerts.
        update_alert_status(alerts);
        
        self.alert_user(alerts)