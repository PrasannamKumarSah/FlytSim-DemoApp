import time
import argparse
from flyt_python import api

drone = api.navigation(timeout=120000)
time.sleep(3)

parser = argparse.ArgumentParser()
parser.add_argument('side', metavar='a', type=float)
parser.add_argument('height',metavar='b', type=float)
args = parser.parse_args()

a = args.side
print 'Side of square : ',a
h = args.height
print 'Height of drone : ',h

print "Takking Off"
print "Taking Off at start of Square"
drone.take_off(h)

print "Going to point 1"
drone.position_set_global(37.4196, -122.0782,0, yaw=0.0, tolerance=0.0, async=False, yaw_valid=True)

print "At point 1 going to point 2"
drone.position_set(a,0,-h,relative=True, yaw_valid=True, tolerance=0.0, yaw=0.0)

print "At point 2 going to point 3"
drone.position_set(0,a,0,relative=True, yaw_valid=True, tolerance=0.0, yaw=1.6)

print "At point 3 going to point 4"
drone.position_set(-a,0,0,relative=True, yaw_valid=True, tolerance=0.0, yaw=1.6)

print "At point 4 going to point 1"
drone.position_set(0,-a,0,relative=True, yaw_valid=True, tolerance=0.0, yaw=1.6)

print "Landing..."
drone.land(async=False)

print "Task Completed"

drone.disarm()
print "Disarmed"

drone.disconnect()
print "Disconnected"