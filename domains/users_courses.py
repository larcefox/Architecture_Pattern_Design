# -*- coding: utf-8 -*-
import abc


class UsersCourses(abc.ABC):

    @abc.abstractmethod
    def add_course(self):
        pass

    @abc.abstractmethod
    def del_course(self):
        pass

    @abc.abstractmethod
    def show_user_courses(self):
        pass

    @abc.abstractmethod
    def show_not_user_courses(self):
        pass

    @abc.abstractmethod
    def update_courses(self):
        pass

    @abc.abstractmethod
    def update_users(self):
        pass

    @staticmethod
    def create(courses_journals, courses_journal):
        return courses_journals[courses_journal]()
from urllib.parse import unquote