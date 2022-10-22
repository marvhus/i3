#!/usr/bin/python3

import os
import sys

def clamp(num, min_num, max_num):
    return max(min(num, max_num), min_num)

path = "~/.config/i3/brightness-last" 

# Get existing brightness
brightness = os.popen(f'cat {path}').read()
if len(brightness) <= 0:
    brightness = '1.0'
try:
    brightness = float(brightness)
except:
    exit(1)
print('existing', brightness)

# Get args
args = sys.argv
change = 0
if len(args) >= 2:
    try:
        change = float(args[1])
    except:
        exit(1)
else:
    print(args, len(args))
print('change', change)

# Get new brightness
new = clamp((brightness + change), 0, 1)
print('new', new)

# Save new brightness
os.system(f'echo {new} > {path}')

# Get screens
screens = os.popen("xrandr -q | grep ' connected' | cut -d ' ' -f1").read()
screens = screens.split()
print('screens', screens)

# Set brightness for all screens
for screen in screens:
    os.system(f'xrandr --output {screen} --brightness {new}')

