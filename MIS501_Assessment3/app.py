#this function handles the dashboard
    







class Calculator:
        def total_price_in_cart(self, cart):
            amount = 0
            for item in cart:
                amount += item["price"]
            return amount
            

class Restaurant(Calculator):
    users = []
    logged_in_user = ""

    cart = []
    id_count = 0

    all_dine_in_order = []
    all_pick_up_order = []
    all_delivery_order = []

    order_mode = ""

    food_item = {
        "1": {
            "name": "Noodles",
            "price": 2
        },
        "2": {
            "name": "Sandwich",
            "price": 4
        },
        "3": {
            "name": "Dumpling",
            "price": 6
        },
        "4": {
            "name": "Muffins",
            "price": 8
        },
        "5": {
            "name": "Pasta",
            "price": 10
        },
        "6": {
            "name": "Pizza",
            "price": 12
        }
    }

    drink_item = {
        "1": {
            "name": "Coffee",
            "price": 2
        },
        "2": {
            "name": "Colddrink",
            "price": 4
        },
        "3": {
            "name": "Shake",
            "price": 6
        }
    }
    

    
    def _init_(self) -> None:
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

        """check if the mobile number are digits"""
        if mobile.isnumeric():
            """check if the password conform to the pattern"""
            if ("@" in password and password[-1].isnumeric()):
                """check if pass match confirmed password"""
                if (password == confirm_password):
                    """split DOB to check format criteria"""
                    get_date_of_birth = dob.split("/")
                    if (get_date_of_birth[0].isnumeric() and get_date_of_birth[1].isnumeric() and get_date_of_birth[2].isnumeric()):
                        
                        if (int(get_date_of_birth[0]) >31):
                            print("Please enter a valid day of birth")
                            self.sign_up()
                        elif (int(get_date_of_birth[1])>12):
                            print("please enter a valid month of birth")
                            self.sign_up()
                        else:
                            
                            """check if user already exist"""
                            if self.users :
                                for user in self.users:
                                    if (user["mobile"] == mobile):
                                        print("user already exit")
                                        self.landing_page()
                                    else:
                                        newUser = {
                                        "name": name,
                                        "address": address,
                                        "mobile": mobile,
                                        "password": password,
                                        "dob": dob,
                                        }
                                        self.users.append(newUser)
                                        self.landing_page()
                    
                            else:
                                newUser = {
                                        "name": name,
                                        "address": address,
                                        "mobile": mobile,
                                        "password": password,
                                        "dob": dob
                                    }
                                self.users.append(newUser)
                                self.landing_page()
                    else:
                        print("Invalid date of birth format ok")
                        self.landing_page()
                else:
                    print("here please password does not match")
                    self.sign_up()
            else:
                print("Please enter a valid password format")
                self.sign_up()
        else:
            print("invalid phone number")
            self.sign_up()
                

    def sign_in(self):
        username = input("Please enter your Username (Mobile Number):01111111111 \n")
        pasword = input("Please enter your password:x@11 \n")
        
        """check if the user exist in the list of registered uers"""
        for x in self.users:
            
            """check look up the username which is mobile"""
            if x["mobile"] == username:
                """if user validate password"""
                if (x["password"] == pasword):
                    self.logged_in_user = username
                    print(f"you have successfully signed in {self.logged_in_user}")
                    self.dashboard()

                else:
                    """if password does not match display error and 
                    redirect user to login"""
                    print("Please enter a valid password")
                    self.sign_in()
            else:
                """if does not exist through warning request to login"""
                print("User does not exist please sign up")
                self.sign_up()
        print("User does not exist please sign up")
        self.landing_page()
        
    
    def dashboard(self):
        option = input("Please Enter 2.1 to start Ordering.\nPlease Enter 2.2 to Print Statistics.\nPlease enter 2.3 for Logout.\n")
        log_out = print("")
    
        if option == "2.1":
            self.ordering()
        elif option == "2.2":
            self.stat()
        elif option == "2.3":
            print("Loging out...")
            self.landing_page()
        else:
            print("Please select a valid option");

    def stat(self):
        stat_options = """Please Enter the Option to Print the Statitics.
 1 - All Dine in Orders.
 2 - All Pick up Orders.
 3 - All Deliveries.
 4 - All Orders (Ascending Order).
 5 - Total Amount Spent on All Orders.
 6 - To go to Previous Menu.
    """
        stat_options_val = input(stat_options)
        if (stat_options_val in ["1", "2", "3", "4", "5", "6"] ):
            if (stat_options_val == "6"):
                self.dashboard()
            elif (stat_options_val == "5"):
                all_order = self.all_delivery_order + self.all_dine_in_order + self.all_pick_up_order
                total_value = self.total_price_in_cart(all_order)
                print(f"""Option 5: Total Amount Spent(All Type of Orders i.e.,
    Dine in, Deliveries and Pickups)
    Total amount spent on all orders AUD: {total_value}""")
            elif (stat_options_val in ["1", "2", "3", "4"]):
                order_type = {
                    "1": "Dine in",
                    "2": "Pick up",
                    "3": "delivery",
                    "4": "desce"
                }

                if (stat_options_val == "1"):
                    print(f"""Option 1: All {stat_options_val} in orders Output:
 Order ID    Date    Total Amount Paid   Type of Order""")
                    for order in self.all_dine_in_order:
                        id = order["price"]
                        price = order["price"]
                        date = order["date"]
                        print(f"""{id}        {date}     {price}   Dine in""")
                if (stat_options_val == "2"):
                    print(f"""Option 1: All {stat_options_val} in orders Output:
 Order ID    Date    Total Amount Paid   Type of Order""")
                    for order in self.all_pick_up_order:
                        id = order["price"]
                        price = order["price"]
                        date = order["date"]
                        print(f"""{id}        {date}     {price}   """)
                        
        else:
            print("you entered the wrong option")

    def ordering(self):
        order_option = input(f"\n Please Enter 1 for Dine in.\n Please Enter 2 for Order Online.\n Please Enter 3 to go to Login page\n")

        if order_option == "2":
            # move the user to order online
            self.order_online()
        elif (order_option == "1"):
            #set user ordering mode and move user for dine
            self.order_mode = "dine in"
            self.menu("1")
        elif (order_option == "3"):
            self.dashboard()
        else:
            print("Please enter a valid option")
            self.ordering()

    def order_online(self):
        order_option = """ Enter 1 for Self Pickup. 
 Enter 2 for Home Delivery.
 Enter 3 to go to previous Menu."""
        order_option_value = input(order_option)
        if (order_option_value == "1"):
            #set order mode
            self.order_mode =  "click and collect"           
            self.menu(order_option_value)
        elif (order_option_value == "2"):
            self.order_mode =  "delivery mode"           
            self.menu(order_option_value)
        elif(order_option_value == 3):
            self.ordering()

        else:
            print("Please a valid option")
            self.order_online()

    def menu(self, order_type):
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
            self.drink_menu(order_type)
        elif (menu_option_value in ["1","2","3","4","5","6"]):
            new_item = self.food_item[f"{menu_option_value}"]
            self.cart.append(new_item)
            print(self.cart)
            self.menu(order_type)
        else:
            print("please select a valid option")
            self.menu(order_type)
        
    def drink_menu(self, order_type):
        dink_option = """Enter 1 for Coffee Price AUD 2
 Enter 2 for Colddrink Price AUD 4
 Enter 3 for Shake Price AUD 6
 Enter 4 fro Checkout:
    """
        drink_option_value = input(dink_option)
        if (drink_option_value in ["1", "2", "3"]):
            new_item = self.food_item[f"{drink_option_value}"]
            self.cart.append(new_item)
            print(self.cart)
            self.drink_menu(order_type)
        elif drink_option_value == "4":
            """check for order typer if pick up or delivery"""
            check_out = """Please Enter Y to proceed to Checkout or
 Enter N to cancel the order """
            check_out_value = input(check_out)
            if (order_type == "2"):
                for user in self.users:
                    if(user["mobile"] == self.logged_in_user):
                        if (user["address"] == ""):
                            self.no_address_alert()
                            self.drink_menu(order_type)
                    else:
                        print("smart anon")
                        self.landing_page()
                 
            if check_out_value.lower() == "y":
                """get list of options the person has bought
                and calculate values"""
                if (self.order_mode == "dine in"):
                    cart_bill = self.total_price_in_cart(self.cart)
                    charges = cart_bill * (15/100)
                    plus_charges = cart_bill + charges
                    print(f"Your total payble amount is: {plus_charges} inclusing AUD {charges} for Service Charges")
                    self.order_operation(self.order_mode, plus_charges)
                elif (self.order_mode == "click and collect"):
                    print(f"Your total payble is: {self.total_price_in_cart(self.cart)}")
                    self.order_operation(self.order_mode, self.total_price_in_cart(self.cart))
                elif (self.order_mode == "delivery"):
                    bill = self.total_price_in_cart(self.cart)
                    print(f"Your total payble is: {bill} and there will be an additional charges for delivery.")
                    self.order_operation(self.order_mode, bill)
                else:
                    print("please select a valid option")
            elif check_out_value.lower() == "n":
                print("cancling check out")
            else:
                print("please select a valid option")


    def no_address_alert(self):
        msg = """You have not mentioned your address, while signing up.
 Please Enter Y if you would like to enter your address.
 Enter N if you would like to select mode of order
    """
        msg_option = input(msg)
        if (msg_option.lower() == "y"):
            address_value = input("Please Enter an address ")
            if (address_value == "" and address_value.isspace()):
                print("Please enter a valid option")
                self.no_address_alert()
            else:
                for user in self.users:
                    if (user["mobile"] == self.logged_in_user):
                        user["address"] = address_value
                        get_position = self.users.index(user)
                        self.users[get_position] = user
                    else:
                        print("Please Sign in or Sign up")
                        self.landing_page()
        elif (msg_option.lower() == "n"):
            self.ordering()
        else:
            print("please enter a valid option")
    
    def order_operation(self, mode, plus_service):
        if mode.lower() == "dine in":
            date_of_booking = input("Please enter the Date of booking for dine in:12/11/2022\n")
            time_of_booking = input("Please enter the Time of Booking for the Dine in 16:00\n")
            persons = input("Please enter the number of persons:5\n")
            #check if user entered a numbers
            if (persons.isnumeric() and date_of_booking.count("/") == 2 and (":" in time_of_booking)):
                date_to_list = date_of_booking.split("/")
                for i in date_to_list:
                    if i.isnumeric():
                        pass

                    else:
                        print("Please enter valid date 12/11/2022")
                        self.order_operation(mode, plus_service)
                id = "S{:03d}".format(self.id_count)
                self.id_count += 1
                new_dine_order = {
                    "date": date_of_booking,
                    "time": time_of_booking,
                    "price": plus_service * int(persons)
                }
                self.all_dine_in_order.append(new_dine_order)
                print("Thank you for your Order, Your Order has been confirmed.")
                self.dashboard()
                
            else:
                print("please enter a valid order")
                self.order_operation(mode, plus_service)
        elif (mode.lower() == "click and collect"):
            date_of_pickup = input("Please enter the Date of Pick up:12/11/2022\n")
            time_of_pickup = input("Please enter the time of Pick up 17:00\n")
            persons = input("Please enter the number of Persons:XXXXX\n")
            if (persons.isnumeric() and date_of_pickup.count("/") == 2 and (":" in time_of_pickup)):
                date_to_list = date_of_pickup.split("/")
                for i in date_to_list:
                    if i.isnumeric():
                        pass
                        
                    else:
                        print("Please enter valid date 12/11/2022")
                        self.order_operation(mode, plus_service)
                id = "S{:03d}".format(self.id_count)
                self.id_count += 1
                new_pickup_order = {
                    "id": id,
                    "date": date_of_pickup,
                    "time": time_of_pickup,
                    "price":plus_service * int(persons)
                }
                self.all_pick_up_order.append(new_pickup_order)
                print("Thank you for your Order, Your Order has been confirmed.")
                self.dashboard()
                
            else:
                print("please enter a valid order")
                self.order_operation(mode, plus_service)
        elif (mode.lower() == "delivery"):
            date_of_pickup = input("Please enter the Date of Delivery:12/11/2022\n")
            time_of_pickup = input("Please enter the time of Delivery 18:00\n")
            distance = input("Please enter the Distance from the restaurant:8\n")
            if int(distance) > 15:
                print("More than the applicable limits, Please you have to pickup order")
            else:
                if (distance.isnumeric() and date_of_pickup.count("/") == 2 and (":" in time_of_pickup)):
                    date_to_list = date_of_pickup.split("/")
                    for i in date_to_list:
                        if i.isnumeric():
                            pass
                        else:
                            print("Please enter valid date 12/11/2022")
                            self.order_operation(mode, plus_service)
                    if (int(distance) < 6):
                        plus_service += 5
                    elif (int(distance) < 11):
                        plus_service += 10
                    elif (int(distance) < 15):
                        plus_service += 18
                    else:
                        pass
                    id = "S{:03d}".format(self.id_count)
                    self.id_count += 1
                    new_delivery_order = {
                        "id": id,
                        "date": date_of_pickup,
                        "time": time_of_pickup,
                        "persons": int(distance),
                        "price": plus_service
                    }
                    self.all_delivery_order.append(new_delivery_order)
                    print("Thank you for your Order, Your Order has been confirmed.")
                    self.dashboard()
                    
                else:
                    print("please enter a valid order")
                    self.order_operation(mode, plus_service)
        else:
            print("please enter a valid option")
        end_msg = """Thank you for your Order, Your Order has been confirmed."""
        print (end_msg)
        self.dashboard()

    


x = Restaurant()
x.landing_page()