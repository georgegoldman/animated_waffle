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

