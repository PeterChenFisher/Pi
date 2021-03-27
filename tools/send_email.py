#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import smtplib
from email.mime.text import MIMEText

from tools.log import logger
from tools.reply_template import *

mail_host = "smtp.163.com"  # 使用的邮箱的smtp服务器地址
mail_port = 465
mail_user = "peter_chenxiaofeng@163.com"  # 用户名（网易邮箱登录的用户名）
mail_pwd = "ETOTYJNRULYDJKJW"  # 密码（注意：此处密码为网易邮箱授权码）

server = None


def init_mail(init_times=0):
    global server

    if server is None:
        try:
            server = smtplib.SMTP_SSL(mail_host, mail_port)
            server.login(mail_user, mail_pwd)
            logger.info('邮箱登录成功')
        except Exception as e:
            logger.info(f'邮箱登录失败,等待网络连接 Exception: {e}')
            init_times += 1
            time.sleep(60)
            if init_times > 30:
                logger.info(f'已经进入内网，邮箱登录失败超过30次，无法登陆，请检查原因')
                return False
            init_mail(init_times)
            return False
    return True


def send_mail(aim_list, subject, content, accessory=False):
    if not server:
        init_mail()
    me = "PiServer" + "<" + mail_user + ">"
    # if accessory:
    #     msg
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(aim_list)  # 将收件人列表以‘;’分隔
    try:
        server.sendmail(me, aim_list, msg.as_string())
        logger.info(f'邮件成功发送！邮件主题:{subject}')
        return template(success=True)
    except Exception as e:
        return template(message=f'邮件 [{subject}]发送失败 Exception: {e}')


def close_server():
    global server
    if server is not None:
        try:
            server.close()
            server = None
            logger.info('邮箱登录已被关闭')
        except Exception as e:
            logger.warning(f'关闭邮箱失败，错误信息：{e}')
