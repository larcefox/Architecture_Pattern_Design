# -*- coding: utf-8 -*-
import os
import configparser

# Загрузка файла конфигурации сервера
config = configparser.ConfigParser()
conf_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings', 'settings.cfg')
config.read(conf_path)
ANSWER_CODES = config['ANSWER_CODES']
body = {}

class Response(object):
    def __init__(self, code, text):
        self.code = code
        self.text = text

def main_view(request, template_render) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'INDEX'
    body['data'] = request.data.get('GET_DATA', None)
    return Response(ANSWER_CODES['200'], template_render(title, body))

def about_view(request, template_render) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'ABOUT'
    return Response(ANSWER_CODES['200'], template_render(title, body))

def contacts_view(request, template_render) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'CONTACTS'
    print(request.data.get('POST_DATA', None))
    print(request.data.get('GET_DATA', None))
    return Response(ANSWER_CODES['200'], template_render(title, body))

def not_found_view(request, template_render) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'NOT FOUND'
    return Response(ANSWER_CODES['404'], template_render(title, body))

