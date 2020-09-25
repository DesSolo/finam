import re
import logging
from datetime import datetime
import requests


def get_current_data():
    return datetime.today().strftime('%d.%m.%Y')


class ExportFinam:
    url = 'http://export.finam.ru'

    def __init__(self, user_agent):
        self.session = requests.Session()
        self.session.headers = requests.sessions.cookiejar_from_dict({'User-Agent': user_agent})

    def raw(self, method, uri, params=None, data=None):
        logging.debug('raw request method: "%s" uri: "%s" params: "%s" data: "%s"', method, uri, params, data)
        return self.session.request(method, self.url + uri, params=params, data=data)

    # https://www.finam.ru/profile/moex-akcii/mosenrg/export/
    def export(self, em, name, date_from=None, date_to=None):
        logging.debug('call export em: "%s" name: "%s"', em, name)
        if not date_from:
            date_from = get_current_data()
        if not date_to:
            date_to = get_current_data()
        day_from, mouth_from, year_from = map(int, date_from.split('.'))
        day_to, mouth_to, year_to = map(int, date_to.split('.'))
        params = {
            'market': '1',
            'em': em,
            'apply': '0',
            'df': day_from,
            'mf': mouth_from - 1,
            'yf': year_from,
            'from': date_from,
            'dt': day_to,
            'mt': mouth_to - 1,
            'yt': year_to,
            'to': date_to,
            'p': '2',
            'e': '.csv',
            'cn': name,
            'dtf': '1',
            'tmf': '3',
            'MSOR': '1',
            'mstime': 'on',
            'mstimever': '1',
            'sep': '1',
            'sep2': '1',
            'datf': '4',
            'at': '1'
        }
        response = self.raw('GET', '/export9.out', params=params)
        logging.debug('response code: %d headers: "%s"', response.status_code, response.headers)
        data = response.text.replace('\r', '').split('\n')
        header = re.sub('[<>]', '', data[0]).lower().split(',')
        for line in data[1:]:
            if not line:
                logging.debug('line is empty')
                continue
            item = {}
            for key, value in zip(header, line.split(',')):
                item[key] = value
            logging.debug('line: "%s"', item)
            yield item
