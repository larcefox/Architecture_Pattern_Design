# -*- coding: utf-8 -*-
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


class TemplateRender():
    def __call__(self, title, body):
        template = TemplateSelector(title)
        template = template()
        template = self.render(template, title, body)
        template = self.encode_text(template)
        template = self.wsgi_prepair(template)
        return template

    def encode_text(self, template):
        return template.encode(encoding='utf8')

    def render(self, template, title, body):
        return template.render(title=title, body=body)

    def wsgi_prepair(self, template):
        return [template]

class TemplateSelector():
        def __init__(self, title):
            self.title = title
            self.env = Environment()
            self.env.loader = FileSystemLoader('templates')
            self.templates = self.env.loader.list_templates()
            # print(self.templates)

        def __call__(self):
            for item in self.templates:
                if self.title in item.split('.')[0]:
                    template = self.env.get_template(item)
                    return template
            template = self.env.get_template('index.html')
            return template