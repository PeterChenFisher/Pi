import RPi.GPIO as GPIO
import time
import datetime


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
        while 9 < h < 21:
            GPIO.output(13, GPIO.HIGH)  # 输出高电平
            print('HIGH')
            time.sleep(60*3)
            GPIO.output(13, GPIO.LOW)  # 输出高电平
            print('LOW')
            time.sleep(60*5)
        time.sleep(30)


if __name__ == '__main__':
    fans_ctrl()
