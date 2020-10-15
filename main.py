# -*- coding: utf-8 -*-
from core.engine import Application
import views
import os


def client_middleware(request, environ):
    request.data['client'] = environ['HTTP_USER_AGENT']

def slash_middleware(request, environ):
    url = environ['PATH_INFO']
    if url[-1] != '/':
        url = url + '/'
    request.data['PATH_INFO'] = url

def data_middleware(request, environ):
    if environ['REQUEST_METHOD'] == 'GET':
        # filtr blanc GET requests
        if environ['QUERY_STRING']:
            query_string = environ['QUERY_STRING']
            request_params = parse_input_data(query_string)
            # making list of dicts for jinja2
            request.data['GET_DATA'] = []
            for key, value in request_params.items():
                request.data['GET_DATA'].append({key: value})
    elif environ['REQUEST_METHOD'] == 'POST':
        query_string = get_wsgi_input_data(environ).decode(encoding='utf-8')
        request_params = parse_input_data(query_string)
        request.data['POST_DATA'] = request_params
    else:
        print('REQUEST METHOD NOT SUPPORT :', environ['REQUEST_METHOD'])

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

def path_maker(*args):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *args)

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

# dict of templates with paths
# if page title equal dict key template will be applied
templates_dict = {
    'INDEX': 'index.html',
    'CONTACTS': 'contacts.html',
    'NOT FOUND': '404.html',
    'ABOUT': 'about.html',
}

application = Application(urls, middlewares, templates_dict)