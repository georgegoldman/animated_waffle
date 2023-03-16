print("ctrl+z to exit program")
mobile_number = input("Insert mobile number: ")
password = input("Insert password: ")
# print(len(mobile_number))
# exit()
if len(mobile_number) == 10 or len(password) <= 8:
    print("Invalid credentials")
else:
    print("Done")