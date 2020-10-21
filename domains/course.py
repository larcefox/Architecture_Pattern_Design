# -*- coding: utf-8 -*-
import abc


class Course(abc.ABC):

    @abc.abstractmethod
    def course_duration(self):
        pass

    @abc.abstractmethod
    def course_level(self):
        pass

    @abc.abstractmethod
    def course_specialization(self):
        pass

    @staticmethod
    def create(course_types, course_type, course_specialization, course_duration, course_level, course_category, **kwargs):
        course_type = course_type if len(course_type) else 'generic'
        course_specialization = course_specialization if len(course_specialization) else 'IT'
        course_duration = course_duration if len(course_duration) else '5'
        course_level = course_level if len(course_level) else '1'
        category = None
        return course_types[course_type](course_specialization, course_duration, course_level, course_category)
