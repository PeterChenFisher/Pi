#!/usr/bin/env bash
# set up for pi running
sleep 10
cd /home/pi/Projects/Pi/
source /home/pi/Projects/Pi/venv/bin/activate
python3 /home/pi/Projects/Pi/main.py &
python3 /home/pi/Projects/Pi/events/FansCTR.py &
