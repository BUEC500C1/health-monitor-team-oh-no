# Use this file to send random predictions to the processor
# to be used for future actions by the user

import os
import random

def ai_thoughts(storage_data_file):
  # Function will return a list of 3 integers, in order of
  # heart rate, blood pressure, and oxygen level
  # 0 indicates low, 1 indicates normal, 2 indicates high

  vital_trend = []

  with open(storage_data_file, 'r') as file:
    ai_data = file.read()

    pulse_stat = random.randint(0,2)
    vital_trend.append(pulse_stat)

    pressure_stat = random.randint(0,2)
    vital_trend.append(pressure_stat)

    oxy_stat = random.randint(0,2)
    vital_trend.append(oxy_stat)

  return(vital_trend)

# if __name__ == '__main__':
#   print(ai_thoughts("requirements.txt"))

    