print("ctrl+z to exit program")
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