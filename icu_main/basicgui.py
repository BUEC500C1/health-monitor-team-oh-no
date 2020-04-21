import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

import csv

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [str(row_index), row[0], row[1], row[2]]
                data.append(columns)
    return data

def display_result(time_setting):
    plt.style.use('fivethirtyeight')
    x_vals = []
    y_vals = []

    index = count()
    data = pd.read_csv('data.csv')
    
    val = time_setting
    
    pressure_range = val
    rate_range =  val
    concen_range = val
    
    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,6))
    def animate(i):
        data = pd.read_csv('data.csv')
        
        x = data['x_value']
        y1a = data['blood_pressure']
        y1b = data['blood_pressureb']
        
        ax1.cla()
        ax1.set_ylim(0, 200)
        ax1.set_xlim(abs(x.size-pressure_range),x.size-1)

        ax1.set_title('Blood Pressure')
        ax1.set_ylabel('Blood Pressure (mm Hg)')
        ax1.set_xlabel('Time (s)')

        ax1.plot(x, y1a, label='Blood Pressure')
        ax1.plot(x, y1b, label='Blood Pressure')


        data = pd.read_csv('data.csv')
        x = data['x_value']
        y2 = data['heart_rate']
        
        ax2.cla()
        ax2.set_ylim(0, 200)
        ax2.set_xlim(abs(x.size-rate_range),x.size-1)

        ax2.set_title('Heart Rate')
        ax2.set_ylabel('Heart Rate (beats/min)')
        ax2.set_xlabel('Time (s)')

        ax2.plot(x, y2, label='Heart Rate')

        data = pd.read_csv('data.csv')
        x = data['x_value']
        y3 = data['footPressure']

        ax3.cla()
        ax3.set_ylim(0, 200)
        ax3.set_xlim(abs(x.size-rate_range),x.size-1)

        ax3.set_title('Foot Pressure')
        ax3.set_ylabel('Foot Pressure')
        ax3.set_xlabel('Time (s)')
        
        ax3.plot(x, y3, label='oxy_concen')
        
    ani = FuncAnimation(fig, animate, interval=1000)
    plt.show()
    
