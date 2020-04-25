import datetime
import time

import RPi.GPIO as GPIO

# from config import *


def get_pi_cpu_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    return temp


def fans_ctrl():
    '''
    功能：通过控制树莓派的13号IO口，控制树莓派风扇的转动和停止。
    在9:00am ~ 20:00pm时间段，树莓派风扇每次休息3min，转动5min，一直循环
    :return: void
    '''
    GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
    GPIO.setup(13, GPIO.OUT)  # 设置物理引脚13负责输出电压
    while 1:
        now = datetime.datetime.now()
        h = now.hour
        if 9 < h < 21:
            GPIO.output(13, GPIO.HIGH)  # 输出高电平
            time.sleep(60 * 5)
            GPIO.output(13, GPIO.LOW)  # 输出高电平
            time.sleep(60 * 1)
        elif get_pi_cpu_temp() >= 50:
            GPIO.output(13, GPIO.HIGH)
            time.sleep(60 * 5)


# def record_temp():
#     with open(raspi_temp_result_file, 'w+') as fo:
#         while True:
#             temp = get_pi_cpu_temp()
#             fo.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#             fo.write(str(temp))
#             fo.write('\n')
#             time.sleep(60)
#

if __name__ == '__main__':
    fans_ctrl()
