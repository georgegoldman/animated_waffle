#create Restaurant
class Restaurant:
    x = int(input("enter length meter(s): "))
    y = int(input("enter width meter(s): "))

    def __init__(self):
        return

    def size(self):
        return self.x * self.y

    def capacity(self):
        return float(self.size()/1.2 )
    

#instantiate restaurant object
restaurant_a = Restaurant()

if restaurant_a.capacity() > 60:
    print("A Maximum of 60 persons are allowed")