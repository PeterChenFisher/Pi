#!/usr/bin/env bash
# set up for pi running
sleep 10
cd /home/pi/Projects/Pi/
source /home/pi/Projects/Pi/venv/bin/activate
echo '开始执行main.py 脚本'
python3 /home/pi/Projects/Pi/main.py &
echo '开始执行 树莓派风扇控制 脚本'
python3 /home/pi/Projects/Pi/events/FansCTR.py &
