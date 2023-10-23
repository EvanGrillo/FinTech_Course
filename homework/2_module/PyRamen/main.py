import csv
import os

from Classes.Menu import Menu
from Classes.Report import Report

import pprint
pp = pprint.PrettyPrinter()

menu_path = os.path.relpath('Homework/2_module/PyRamen/Resources/menu_data.csv')
sales_path = os.path.relpath('Homework/2_module/PyRamen/Resources/sales_data.csv')

"""
    dicts
    keys are menu item names
    values are instances of Menu and Report class
"""
menu = {}
report = {}

with open(menu_path) as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        menu[row[0]] = Menu(row)

with open(sales_path) as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        
        #destructure list
        id, date, cc, qty, item = row
        
        qty = int(qty)
        
        #get menu item
        menu_item = menu[item]
        price = int(menu_item.price)
        cost = int(menu_item.cost)
        profit = price - cost
        
        if item not in report:
            report[item] = Report()

        report[item].count += qty
        report[item].revenue += price * qty
        report[item].cogs += cost * qty
        report[item].profit += profit * qty

for item in report:
    print(f"{item}: {vars(report[item])}")