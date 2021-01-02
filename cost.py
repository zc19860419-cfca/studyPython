#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Cost:
    def __init__(self, bait, eaten, depreciation_of_tools, tax_rate, total_income):
        self.__bait = bait
        self.__eaten = eaten
        self.__depreciation_of_tools = depreciation_of_tools
        self.__tax_rate = tax_rate
        self.__total_income = total_income

    @property
    def bait(self):
        return self.__bait

    @bait.setter
    def bait(self, bait):
        if not isinstance(bait, int):
            raise ValueError('bait must be a Integer')
        self.__bait = bait

    @property
    def eaten(self):
        return self.__eaten

    @eaten.setter
    def eaten(self, eaten):
        if not isinstance(eaten, int):
            raise ValueError('eaten must be a Integer')
        self.__eaten = eaten

    @property
    def tax_rate(self):
        return self.__tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        if not isinstance(tax_rate, float):
            raise ValueError('tax_rate must be a Float')
        self.__tax_rate = tax_rate

    @property
    def depreciation_of_tools(self):
        return self.__depreciation_of_tools

    @depreciation_of_tools.setter
    def bait(self, depreciation_of_tools):
        if not isinstance(depreciation_of_tools, int):
            raise ValueError('depreciation_of_tools must be a Integer')
        self.__depreciation_of_tools = depreciation_of_tools

    def total(self):
        return self.__eaten + self.__depreciation_of_tools + (self.__total_income * self.__tax_rate) + self.__bait
