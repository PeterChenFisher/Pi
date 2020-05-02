#!/usr/bin/env bash
# set up for pi running
sleep 5
# shellcheck disable=SC2164
cd /home/pi/Projects/Pi/
source /home/pi/Projects/Pi/venv/bin/activate
echo '开始执行每日经文脚本'
python3 assistant.py daily_scriputre &