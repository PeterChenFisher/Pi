#!/usr/bin/env bash
# set up for pi running
sleep 10
# shellcheck disable=SC2164
cd /home/pi/Projects/Pi/
source /home/pi/Projects/Pi/venv/bin/activate
echo '开始执行main.py 脚本'
python3 /home/pi/Projects/Pi/main.py 
