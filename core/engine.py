# -*- coding: utf-8 -*-

class Request:
    def __init__(self, data=None):
        self.data = data or {}

class Application(object):

    def __init__(self, urls: dict, middlewares: list):
        self.urls = urls
        self.middlewares = middlewares

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """

        request = Request()

        for item in self.middlewares:
            item(request, environ)

        url = request.data['PATH_INFO']

        if url in self.urls:
            view = self.urls[url]
            response = view(request)
        else:
            view = self.urls['/not_found/']
            response = view(request)

        start_response(response.code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return response.text