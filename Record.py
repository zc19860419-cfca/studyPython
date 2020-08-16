#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Record:
    date = ""
    name = ""
    count = 0
    price = 0.0

    def __init__(self, date, name, count, price):
        self.name = name
        self.date = date
        self.count = count
        self.price = price
