#!/bin/sh
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus export DISPLAY=:0;

#Code:
#/usr/bin/notify-send "Test"
python /home/kev/flash-card/select_random_word.py
