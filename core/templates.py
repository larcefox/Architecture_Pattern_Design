# -*- coding: utf-8 -*-
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


class TemplateRender():
    def __init__(self, templates_dict):
        self.templates_dict = templates_dict

    def __call__(self, title, body):
        template = TemplateSelector(self.templates_dict, title)
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
        def __init__(self, templates_dict, title):
            self.templates_dict = templates_dict
            self.title = title
            self.env = Environment()
            self.env.loader = FileSystemLoader('templates')

        def __call__(self):
            if self.title in self.templates_dict:
                template = self.env.get_template(self.templates_dict[self.title])
                return template
            else:
                template = self.env.get_template(self.templates_dict['INDEX'])
                return template
