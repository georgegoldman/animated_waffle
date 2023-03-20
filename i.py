customer_name = input("Enter customer’s name: ")
mobile_number = input("Enter mobile number: ")
year_of_birth = input("Enter year of birth: ")
current_city = input("Enter current city: ")
email_address = input("Enter email address: ")

year_of_birth_toInt = int(year_of_birth)
age  = 2023 - year_of_birth_toInt

if age > 21:
    print("\nCustomer details")
    print(f"customer’s name: {customer_name}")
    print(f"customer’s mobile number: {mobile_number}")
    print(f"year of birth: {year_of_birth}")
    print(f"current city: {current_city}")
    print(f"email address: {email_address}")