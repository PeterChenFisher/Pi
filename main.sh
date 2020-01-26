#!/usr/bin/env bash
# set up for pi running
sleep 10
cd /home/pi/Projects/Pi/
git pull gitee master >> ./excluded/gitpull-results.txt
source /home/pi/Projects/Pi/venv/bin/activate
python3 /home/pi/Projects/Pi/main.py &
