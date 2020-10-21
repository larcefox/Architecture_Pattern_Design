# -*- coding: utf-8 -*-
import abc


class User(abc.ABC):

    @abc.abstractmethod
    def user_login(self):
        pass

    @abc.abstractmethod
    def user_password(self):
        pass

    @abc.abstractmethod
    def user_level(self):
        pass

    @staticmethod
    def create(user_types, user_type, user_login, user_password, user_level):
        user_type = user_type if len(user_type) else 'standart_user'
        user_login = user_login if len(user_login) else 'Noob'
        user_password = user_password if len(user_password) else 'pass'
        user_level = user_level if len(user_level) else '1'
        return user_types[user_type](user_login, user_password, user_level)