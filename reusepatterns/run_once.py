#!/home/larce/.virtualenvs/APD/bin/python
# -*- coding: utf-8 -*-

class RunOnce(object):
    def __init__(self, function):
        self.function = function
        self.run = True
    def __call__(self, *args, **kwargs):
        if self.run:
            self.run = False
            self.function(*args, **kwargs)
