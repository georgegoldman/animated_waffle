address = input("full address: ")
distance = int(input("Distance between in Kilometre: "))

if distance > 0 and distance <= 5:
    print("$5")
elif distance > 5 and distance <= 10:
    print("$8")
elif distance > 10 and distance <= 12:
    print("$10")
else:
    print("No Delivery can be done.")
