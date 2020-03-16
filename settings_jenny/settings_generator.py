# Use this file to send random settings values to the
# processor for display
# Sent values: time interval (represents minutes, but sent as seconds)

import time
import random

def time_display_change():
  # Sends a pseudo-setting to diplay for 1, 5, and 10 minutes
  # resending a setting every 15 seconds

  time_rand = random.randint(0,2)
  if (time_rand > 0):
    time_setting = time_rand * 5
  else:
    time_setting = 1
  return(time_setting)

if __name__ == '__main__':
  while True:
    print(time_display_change())
    time.sleep(15)

