# -*- coding: utf-8 -*-

import configparser
import os

from core.engine import Application
from domains.course import Course
from domains.user import User

# Загрузка файла конфигурации сервера
config = configparser.ConfigParser()
conf_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "settings", "settings.cfg"
)
config.read(conf_path)
ANSWER_CODES = config["ANSWER_CODES"]
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

    def get_course_by_id(self, id):
        for course in self.get_courses():
            if course.id == id:
                return course

    def get_user_by_id(self, id):
        for user in self.get_users():
            if user.id == id:
                return user


data_storage = Data_Storage()


def main_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "index"
    body["data"] = request.data.get("GET_DATA", None)
    return Response(ANSWER_CODES["200"], template_render(title, body))


def about_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "about"
    return Response(ANSWER_CODES["200"], template_render(title, body))


def contacts_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "contacts"
    print(request.data.get("POST_DATA", None))
    return Response(ANSWER_CODES["200"], template_render(title, body))


def not_found_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "404"
    return Response(ANSWER_CODES["404"], template_render(title, body))


def admin_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "admin"

    post_data = request.data.get("POST_DATA", None)
    get_data = request.data.get("GET_DATA", None)
    body["course_list"] = models_list["course_types"]
    body["course_category"] = models_list["categorys"]
    if post_data:

        if "course_category_add" in post_data:
            models_list["select_category"](name=post_data["course_category_add"])

        elif "course_type" in post_data:
            # Replace category name by object
            post_data["course_category"] = models_list["select_category"](
                post_data["course_category"]
            )
            # Create course
            course = Course.create(models_list["course_types"], **post_data)
            data_storage.save_course(course)

        elif "course_clone_id" in post_data:
            # Course clone error. Same hidden fild names, clone last element in list <li>.
            original_course_id = int(post_data["course_clone_id"])
            print("original_course_id ", original_course_id)
            for course in data_storage.get_courses():
                print(course.id)
            original_course = data_storage.get_course_by_id(original_course_id)
            clone_course = original_course.clone(original_course)
            print("original ", original_course, "copy ", clone_course)
            data_storage.save_course(clone_course)

        body["courses"] = data_storage.get_courses()

    return Response(ANSWER_CODES["200"], template_render(title, body))


def user_add_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "user_add"
    post_data = request.data.get("POST_DATA", None)
    get_data = request.data.get("GET_DATA", None)
    body["user_category"] = models_list["user_categorys"]
    if post_data:

        if "user_category_add" in post_data:
            models_list["select_user_category"](name=post_data["user_category_add"])

        elif "user_login" in post_data:
            # Replace category name by object
            post_data["user_category"] = models_list["select_user_category"](
                post_data["user_category"]
            )
            # Create course
            user = User.create(models_list["user_types"], **post_data)
            data_storage.save_user(user)

        elif "user_course_id" in post_data:
            print(
                f'user_course_id: { post_data["user_course_id"] }, get_course_by_id: { data_storage.get_course_by_id(int(post_data["user_course_id"])) }'
            )
            course = data_storage.get_course_by_id(int(post_data["user_course_id"]))
            print(
                f'user_id: { post_data["user_id"] }, get_user_by_id: { data_storage.get_user_by_id(int(post_data["user_id"])) }'
            )
            user = data_storage.get_user_by_id(int(post_data["user_id"]))
            course.users.append(user)
        body["users"] = data_storage.get_users()

    return Response(ANSWER_CODES["200"], template_render(title, body))


def course_edit_view(request, template_render, models_list) -> Response:
    body["client"] = request.data.get("client", None)
    # if page title equal dict key template will be applied
    title = "course_edit"
    post_data = request.data.get("POST_DATA", None)

    if post_data:
        if "cource_id" in post_data:

            edit_course = data_storage.get_course_by_id(int(post_data["cource_id"]))

            if (
                edit_course.course_specialization != post_data["course_specialization"]
                or edit_course.course_duration != post_data["course_duration"]
                or edit_course.course_level != post_data["course_level"]
            ):
                edit_course.course_specialization = post_data["course_specialization"]
                edit_course.course_duration = post_data["course_duration"]
                edit_course.course_level = post_data["course_level"]

            if edit_course.course_category != post_data["course_category"]:
                edit_course.course_category_del()
                edit_course_category = models_list["select_category"](
                    post_data["course_category"]
                )
                edit_course.course_category = edit_course_category
                edit_course.course_category_add()
                edit_course._notify()

    return Response(ANSWER_CODES["404"], template_render(title, body))
