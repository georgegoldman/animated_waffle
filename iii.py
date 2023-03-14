#get list of order total prices and return a list
def list_of_orders_total_prices (message):
    new_list_price = []
    print("Exit program with CTRL+Z\neg format 100,33,744,...n: ")
    get_list_price_String = input(f"The list of orders total prices of the {message} week in AUD ")
    list_price = get_list_price_String.split(",")
    for x in list_price:
        new_list_price.append(float(x))
    return new_list_price
    

class Sale:

    total_sales_price_curr_week = list_of_orders_total_prices ("current")
    total_sales_price_pre_week = list_of_orders_total_prices ("previous")
    tota_number_of_person_visited_curr = int(input("Total number of persons visited in the Current Week: "))
    tota_number_of_person_visited_pre = int(input("Total number of persons visited in the Last Week: "))

    def __init__(self):
        return
    
    def get_total_sale(self,total_sales):
        a = 0
        for y in total_sales:
            a+= y
        return a
    
    def current_Week_per_person_average_sale(self):
        print(f"Current Week per person average sale= {self.get_total_sale(self.total_sales_price_curr_week)/self.tota_number_of_person_visited_curr}")
    
    def previous_Week_per_person_average_sale(self):
        print(f"Last Week per person average sale= {self.get_total_sale(self.total_sales_price_pre_week)/self.tota_number_of_person_visited_pre}")

sale1 = Sale()
sale1.current_Week_per_person_average_sale()
sale1.previous_Week_per_person_average_sale()
# print(sale1.get_total_sale(sale1.total_sales_price_pre_week))
