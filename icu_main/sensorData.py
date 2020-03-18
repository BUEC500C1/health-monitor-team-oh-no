import random

def genNumbers():
    # Random float x, 60.0 <= x < 100.0
    heartRate = random.randint(60, 100)

    # Random float x, 75.0 <= x < 100.0
    footPressure = random.randint(75, 100)

    # Random float x, 100.0 <= x < 120.0
    bloodPressure = [random.randint(100, 120), random.randint(100, 120)]

    dict = {}
    dict['heartRate'] = heartRate
    dict['footPressure'] = footPressure
    dict['bloodPressure'] = bloodPressure

    return dict

# Test
if __name__ == '__main__':
    for i in range(5):
        d = genNumbers()
        print(d)