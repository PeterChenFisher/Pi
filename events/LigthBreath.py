import RPi.GPIO as GPIO  # 导入Rpi.GPIO库函数命名为GPIO

import time  # 导入计时time函数

GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
GPIO.setup(11, GPIO.OUT)  # 设置物理引脚11负责输出电压


def LightBreath(light_code):
    while True:
        GPIO.output(light_code, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(light_code, GPIO.LOW)
        time.sleep(1)


if __name__ == '__main__':
    LightBreath(11)
    GPIO.cleanup()  # 释放使用的GPIO引脚（程序到达最后都需要释放
