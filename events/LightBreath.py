from config import *
import time  # 导入计时time函数

if os_platform == 'linux' or os_platform == 'Linux':
    import RPi.GPIO as GPIO  # 导入Rpi.GPIO库函数命名为GPIO

    GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
    GPIO.setup(11, GPIO.OUT)  # 设置物理引脚11负责输出电压


    def LightBreath(light_code):
        while True:
            time.sleep(1)
            GPIO.output(light_code, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(light_code, GPIO.LOW)

if __name__ == '__main__':
    LightBreath(11)
    GPIO.cleanup()  # 释放使用的GPIO引脚（程序到达最后都需要释放
