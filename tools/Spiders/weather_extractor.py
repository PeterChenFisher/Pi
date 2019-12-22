import time
import requests
from tools.reply_template import *
from tools.log import logger
from bs4 import BeautifulSoup

weather_url = 'https://tianqi.moji.com/weather/china/guangdong/shantou'
request_time = 0
weather_infos = {
    '空气质量': None,
    '天气预警': None,

}


def get_weather():
    global request_time
    try:
        response = requests.request(method='GET', url=weather_url, timeout=30)
    except Exception as e:
        time.sleep(10)
        request_time += 1
        if request_time == 10:
            return template(message='Requested Over 10 Times.')
        logger.info(
            'Request UrlPage Failed. We will Request Again. Request Time:%s. Error Message:%s' % (request_time, e))
        result = get_weather()
        return result
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        weather_description = soup.head.find('meta', attrs={'name': 'description'})['content']
        logger.info(weather_description)
        return template(success=True, data=weather_description)
        # weather_info = soup.body.find('div', class_='wrap clearfix wea_info').find('div', class_='left')
    except Exception as e:
        logger.info('Get Weather Info Failed.Please Check The Url Page Style.', e)
        return template(message='Get Weather Info Failed.Please Check The Url Page Style. Error Message:' + str(e))
    # print(weather_info)
    # if not wea_alert(weather_info) or not wea_content(weather_info) or not wea_about(weather_info) or not wea_tips(
    #         weather_info):
    #     print('Get Weather Info Failed.Please Check The Url Page Style.')


def wea_alert(weather_info):
    return True


def wea_content(weather_info):
    return True


def wea_tips(weather_info):
    return True


def wea_about(weather_info):
    return True


if __name__ == '__main__':
    result = get_weather()
    print(result[key_data])
