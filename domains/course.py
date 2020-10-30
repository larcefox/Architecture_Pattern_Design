# -*- coding: utf-8 -*-
import abc
import copy


class Course(abc.ABC):

    auto_id = 0

    @abc.abstractmethod
    def course_duration(self):
        pass

    @abc.abstractmethod
    def course_level(self):
        pass

    @abc.abstractmethod
    def course_specialization(self):
        pass

    @abc.abstractmethod
    def course_type(self):
        pass

    @abc.abstractmethod
    def course_category_add(self):
        pass

    @staticmethod
    def create(course_types, course_type, course_specialization, course_duration, course_level, course_category, **kwargs):
        course_type = course_type if len(course_type) else 'generic'
        course_specialization = course_specialization if len(course_specialization) else 'IT'
        course_duration = course_duration if len(course_duration) else '5'
        course_level = course_level if len(course_level) else '1'
        category = None
        return course_types[course_type](course_specialization, course_duration, course_level, course_category)

    @staticmethod
    def clone(course_object):
        clone_course = copy.copy(course_object)
        clone_course.id = Course.auto_id
        Course.auto_id += 1
        clone_course.parent_id = course_object.id
        clone_course.course_category_add()
        print(course_object.course_type, clone_course.course_type)
        return clone_course