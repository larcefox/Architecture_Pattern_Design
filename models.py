from domains.course import Course
from domains.user import User

'''
--------------------------COURCES--------------------------
'''

class Java(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = 'java'
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type
    def course_category_add(self):
        self.course_category.courses.append(self)

class JavaScript(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = 'javascript'
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type
    def course_category_add(self):
        self.course_category.courses.append(self)

class Python(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = 'python'
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type
    def course_category_add(self):
        self.course_category.courses.append(self)

class Generic(Course):
    def __init__(self, course_specialization, course_duration, course_level, course_category):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = 'generic'
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
    def course_duration(self):
        return self.course_duration
    def course_level(self):
        return self.course_level
    def course_specialization(self, course_specialization):
        return self.course_specialization
    def course_type(self):
        return self.course_type
    def course_category_add(self):
        self.course_category.courses.append(self)

'''
--------------------------USERS--------------------------
'''

class StandartUser(User):
    def __init__(self, user_login, user_password, user_level, user_category):
        self.id = User.auto_id
        User.auto_id += 1
        self.user_type = 'standart_user'
        self.user_login = user_login
        self.user_password = user_password
        self.user_level = user_level
        self.user_category = user_category
        self.user_category_add()
    def user_type(self):
        return self.user_type
    def user_password(self):
        return self.user_password
    def user_login(self):
        return self.user_login
    def user_level(self):
        return self.user_level
    def user_category_add(self):
        self.user_category.users.append(self)

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

class CategoryLogger():
    categorys = {
            'standart_category': Category('standart_category', None),
        }
    def __call__(self, name: str, category=None) -> object:
        if name in __class__.categorys:
            return __class__.categorys[name]
        else:
            __class__.categorys[name] = Category(name, None)
            return __class__.categorys[name]

'''
--------------------------USER_CATEGORY--------------------------
'''

class UserCategory(object):

    auto_id = 0

    def __init__(self, name, category):
        self.id = UserCategory.auto_id
        UserCategory.auto_id += 1
        self.name = name
        self.category = category
        self.users = []
    def user_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.user_count()
        return result

class UserCategoryLogger():
    categorys = {
            'teacher': UserCategory('standart_teacher', None),
            'student': UserCategory('standart_student', None),
        }
    def __call__(self, name: str, category=None) -> object:
        if name in __class__.categorys:
            return __class__.categorys[name]
        else:
            __class__.categorys[name] = UserCategory(name, None)
            return __class__.categorys[name]

