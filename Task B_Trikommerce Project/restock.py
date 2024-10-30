def restock_inventory(available_items, inventory_records, current_day):
    restock = 0                                          # sets 0 as the default restock number
    if current_day % 7 == 0 and available_items != 2000: # if the current day is divisible by 7 and the current stock not 2000
        restock = 2000 - available_items                 # finds amount needed for restock by subtracting the current stock by the maximum stock amount
    return restock                                       # return output of function
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
