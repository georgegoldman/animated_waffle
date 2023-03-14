def cin_int (message):
    try:
        d = int(input(message))
        return d
    except:
        print("numbers only")

class Order:
    address = input("full address: ")
    distance = cin_int("Distance between in Kilometre: ")

    def __init__(self) -> None:
        pass

    def delivery_charge(self):
        if self.distance > 0 and self.distance <= 5:
            print("$5")
        elif self.distance > 5 and self.distance <= 10:
            print("$8")
        elif self.distance > 10 and self.distance <= 12:
            print("$10")
        else:
            print("No Delivery can be done.")

order_x = Order()
order_x.delivery_charge()