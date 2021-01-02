#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Test:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('name must be a String')
        self.__name = name


test = Test('zc')
print("test.name=", test.name)
