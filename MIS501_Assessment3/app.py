def sign_up():
    name = input("Please enter you name:XXX ")
    address = input("Please enter your address or press enter to skip. ")
    mobile = input("Please enter your mobile number.0111111111 ")
    password = input("Please your Password:x@11 ")
    confirm_password = input("Please enter you password:x@11 ")
    dob = input("please enter your Date of Birth #DD/MM/YYYY (No space)11/11/1988 ")
    print("You have Successfully Signed up")


def sign_in():
    name = input("Please enter your Username (Mobile Number):01111111111 ")
    print("")
    pasword = input("Please enter your password:x@11 ")
    print("you have successfully signed in")

#this function handles the dashboard
def dashboard():
    option = input("Please Enter 2.1 to start Ordering.\nPlease Enter 2.2 to Print Statistics.\nPlease enter 2.3 for Logout.\n")
    log_out = print("")
   
    if option == "2.1":
        ordering(option)
    elif option == "2.2":
        print("Printing Statistics...")
    elif option == "2.3":
        print("Loging out...")
    else:
        print("Please select a valid option");


def ordering(option):
    order_option = input(f"{option}\n Please Enter 1 for Dine in.\n Please Enter 2 for Order Online.\n Please Enter 3 to go to Login page\n")

    if order_option == "2":
        order_online()


def order_online():
    order_option = """ Enter 1 for Self Pickup. 
 Enter 2 for Home Delivery.
 Enter 3 to go to previous Menu."""
    order_option_value = input(order_option)
    if (order_option_value == "1" or order_option_value == 2):
        menu(order_option_value)
    elif(order_option_value == 3):
        ordering(None)
    else:
        print("Please a valid option")
        order_online()

def menu(order_online_value):
    print(order_online_value)
    menu_option = """ Enter 1 for Noodles Price AUD 2
 Enter 2 for Sandwich Price AUD 4
 Enter 3 for Dumpling Price  AUD 6
 Enter 4 for Muffins Price AUD 8
 Enter 5 for Pasta Price AUD 10
 Enter 6 for Pizza Price AUD 20
 Enter 7 for Drinks Menu:
 """
    menu_option_value = input(menu_option)
    if (menu_option_value == "7"):
        print("loading option 7")
    elif (menu_option in ["1","2","3","4","5","6"]):
        print("order options...")
    else:
        print("please select a valid option")

def drink_menu(menu_option_value):
    print(menu_option_value)
    dink_option = """Enter 1 for Coffee Price AUD 2
 Enter 2 for Colddrink Price AUD 4
 Enter 3 for Shake Price AUD 6
 Enter 4 fro Checkout:
 """
    drink_option_value = input(dink_option)
    if (drink_option_value in ["1", "2", "3"]):
        print("you selected a drink")
    elif drink_option_value == "4":
        check_out = """Please Enter Y to proceed to Checkout or
 Enter N to cancel the order """
        check_out_value = input(check_out)
        if check_out_value.lower() == "y":
            print("Proceeding to checkout")
        elif check_out_value.lower() == "n":
            print("cancling check out")
        else:
            print("please select a valid option")
    
def no_address_alert():
    msg = """You have not mentioned your address, while signing up.
 Please Enter Y if you would like to enter your address.
 Enter N if you would like to select mode of order
 """
    msg_option = input(msg)
    if (msg_option.lower() == "y"):
        print("you selected y")
    elif (msg_option.lower() == "n"):
        print("you selected n")
    else:
        print("please enter a valid option")

def calculator():
    