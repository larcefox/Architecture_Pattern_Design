# -*- coding: utf-8 -*-
import os
import configparser
from core.templates import rendr

# Загрузка файла конфигурации сервера
config = configparser.ConfigParser()
conf_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings', 'settings.cfg')
config.read(conf_path)
ANSWER_CODES = config['ANSWER_CODES']

class Response(object):
    def __init__(self, code, text):
        self.code = code
        self.text = text

def main_view(request) -> Response:
    body = request.data.get('client', None)
    title = 'MAIN'
    return Response(ANSWER_CODES['200'], rendr(title, body))

def about_view(request) -> Response:
    body = request.data.get('client', None)
    title = 'ABOUT'
    return Response(ANSWER_CODES['200'], rendr(title, body))

def contacts_view(request) -> Response:
    body = request.data.get('client', None)
    title = 'CONTACTS'
    return Response(ANSWER_CODES['200'], rendr(title, body))

def not_found_view(request) -> Response:
    body = request.data.get('client', None)
    title = 'NOT FOUND'
    return Response(ANSWER_CODES['404'], rendr(title, body))

