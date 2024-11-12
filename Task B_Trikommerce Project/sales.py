import random

def daily_sales(available_items, inventory_records, current_day):
    if current_day % 7 != 0:                                            # if the current day is not divisible by 7 it is a sales day
        sales = random.randint(0,200)                                   # use a random number to simulate the sales
        available_items = available_items-sales                         # The daily sales are subtracted from the stock
        inventory_records += [[current_day, sales, 0, available_items]] # inventory records are updated
    return available_items                                              # return available items as integers