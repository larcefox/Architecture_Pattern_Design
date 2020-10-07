# -*- coding: utf-8 -*-
from core.templates import TemplateRender

class Request:
    def __init__(self, data=None):
        self.data = data or {}

class Application(object):

    def __init__(self, urls: dict, middlewares: list, templates_dict: dict):
        self.urls = urls
        self.middlewares = middlewares
        self.templates_dict = templates_dict

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """

        request = Request()
        template_render = TemplateRender(self.templates_dict)

        for item in self.middlewares:
            item(request, environ)

        url = request.data['PATH_INFO']
        view = ViewSelector()
        view = view(self.urls, url)
        response = view(request, template_render)
        start_response(response.code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return response.text


class ViewSelector():
        def __call__(self, urls, url):
            if url in urls:
                return urls[url]
            else:
                return urls['/not_found/']