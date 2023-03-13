#importt  date lib for age calculation
from datetime import date

#get input from console
def cin(message):
        return input(f"{message}: ")

#cin takes in string or text convert to date form
def getDateOfBirth():
    DOB = cin("Enter date of birth in this format year/month/day")
    DOB_list = DOB.split("/")
    if len(DOB_list) < 3:
         print("Wrong Date of birth format...\nExiting signup...")
         exit()
    else:
         return date(int(DOB_list[0]), int(DOB_list[1]), int(DOB_list[2]))

#this is a customer class
class Customer:

    #this are the attribute of a customer as defined in the prolem
    name = cin("Enter a name")
    mobile_number = cin("Enter mobile number")
    year_of_birth = getDateOfBirth()
    current_city = cin("Enter your current city")
    email = cin("Enter your email address")

    #the cals contructor
    def __init__(self):
        return

    #this function print to the console how you want the class to look
    def __repr__(self):
        return f'''
        __Customer__
        \nName:\t{self.name}
        \nMobile number:\t {self.mobile_number}
        \nYear of Birth:\t {self.year_of_birth}
        \nCurrent city:\t {self.current_city}
        \nEmail address:\t {self.email}
        '''

    #this function calculates the customer's age
    def age(self):
        return int(date.today().year) - int(self.year_of_birth.year)



#instantiating a customer object
customer_x = Customer()

if customer_x.age() > 21:
    print(customer_x)

print("Done")