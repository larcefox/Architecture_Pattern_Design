# -*- coding: utf-8 -*-
import os
import configparser
from domains.course import Course
from domains.user import User

# Загрузка файла конфигурации сервера
config = configparser.ConfigParser()
conf_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings', 'settings.cfg')
config.read(conf_path)
ANSWER_CODES = config['ANSWER_CODES']
body = {}

class Response(object):
    def __init__(self, code, text):
        self.code = code
        self.text = text

class Data_Storage:
    def __init__(self):
        self.courses = []
        self.users = []

    def save_course(self, course):
        self.courses.append(course)

    def save_user(self, user):
        self.users.append(user)

    def get_courses(self):
        return self.courses or []

    def get_users(self):
        return self.users or []


data_storage = Data_Storage()


def main_view(request, template_render, models) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'INDEX'
    body['data'] = request.data.get('GET_DATA', None)
    return Response(ANSWER_CODES['200'], template_render(title, body))

def about_view(request, template_render, models) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'ABOUT'
    return Response(ANSWER_CODES['200'], template_render(title, body))

def contacts_view(request, template_render, models) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'CONTACTS'
    print(request.data.get('POST_DATA', None))
    return Response(ANSWER_CODES['200'], template_render(title, body))

def not_found_view(request, template_render, models) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'NOT FOUND'
    return Response(ANSWER_CODES['404'], template_render(title, body))

def admin_view(request, template_render, models_list) -> Response:
    body['client'] = request.data.get('client', None)
    # if page title equal dict key template will be applied
    title = 'ADMIN'

    post_data = request.data.get('POST_DATA', None)
    get_data = request.data.get('GET_DATA', None)
    body['course_list'] = models_list[0]
    body['course_category'] = models_list[3]
    if post_data:

        if 'course_category_add' in post_data:
            models_list[2](post_data['course_category_add'])

        elif 'course_type' in post_data:
            # Replace category name by object
            post_data['course_category'] = models_list[2](post_data['course_category'])
            # Create course
            course = Course.create(models_list[0], **post_data)

            data_storage.save_course(course)
            body['courses'] = data_storage.get_courses()

    return Response(ANSWER_CODES['200'], template_render(title, body))