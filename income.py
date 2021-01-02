#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Income:
    def __init__(self, date, name, count, price):
        self.__date = date
        self.__name = name
        self.__count = count
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('name must be a String')
        self.__name = name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError('date must be a String')
        self.__date = date

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if not isinstance(count, int):
            raise ValueError('count must be a Integer')
        self.__count = count

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise ValueError('price must be a float')
        self.__price = price
