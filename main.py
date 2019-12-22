from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from tools import music_play, log, DDingWarn
import events

# 测试代码
debug = False
events.debug_code(debug)

if __name__ == '__main__':
    # 程序启动初始化
    logger = log.logger
    events.starting_up()

    # 初始化任务调度器
    BlockScheduler = BlockingScheduler()
    BackScheduler = BackgroundScheduler()
    BackScheduler._logger = logger
    BlockScheduler._logger = logger
    logger.info('[ 石头派 ] 的 [ 任务调度器 ] 初始化完成')

    # 在调度器上增加
    events.schedules.add_block_schedule_jobs(BlockScheduler)
    events.schedules.add_back_schedule_jobs(BackScheduler)
    BackScheduler.start()
    BlockScheduler.start()

    # 从启动器启动任务
    events.events.initiator()
