x = float(input("enter length meter(s): "))
y = float(input("enter width meter(s): "))

area = x * y

restaurant_capacity = area / 1.2

if restaurant_capacity > 60:
    print("A Maximum of 60 persons are allowed")