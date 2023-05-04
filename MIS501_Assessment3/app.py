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
    input(" Enter 1 for Self Pickup.\n Enter 2 for Home Delivery.\n Enter 3 to go to previous Menu.")

def menu(order_online_option):
    menu = """Enter 1 for Noodles Price AUD 2
    Enter 2 for Sandwich Price AUD 4
    Enter 3 for Dumpling Price  AUD 6
    Enter 4 for Muffins Price AUD 8
    Enter 5 for Pasta Price AUD 10"""