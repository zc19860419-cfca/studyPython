#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cost import Cost
from income import Income


def initialize_income():
    income_dict = {"2019-01-01#鲫鱼": Income("2019-01-01", "鲫鱼", 18, 10.5),
                   "2019-01-01#鲤鱼": Income("2019-01-01", "鲤鱼", 8, 6.2),
                   "2019-01-01#鲢鱼": Income("2019-01-01", "鲢鱼", 7, 4.7),
                   "2019-01-02#草鱼": Income("2019-01-02", "草鱼", 2, 7.2),
                   "2019-01-02#鲫鱼": Income("2019-01-02", "鲫鱼", 3, 12),
                   "2019-01-02#黑鱼": Income("2019-01-02", "黑鱼", 6, 15),
                   "2019-01-03#乌鱼": Income("2019-01-03", "乌鱼", 1, 71),
                   "2019-01-03#鲫鱼": Income("2019-01-03", "鲫鱼", 1, 9.8)}

    return income_dict


def initialize_cost(total_income):
    bait = 20
    eaten = 180
    depreciation_of_tools = 1
    tax_rate = 0.05
    return Cost(bait, eaten, depreciation_of_tools, tax_rate, total_income)


def calc_income(all_incomes):
    total_income = 0.0
    for each_income in all_incomes.values():
        total_income = total_income + (each_income.count * each_income.price)

    return total_income


def modify_incomes(all_incomes, key, change_field, value):
    want_to_update = all_incomes[key]
    if change_field == 'count':
        old = want_to_update.count
        want_to_update.count = old + value

    if change_field == 'price':
        old = want_to_update.price
        want_to_update.price = old * (1 + value)
    all_incomes[key] = want_to_update


def calc_net_profit(income, cost):
    return income - cost.total()


if __name__ == '__main__':
    incomes = initialize_income()
    print("initialize incomes:", incomes)
    income = calc_income(incomes)
    print("initialize income:", income)
    modify_incomes(incomes, "2019-01-01#鲫鱼", "count", -1)
    modify_incomes(incomes, "2019-01-02#黑鱼", "price", 0.1)
    print("after modify incomes:", incomes)
    income = calc_income(incomes)
    print("after modify income:", income)

    cost = initialize_cost(income)
    print("initialize cost:", cost)
    net_profit = calc_net_profit(income, cost)
    print("net_profit:", net_profit)
