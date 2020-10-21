from domains.course import Course
from domains.user import User
from domains.users_courses import UsersCourses

'''
--------------------------COURCES--------------------------
'''

class Java(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.course_type = 'java'
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category.courses.append(self)
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type

class JavaScript(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.course_type = 'javascript'
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category.courses.append(self)
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type

class Python(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.course_type = 'python'
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category.courses.append(self)
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type

class Generic(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.course_type = 'generic'
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category.courses.append(self)
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self):
        return self.course_specialization
    def course_type(self):
        return self.course_type

'''
--------------------------USERS--------------------------
'''

class StandartUser(User):
    def __init__(self, user_login, user_password, user_level):
        self.user_type = 'standart_user'
        self.user_login = user_login
        self.user_password = user_password
        self.user_level = user_level
    def user_type(self):
        return self.user_type
    def user_password(self):
        return self.user_password
    def user_login(self):
        return self.user_login
    def user_level(self):
        return self.user_level

'''
--------------------------CATEGORY--------------------------
'''

class Category(object):

    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []
    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result