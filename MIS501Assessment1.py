# i
print("\ni. Customers details:")
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

# ii
print("\nii. Restaurant Capacity:")
x = float(input("enter length meter(s): "))
y = float(input("enter width meter(s): "))

area = x * y

restaurant_capacity = area / 1.2

if restaurant_capacity > 60:
    print("A Maximum of 60 persons are allowed")

# iii
print("\niii. average per person sale ")
get_listOfSalesCurrentWeek = input("The list of orders total prices of the current week in AUD format 1,2,34,2 or 22.43,43.4,3.43: ")
get_listOfSalesPreviouseWeek = input("The list of orders total prices of the previous week in AUD 1,2,34,2 or 22.43,43.4,3.43: ")

getTotalNumberOfPersonVisitedCurrentWeek = int(input("Total number of persons visited in the Current Week: "))
getTotalNumberOfPersonVisitedPreviouseWeek = int(input("Total number of persons visited in the Previouse Week: "))

listOfSalesCurrentWeek = get_listOfSalesCurrentWeek.split(",")
listOfSalesPreviouWeek = get_listOfSalesCurrentWeek.split(",")

total_get_listOfSalesCurrentWeek = 0
total_get_listOfSalesPreviouseWeek = 0

for current_sales in listOfSalesCurrentWeek:
    total_get_listOfSalesCurrentWeek += float(current_sales)

for previous_sales in listOfSalesPreviouWeek:
    total_get_listOfSalesPreviouseWeek += float(previous_sales)

current_week_per_person_average_sale = total_get_listOfSalesCurrentWeek/getTotalNumberOfPersonVisitedCurrentWeek
previous_week_per_person_average_sale = total_get_listOfSalesPreviouseWeek/getTotalNumberOfPersonVisitedPreviouseWeek


print(f"Current Week per person average sale= {current_week_per_person_average_sale}")
print(f"Current Week per person average sale= {previous_week_per_person_average_sale}")

# iv
print("\niv. calculate and print the amount of change")
print("Sample Input:")
total_invoice_amount = float(input("Total Invoice amount (In Dollars):\t"))
amount_of_tip = float(input("Amount of Tip (In Cents):\t"))
total_payment_by_card = float(input("Total Payment received by Card:\t"))
service_charge_on_card = input("Service Charge on Payment made by Card format '4%':\t")
total_cash_payment = float(input("Total Payment received in Cash (In Dollars):\t"))

remove_last_char_to_float = 0
if "%" in service_charge_on_card:
    remove_last_char = service_charge_on_card[:-1]
    service_charge_on_card = float(remove_last_char)
else:
    service_charge_on_card = float(service_charge_on_card)

service_charge_for_card = total_payment_by_card * (service_charge_on_card/100)

tips_in_dollar = amount_of_tip * 0.0011

total_expenses = total_invoice_amount + service_charge_for_card

total_payment = tips_in_dollar + total_cash_payment + total_payment_by_card

total_customer_balance = total_payment - total_expenses

if total_customer_balance < 0:
    print(f"Outstanding amount and need to be paid by customer: {-1 * total_customer_balance}")
print(f"Change to be returned to the customer (In Dollars):\t\t{total_customer_balance}")

# v
print("\nv. estimate of the order delivery charges")
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

# vi
print("\nvi estimate of the order delivery charges")
enter_order = int(input("Insert the order base cost in AUD:\t"))
enter_order_type = int(input("enter order type\n 1 for dine in\n 2 for pick up\n 3 for deivery\n:\t"))

order_charges = {
        1: ["dine in", 8],
        2: ["pick up", 0],
        3: ["delivery", 10]
    }

print(enter_order + (enter_order * (order_charges[enter_order_type][1]*0.01)))

# vii
print("\nvii. temperature conversion")
#let temp = temperature, conv = convertion
get_temp_value = float(input("Insert the temperature value: "))
get_conv_form = int(input("Insert conversion form\n1- from Centigrade to Fahrenheit\n2-From Fahrenheit to Centigrade\n: "))

if get_conv_form == 1 or get_conv_form == 2:
    if get_conv_form == 1:
        #let cent = centigrade, fah = fahrenheit.
        cent_to_fah = (get_temp_value * 9/5) + 32
        print(f"{cent_to_fah}°F")
    elif get_conv_form == 2:
        fah_to_cent = (get_temp_value - 32)*5/9
        print(f"{fah_to_cent}°C")
    else:
        print("Invalid Entry")
elif get_conv_form != 1 or get_conv_form != 2:
    print("Invalid Entry")
print("done")

# viii
print("\nviii. calculating the net monthly income of theemployee after the tax is deducted")
enter_position = input("position of the employee (chef, waiter or deliver): ")
enter_hours = float(input("number of monthly hours the employee worked: "))
#convert postion to lower case
postion_to_lowercase = enter_position.lower()

tax_rate = 20/100

if postion_to_lowercase == "chef":
    income = enter_hours * 50
    tax = income * tax_rate
    net_monthly_income = income - tax
    print(f"the net monthly income of the employee after the tax is deducted is ${net_monthly_income}")
elif postion_to_lowercase == "waiter":
    income = enter_hours * 40
    tax = income * tax_rate
    net_monthly_income = income - tax
    print(f"the net monthly income of the employee after the tax is deducted is ${net_monthly_income}")
elif postion_to_lowercase == "deliver":
    income = enter_hours * 35
    tax = income * tax_rate
    net_monthly_income = income - tax
    print(f"the net monthly income of the employee after the tax is deducted is ${net_monthly_income}")
else:
    print(" Invalid Entry")

print("Done")

# ix
print("\nix. user credential signing up a new account")
mobile_number = input("Insert mobile number: ")
password = input("Insert password: ")
# print(len(mobile_number))
# exit()
if len(mobile_number) == 10 or len(password) <= 8:
    print("Invalid credentials")
else:
    print("Done")