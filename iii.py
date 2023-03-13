#get list of order total prices and return a list
def list_of_orders_total_prices ():
    new_list_price = []
    get_list_price_String = input('''
list of orders total prices of the current week in AUD
format 100,33,744,...n
    ''')
    list_price = get_list_price_String.split(",")
    for x in list_price:
        new_list_price.append(float(x))
    return new_list_price
    

class Sale:

    total_price_curr_week = list_of_orders_total_prices ()
    total_price_pre_week = list_of_orders_total_prices ()

    def __init__(self):
        return
    
    def total_sale_for_current_week(self):
        a = 0
        for y in self.total_price_curr_week:
            a+= y
        return a

sale1 = Sale()

print(sale1.total_price_curr_week)
print(sale1.total_sale_for_current_week())
