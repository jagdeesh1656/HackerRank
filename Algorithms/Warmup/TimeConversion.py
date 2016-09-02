#!/bin/python3

import sys


time = input().strip()
twentyFourHour = int(time[:-2].split(':')[0]) + 12
if time[-2:] == 'AM':
    if twentyFourHour == 24:
        twentyFourHour = '00'
    elif int(time[:-2].split(':')[0]) < 12:
        twentyFourHour = time[:-2].split(':')[0]
if time[-2:] == 'PM':
    if twentyFourHour == 24:
        twentyFourHour = '12'
        
remTime = str(twentyFourHour) + ':' + time[:-2].split(':')[1] + ':' + time[:-2].split(':')[2]
print (remTime)