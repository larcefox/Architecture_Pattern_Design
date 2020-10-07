# -*- coding: utf-8 -*-
from jinja2 import Template


class TemplateRender():
    def __init__(self, templates_dict):
        self.templates_dict = templates_dict

    def __call__(self, title, body):
        template_name = TemplateSelector(self.templates_dict, title)
        text = self.open_template(template_name())
        template = Template(text)
        template = self.render(template, title, body)
        template = self.encode_text(template)
        template = self.wsgi_prepair(template)
        return template

    def open_template(self, path):
        with open(path, mode='r', encoding='utf8') as f:
            return f.read()

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
        def __call__(self):
            if self.title in self.templates_dict:
                return self.templates_dict[self.title]
            else:
                return self.templates_dict['INDEX']