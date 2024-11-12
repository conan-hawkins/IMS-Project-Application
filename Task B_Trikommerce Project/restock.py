def restock_inventory(available_items, inventory_records, current_day):
    restock = 2000                                                           # sets 0 as the default restock number
    if current_day == 0:
        inventory_records += [[current_day, 0, restock, available_items]]

    elif current_day % 7 == 0:                                                # if the current day is divisible by 7 and the current stock not 2000
        restock = 2000-available_items                                      # finds amount needed for restock by subtracting the current stock by the maximum stock amount
        available_items = available_items+restock                           # availible items are the 
        inventory_records += [[current_day, 0, restock, available_items]]   # inventory records are updated
    return available_items                                                  # return available items as integer 