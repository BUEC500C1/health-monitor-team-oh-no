'''
This module accepts a timestamp and up to 3 sensor input arguments

Parses the input into a CSV file up to length N
'''

from os.path import isfile, isdir, join, dirname
from os import mkdir
from itertools import islice  # Remove the first
from shutil import rmtree
import csv

class sensorDataSaver():
    def __init__(self, outputfilename='output/healthmonitor.csv'):
        '''
        This function creates the output folder if it does not exist, or deletes and

        Creates an output csv file with the proper headers and waits for data to fill

        Puts latest data at the end of the spreadsheet
        '''
        self.N = 100  # Max length of CSV file
        filedir = dirname(outputfilename)
        if isdir(filedir):
            rmtree(filedir)
        mkdir(filedir)
        with open(outputfilename, 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["DateTime", "HeartRate", "bloodPressure", "OxygenLevel"])
        self.linenumber = 0
        self.outputfilename = outputfilename
    def removefirstrows(self):
        '''
        This function detects if the csv file is getting too large

        Stores the old file in a buffer, then rewrites the file line by line
        '''
        if self.linenumber <= 100: 
            return
        with open(self.outputfilename, 'r') as oldfid:
            fileinfo = oldfid.readlines()
        L = len(fileinfo)
        with open(self.outputfilename, 'w') as newfid:
            newfid.write(fileinfo[0]) # Write the header
            for i in range((L-100), L): # Write the last 100 lines of the file
                newfid.write(fileinfo[i])
        self.linenumber = 100

    def appendrow(self, timestamp, heartRate='', bloodPressure='', oxygenLevel=''):
        '''
        This function returns the 
        '''
        with open(self.outputfilename, 'a', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow([timestamp, heartRate, bloodPressure, oxygenLevel])
            self.linenumber += 1
        self.removefirstrows()


if __name__ == '__main__':
    print('Hello world')
    dataSaver = sensorDataSaver()  # Instantiate the class to generate the input and output directories
    dataSaver.appendrow('1234', '60', '120/60', '50%')
    for i in range(200):
        dataSaver.appendrow(i, '60', '120/60', '50%')


