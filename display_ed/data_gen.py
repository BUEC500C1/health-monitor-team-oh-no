import csv
import random
import time

x_value = 0
blood_pressure = 0
heart_rate = 0
oxy_concen = 0

fieldnames = ["x_value", "blood_pressure", "heart_rate", "oxy_concen"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "blood_pressure": blood_pressure,
            "heart_rate": heart_rate,
            "oxy_concen": oxy_concen
        }

        csv_writer.writerow(info)
        print(x_value, blood_pressure, heart_rate, oxy_concen)

        x_value += 1
        blood_pressure = random.randint(0, 200)
        heart_rate = random.randint(0, 200)
        oxy_concen = random.randint(0, 100)

    time.sleep(1)
