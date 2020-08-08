# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from tools import log
import events
from config import *

if __name__ == '__main__':
    # 程序启动初始化
    logger = log.logger_generator(logger_name='PeterPi')
    mk_dirs([excluded_file, tts_location, time_report_tts_location])

    # 从启动器启动任务/进行初始化
    events.schedules.initiator()

    # 初始化任务调度器
    BlockScheduler = BlockingScheduler()
    BackScheduler = BackgroundScheduler()
    BackScheduler._logger = logger
    BlockScheduler._logger = logger
    logger.info(f'[ {logger.name} ] 的 [ 任务调度器 ] 初始化完成')

    # 在调度器上增加任务
    events.schedules.add_block_schedule_jobs(BlockScheduler)
    events.schedules.add_back_schedule_jobs(BackScheduler)
    # 获取所有的进程任务及时间安排，发送钉钉
    BackScheduler.start()
    BlockScheduler.start()
