

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

def calculator(mode):
    if (mode == "dine in"):
        print("dine in mode")
    elif (mode == "click and collect"):
        print("click and collect")
    elif (mode == "delivery"):
        print("delivery mode")
    else:
        print("please select a valid option")

def order_operation(mode):
    if mode.lower() == "dine":
        date_of_booking = input("Please enter the Date of booking for dine in:12/11/2022\n")
        time_of_booking = input("Please enter the Time of Booking for the Dine in 16:00\n")
        persons = input("Please enter the number of persons:5\n")
    elif (mode.lower() == "pick up"):
        date_of_pickup = input("Please enter the Date of Pick up:12/11/2022\n")
        time_of_pickup = input("Please enter the time of Pick up 17:00\n")
        persons = input("Please enter the number of Persons:XXXXX\n")
    elif (mode.lower() == "delivery"):
        date_of_pickup = input("Please enter the Date of Delivery:12/11/2022\n")
        time_of_pickup = input("Please enter the time of Delivery 18:00\n")
        distance = input("Please enter the Distance from the restaurant:8\n")
        if int(distance) > 10:
            print("More than the applicable limits, Please you have to pickup order")
    else:
        print("please enter a valid option")
    end_msg = """Thank you for your Order, Your Order has been confirmed.
 Your order id is S001
 Main Menu..."""
    print (end_msg)

def stat():
    stat_options = """Please Enter the Option to Print the Statitics.
 1 - All Dine in Orders.
 2 - All Pick up Orders.
 3 - All Deliveries.
 4 - All Orders (Asccending Order).
 5 - Total Amount Spent on All Orders.
 6 - To go to Previous Menu.
 """
    stat_options_val = input(stat_options)
    if (stat_options_val in ["1", "2", "3", "4", "5", "6"] ):
        if (stat_options_val == "6"):
            print("loading previous menu...")
        elif (stat_options_val == "5"):
            print("""Option 5: Total Amount Spent(All Type of Orders i.e.,
 Dine in, Deliveries and Pickups)
 Total amount spent on all orders AUD: 56.0""")
        elif (stat_options_val in ["1", "2", "3", "4"]):
            print(f"""Option 1: All {stat_options_val} in orders Output:
    Order ID    Date    Total Amount Paid   Type of Order""")
    else:
        print("you entered the wrong option")


class Restaurant:
    users = []

    
    def __init__(self) -> None:
        pass

    """home screen"""
    def landing_page(self):
        landing_page_options = """ Please Enter 1 for Sign up.
 Please Enter 2 for Sign in.
 Please Enter 3 for Quite
 """
        landing_page_options_val = input(landing_page_options)
        if (landing_page_options_val not in ["1", "2", "3"]):
            print("please select 1, 2, 3")
            self.landing_page()
        else:
            if (landing_page_options_val  == "1"):
                self.sign_up()
            elif (landing_page_options_val == "2"):
                self.sign_in()
            elif (landing_page_options_val == "3"):
                exit()

    """the sign up page"""
    def sign_up(self):
        name = input("Please enter you name:XXX ")
        address = input("Please enter your address or press enter to skip. ")
        mobile = input("Please enter your mobile number.0111111111 ")
        password = input("Please your Password:x@11 ")
        confirm_password = input("Please enter you password:x@11 ")
        dob = input("please enter your Date of Birth #DD/MM/YYYY (No space)11/11/1988 ")

        for i in mobile:
            if isinstance(i, int):
                mobile_digit_to_string = str(i)
            else:
                print("this is not a string")

                

        print("You have Successfully Signed up")

    def sign_in(self):
        name = input("Please enter your Username (Mobile Number):01111111111 \n")
        pasword = input("Please enter your password:x@11 \n")
        print("you have successfully signed in")
    
x = Restaurant()
x.landing_page()