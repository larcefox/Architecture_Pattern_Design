# -*- coding: utf-8 -*-
from jinja2 import Template

template = Template(u'Jinja 2 Template <h1> Page title {{ title }}! </h1> {{ body }}')
# print(template.render(name=u'Вася'))

class Response(object):
    def __init__(self, code, body):
        self.code = code
        self.body = body


class Request:
    def __init__(self, data=None):
        self.data = data or {}


def main_view(request: Request, template) -> Response:
    body = request.data.get('client', None)
    title = 'MAIN'
    print(template.render(title=title, body=body))
    return Response('200 OK', [template.render(title=title, body=body).encode(encoding='utf8')])

def about_view(request: Request, template) -> Response:
    body = request.data.get('client', None)
    title = 'ABOUT'
    return Response('200 OK', [template.render(title=title, body=body).encode(encoding='utf8')])

def contacts_view(request: Request, template) -> Response:
    body = request.data.get('client', None)
    title = 'CONTACTS'
    return Response('200 OK', [template.render(title=title, body=body).encode(encoding='utf8')])

def view_404(request: Request, template):
    body = request.data.get('client', None)
    title = 'NOT FOUND'
    return Response('404 Not Found', [template.render(title=title, body=body).encode(encoding='utf8')])

def client_middleware(request, environ):
    request.data['client'] = environ['HTTP_USER_AGENT']

def slash_middleware(request, environ):
    request.data['client'] = environ['HTTP_USER_AGENT']


class Application(object):

    def __init__(self, urls, middlewares, template):
        self.urls = urls
        self.middlewares = middlewares
        self.template = template

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        :param template: шаблон jija2
        """

        url = environ['PATH_INFO']
        request = Request()

        for item in self.middlewares:
            item(request, environ)

        if url[-1] != '/':
            url = url + '/'

        if url in self.urls:
            view = self.urls[url]
            response = view(request, template)
        else:
            response = view_404(request, template)

        start_response(response.code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return response.body


urls = {
    '/': main_view,
    '/about/': about_view,
    '/contacts/': contacts_view
}

middlewares = [
    client_middleware,
    slash_middleware,
]

application = Application(urls, middlewares, template)