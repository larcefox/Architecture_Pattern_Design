# -*- coding: utf-8 -*-
from core.engine import Application
import views
import os
import models
from pprint import pprint
from logging_mod import Logger, debug
from reusepatterns.run_once import RunOnce

logger = Logger('main')

def client_middleware(request, environ):
    request.data['client'] = environ['HTTP_USER_AGENT']

@RunOnce
def collect_urls_middleware(request, environ):
    print('--------------------------------------------------------------------------------------')
    for module in dir(views):
        if 'view' in module:
            try:
                exec(f'views.{module}()')
            except Exception as e:
                pass
    print('--------------------------------------------------------------------------------------')

def slash_middleware(request, environ):
    url = environ['PATH_INFO']
    if url[-1] != '/':
        url = url + '/'
    request.data['PATH_INFO'] = url

def staic_path(request, environ):
    url = environ['PATH_INFO']
    for itm in urls:
        if itm in url and 'css' in url and url != '/':
            url.replace(itm, "/")


@debug
def data_middleware(request, environ):
    if environ['REQUEST_METHOD'] == 'GET':
        # filtr blanc GET requests
        if environ['QUERY_STRING']:
            query_string = environ['QUERY_STRING']
            request_params = parse_input_data(query_string)
            request.data['GET_DATA'] = request_params

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
    '/admin/': views.admin_view,
}
setattr(models.UrlDecoratorStage2, "urls", urls)

middlewares = [
    client_middleware,
    slash_middleware,
    data_middleware,
    staic_path,
    collect_urls_middleware,
]

# Course types dict
course_types = {
    'generic': models.Generic,
    'java': models.Java,
    'javascript': models.JavaScript,
    'python': models.Python,
}

# User types dict
user_types = {
    'standart_user': models.StandartUser,
}

# Create logger proxy object for category
proxy_category = models.ProxyCategory()

models_list = {
    'course_types': course_types,
    'user_types': user_types,
    'select_category': proxy_category.select_category,
    'categorys': proxy_category.categorys,
}

application = Application(models.UrlDecoratorStage2.urls, middlewares, models_list)