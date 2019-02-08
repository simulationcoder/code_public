# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:39:18 2018
Turn on and off VeSync plug using IFTTT depending on the battery percentage of the windows device
@author: Harpreet
"""

import psutil
import urllib.request
import time

def main():
    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged
    percent_integer = battery.percent
    if percent_integer<=20:
        urllib.request.urlopen("https://maker.ifttt.com/trigger/battery_low/with/key/craFL-nrm4QmsmP8AotPOz").read()
        print('Battery:{}%; Battery Low. Charging activated. Sleeping for the next 30 mins'.format(str(percent_integer)))
    elif percent_integer>=90:
        urllib.request.urlopen("https://maker.ifttt.com/trigger/battery_full/with/key/craFL-nrm4QmsmP8AotPOz").read()
        print('Battery:{}%; Charging de-activated. Sleeping for the next 30 mins'.format(str(percent_integer)))
    else:
        print('Battery:{}%; No action to take. Sleeping for the next 30 mins'.format(str(percent_integer)))

    time.sleep(1800)#sleep for 30 mins
    

while True:
    main()
