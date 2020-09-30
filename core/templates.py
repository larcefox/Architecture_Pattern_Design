# -*- coding: utf-8 -*-
import os
from jinja2 import Template


def rendr(title, body):
    if title == 'CONTACTS':
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'templates','contacts.html'), mode='r', encoding='utf8') as f:
            template = Template(f.read())
            return [template.render(title=title, body=body).encode(encoding='utf8')]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'templates','index.html'), mode='r', encoding='utf8') as f:
            template = Template(f.read())
            return [template.render(title=title, body=body).encode(encoding='utf8')]