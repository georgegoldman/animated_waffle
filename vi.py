print("Ctrl+z to exit app")

def cin_int(message):
    try:
        return int(input(message))
    except:
        print("please enter numbers only")

class OrderCharges:
    order_charges = {
        1: ["dine in", 8],
        2: ["pick up", 0],
        3: ["delivery", 10]
    }
    enter_order = cin_int("Insert the order base cost in AUD:\t")
    enter_order_type = cin_int("enter order type eg 1- dine in, 2-pick up, 3-deivery:\t")
    def __init__(self) -> None:
        pass

    def calculate_charge(self):
        print(self.enter_order + (self.enter_order * (self.order_charges[self.enter_order_type][1]*0.01)))



orderCharges_x = OrderCharges()
orderCharges_x.calculate_charge()