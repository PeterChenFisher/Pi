import RPi.GPIO as GPIO  # 导入Rpi.GPIO库函数命名为GPIO

import time  # 导入计时time函数

GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
GPIO.setup(11, GPIO.OUT)  # 设置物理引脚11负责输出电压


def LightBreath(light_code):
    while True:  # 条件符合，执行以下程序循环
        GPIO.output(light_code, GPIO.HIGH)  # 输出高电平
        time.sleep(1)  # 计时0.5秒
        GPIO.output(light_code, GPIO.LOW)  # 引脚输出低电平
        time.sleep(1)  # 计时1秒


if __name__ == '__main__':
    LightBreath(11)
    GPIO.cleanup()  # 释放使用的GPIO引脚（程序到达最后都需要释放
