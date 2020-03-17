import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
pressure_range=10
rate_range=10
concen_range=10

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,6))

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['blood_pressure']
    
    ax1.cla()
    ax1.set_ylim(0, 200)
    ax1.set_xlim(abs(x.size-pressure_range),x.size-1)

    ax1.set_title('Blood Pressure')
    ax1.set_ylabel('Blood Pressure (mm Hg)')
    ax1.set_xlabel('Time (s)')

    ax1.plot(x, y1, label='Blood Pressure')

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
    y3 = data['oxy_concen']

    ax3.cla()
    ax3.set_ylim(0, 100)
    ax3.set_xlim(abs(x.size-rate_range),x.size-1)

    ax3.set_title('Oxygen Concentration')
    ax3.set_ylabel('Oxygen Concentration (%)')
    ax3.set_xlabel('Time (s)')

    ax3.plot(x, y3, label='oxy_concen')

ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
