import sqlite3
from domains.course import Course
from domains.observer import Observer, Subject
from domains.user import User
from reusepatterns.singletones import Singleton

"""
--------------------------COURCES--------------------------
"""


class Java(Course, Subject):
    course_list = []
    def __init__(
        self, course_specialization, course_duration, course_level, course_category
    ):
        super().__init__()
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = "Java"
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
        _ = (self.attach(obs) for obs in Observer.observers)
        self._subject_state = self.users
        __class__.course_list.append(self)

    def course_duration(self):
        return self.course_duration

    def course_level(self):
        return self.course_level

    def course_specialization(self):
        return self.course_specialization

    def course_type(self):
        return self.course_type

    def course_category_add(self):
        self.course_category.courses.append(self)

    def course_category_del(self):
        self.course_category.courses.remove(self)


class JavaScript(Course, Subject):
    course_list = []
    def __init__(
        self, course_specialization, course_duration, course_level, course_category
    ):
        super().__init__()
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = "JavaScript"
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
        _ = (self.attach(obs) for obs in Observer.observers)
        self._subject_state = self.users
        __class__.course_list.append(self)

    def course_duration(self):
        return self.course_duration

    def course_level(self):
        return self.course_level

    def course_specialization(self):
        return self.course_specialization

    def course_type(self):
        return self.course_type

    def course_category_add(self):
        self.course_category.courses.append(self)

    def course_category_del(self):
        self.course_category.courses.remove(self)


class Python(Course, Subject):
    course_list = []
    def __init__(
        self, course_specialization, course_duration, course_level, course_category
    ):
        super().__init__()
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = "Python"
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
        _ = (self.attach(obs) for obs in Observer.observers)
        self._subject_state = self.users
        __class__.course_list.append(self)

    def course_duration(self):
        return self.course_duration

    def course_level(self):
        return self.course_level

    def course_specialization(self):
        return self.course_specialization

    def course_type(self):
        return self.course_type

    def course_category_add(self):
        self.course_category.courses.append(self)

    def course_category_del(self):
        self.course_category.courses.remove(self)


class Generic(Course, Subject):
    course_list = []
    def __init__(
        self, course_specialization, course_duration, course_level, course_category
    ):
        super().__init__()
        self.id = Course.auto_id
        Course.auto_id += 1
        self.course_type = "Generic"
        self.users = []
        self.course_specialization = course_specialization
        self.course_duration = course_duration
        self.course_level = course_level
        self.course_category = course_category
        self.course_category_add()
        _ = (self.attach(obs) for obs in Observer.observers)
        self._subject_state = self.users
        __class__.course_list.append(self)

    def course_duration(self):
        return self.course_duration

    def course_level(self):
        return self.course_level

    def course_specialization(self):
        return self.course_specialization

    def course_type(self):
        return self.course_type

    def course_category_add(self):
        self.course_category.courses.append(self)

    def course_category_del(self):
        self.course_category.courses.remove(self)


"""
--------------------------USERS--------------------------
"""


class StandartUser(User):
    def __init__(self, user_login, user_password, user_level, user_category):
        self.id = User.auto_id
        User.auto_id += 1
        self.user_type = "standart_user"
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


"""
--------------------------CATEGORY--------------------------
"""


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


class CategoryLogger:
    categorys = {
        "standart_category": Category("standart_category", None),
    }

    def __call__(self, name: str, category=None) -> object:
        if name in __class__.categorys:
            return __class__.categorys[name]
        else:
            __class__.categorys[name] = Category(name, None)
            return __class__.categorys[name]


"""
--------------------------USER_CATEGORY--------------------------
"""


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


class UserCategoryLogger:
    categorys = {
        "teacher": UserCategory("standart_teacher", None),
        "student": UserCategory("standart_student", None),
    }

    def __call__(self, name: str, category=None) -> object:
        if name in __class__.categorys:
            return __class__.categorys[name]
        else:
            __class__.categorys[name] = UserCategory(name, None)
            return __class__.categorys[name]


"""
--------------------------OBSEVER--------------------------
"""


class SMS(Observer):
    def __init__():
        super().__init__()

    def update(self, users: list):
        for user in users:
            print(f"SMS to {user}")

"""
--------------------------DATA_MAPPER--------------------------
"""

class DataMapper(metaclass=Singleton):
    def __init__(self):
        # self.obj = obj
        self.conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()

    def obj_to_db(self, obj):
        # Create table

        columns = obj.__dict__.keys()
        values = [str(itm) for itm in obj.__dict__.values()]
        object_id = str(obj)
        columns = 'name, ' + ', '.join(columns)
        values = f'"{object_id}", "' + '", "'.join(values) + '"'
        class_name = obj.__class__.__name__

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS
                            { class_name }({ columns })
                                ''')
        self.cursor.execute(f'''INSERT INTO { class_name }({ columns }) VALUES ({ values })''')
        self.conn.commit()

    def repair_from_db(self, model_list: dict):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        data_storage = model_list["ds"]()
        for table in tables:
            table = (table[0])
            for course_class in model_list['course_types'].values():
                if table == course_class.__name__:
                    self.cursor.execute(f'SELECT name FROM {table}')
                    db_courses = self.cursor.fetchall()
                    for db_course in db_courses:
                        if db_course[0] in (str(course) for course in course_class.course_list):
                            print('in', db_course[0])
                        elif db_course[0] not in (str(course) for course in course_class.course_list):
                            print('not in', db_course[0])
                            self.cursor.execute(f'SELECT course_specialization, course_duration, course_level FROM {table} where name="{db_course[0]}"')
                            data = self.cursor.fetchall()[0]
                            print('data', data)
                            course = Course.create(model_list['course_types'], course_class.__name__, *data, model_list["select_category"]('repair'))
                            data_storage.save_course(course)
                            self.cursor.execute(f'DELETE FROM {table} WHERE name="{db_course[0]}"')

    def show(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            print(table[0])
            table = (table[0])
            self.cursor.execute(f'SELECT * FROM {table}')
            print(self.cursor.fetchall())


"""
--------------------------DATA_STORAGE--------------------------
"""


class DataStorage(metaclass=Singleton):
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