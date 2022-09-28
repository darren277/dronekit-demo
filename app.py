from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

import argparse

from settings import LAT, LON

parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

connection_string = args.connect

print(f'Connecting to vehicle on: {connection_string}')

vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(target_altitude):
    print('Arming motors')

    while not vehicle.is_armable:
        print('Waiting for arming...')
        time.sleep(1)

    vehicle.mode = VehicleMode('GUIDED')
    vehicle.armed = True

    print('Taking off!')
    vehicle.simple_takeoff(target_altitude)

    while True:
        print(f'Altitude: {vehicle.location.global_relative_frame.alt}')
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print('Reached target altitude')
            break
        time.sleep(1)

arm_and_takeoff(10)

vehicle.airspeed = 7

print("Go to wait point (wp1)")
wp1 = LocationGlobalRelative(LAT, LON, 10)

vehicle.simple_goto(wp1)

time.sleep(30)
...


print("Coming back")
vehicle.mode = VehicleMode('RTL')

time.sleep(30)

vehicle.close()

