
get_listOfSalesCurrentWeek = input("The list of orders total prices of the current week in AUD: ")
get_listOfSalesPreviouseWeek = input("The list of orders total prices of the previous week in AUD: ")

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