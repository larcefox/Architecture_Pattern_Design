# -*- coding: utf-8 -*-
from core.templates import TemplateRender
from reusepatterns.singletones import Singleton

class Request:
    def __init__(self, data=None):
        self.data = data or {}

class Application():
    _instance = None

    def __init__(self, urls: dict, middlewares: list, models_list: dict):
        self.urls = urls
        self.middlewares = middlewares
        self.models_list = models_list
        __class__._instance = self

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """

        request = Request()
        template_render = TemplateRender()

        for item in self.middlewares:
            item(request, environ)

        url = request.data['PATH_INFO']
        view = ViewSelector()
        view = view(self.urls, url)
        response = view(request, template_render, self.models_list)
        start_response(response.code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return response.text

    def add_route(self, url):
        # паттерн декоратор
        def inner(view):
            self.urls[url] = view
        return inner

class ViewSelector():
        def __call__(self, urls, url):
            if url in urls:
                return urls[url]
            else:
                return urls['/not_found/']