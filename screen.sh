#!/bin/bash

ExtraScreen='HDMI-A-0'
PrimaryScreen='eDP'

if xrandr --query | grep "$ExtraScreen connected"
then
    xrandr \
        --output $ExtraScreen --mode 1920x1080 --left-of $PrimaryScreen --primary \
        --output $PrimaryScreen --mode 1920x1080 --pos 0x0 --rotate normal &
    /home/martin/Doot.sh
else
    xrandr \
        --output $ExtraScreen --off \
        --output $PrimaryScreen --mode 1920x1080 --pos 0x0 --rotate normal &
fi
