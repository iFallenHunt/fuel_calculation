import random
import os
from time import sleep

time = float(input('Enter the time spent on the trip: '))
velocity = float(input('Enter the average speed: '))
spent = float(input("Enter your vehicle's fuel consumption in KM/L: "))

distance = time * velocity
liters_used = distance / spent

print('Average speed: ', velocity, 'KM/h')
print('Time spent traveling: ', time, 'Hours')
print('Distance traveled: ', distance, 'KM')
print('Number of liters: ', round(liters_used,2), 'Liters')
