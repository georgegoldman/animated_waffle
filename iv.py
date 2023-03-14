def cin(message):
    try:
        return int(input(message))
    except:
        print("oops! only numbers allowed")
        exit()
    
def cin_percent(message):
    try:
        value = input(message)
        if "%" in value:
            remove_last_char = value[:-1]
            rm_val_to_num = int(remove_last_char)
            if rm_val_to_num > 0 and rm_val_to_num < 100:
                return rm_val_to_num
            else:
                print("Invalid percent range")
                exit()
        else:
            print("'%' sign required")
            exit()
    except:
        print("please enter numbers alone")
        exit()
    

class Bill:
    print("Sample Input:")
    total_invoice_amount = cin("Total Invoice amount (In Dollars):\t\t\t")
    amount_of_tip = cin("Amount of Tip (In Cents):\t\t\t")
    total_payment_by_card = cin("Total Payment received by Card:\t\t\t")
    service_charge_on_card = cin_percent("Service Charge on Payment made by Card:\t\t\t")
    total_cash_payment = cin("Total Payment received in Cash (In Dollars):\t\t\t")

    def __init__(self) -> None:
        pass

    def __service_charge_for_card(self):
        return self.total_payment_by_card * (self.service_charge_on_card/100)
    
    def __tips_in_dollar(self):
        return self.amount_of_tip * 0.0011
    
    def __total_expenses(self):
        return self.total_invoice_amount + self.__service_charge_for_card()

    def __total_payment(self):
        return self.__tips_in_dollar() + self.total_cash_payment + self.total_payment_by_card

    def customer_balance(self):
        total_customer_balance = self.__total_payment() - self.__total_expenses()
        if total_customer_balance < 0:
            print(f"Outstanding amount and need to be paid by customer: {-1 * total_customer_balance}")
        print(f"Change to be returned to the customer (In Dollars):\t\t{total_customer_balance}")

bill_x = Bill()
bill_x.customer_balance()