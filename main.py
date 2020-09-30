# -*- coding: utf-8 -*-
from core.engine import Application
import views


def client_middleware(request, environ):
    request.data['client'] = environ['HTTP_USER_AGENT']

def slash_middleware(request, environ):
    url = environ['PATH_INFO']
    if url[-1] != '/':
        url = url + '/'
    request.data['PATH_INFO'] = url

def data_middleware(request, environ):
    if environ['REQUEST_METHOD'] == 'GET':
        print('GET')
        query_string = environ['QUERY_STRING']
        request_params = parse_input_data(query_string)
        print(request_params)
    elif environ['REQUEST_METHOD'] == 'POST':
        print('POST')
        query_string = get_wsgi_input_data(environ).decode(encoding='utf-8')
        request_params = parse_input_data(query_string)
        print(request_params)
    else:
        print('REQUEST METHOD NOT SUPPORT')

def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result

def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data

urls = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contacts/': views.contacts_view,
    '/not_found/': views.not_found_view,
}

middlewares = [
    client_middleware,
    slash_middleware,
    data_middleware,
]

application = Application(urls, middlewares)