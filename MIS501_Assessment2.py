
user_database = []          #user data base

"""This start function initialize the app or kick start the app"""
def start():
    homePage()

"""This is the landing page"""
def homePage():
    
    """Take in prompt selected by users"""
    home_screen_prompt = int(input("Please Enter 1 for Sign up.\nPlease Enter 2 for Sign in\nPlease Enter 3 for Quit.\n:"))

    """Redirect users base on the option
    the screen they need to see
    """
    if home_screen_prompt == 1:
        sign_up()
    elif home_screen_prompt == 2:
        signIn(0)
    elif home_screen_prompt == 3:
        print("Thank You for using this Application")
        exit()          #this function kill the program
    else:
        print("Please choose a valid option")
        start()

"""This function allows for registration"""
def sign_up():
    name = input("Please enter your name:")
    mobile_number = input("Please enter your mobile number:")
    password = input("Please enter your password:")
    confirm_password = input("Please enter confirm password:")
    date_of_birth = input("Please enter Date of birth #DD/MM/YYYY (No Space):")
    
    """Removing the forward slash 
    in the Date of Birth '/' using split
    String function"""
    format_date_of_birth = date_of_birth.split("/")

    """calculate age"""
    age = 2023 - int(format_date_of_birth[2])

    """Comparing password to confirm password
    if they are the same"""
    if password == confirm_password:
       
       """The password checker
       so that if the password doesn't meet
       our criteria don't continue
       sign up process then show user
       the error"""
       if ("@" in password or "&" in password) and isinstance(int(password[-1]), int):
           
           """This check for age range
           to be allowed in the system"""
           if age > 20:
               userExist = False

               """check if the user
               Exist before creating new user
               to avoid duplicate"""
               for i in user_database:
                   if name == i["name"]:
                       userExist = not userExist
                       break
               if userExist:
                   print("user exist")
               else:
                   """Using a dictionary to create user
                   because the dictionary accepts different data type"""
                   new_user = {
                       "name": name,
                       "mobile_number":mobile_number,
                       "password": password,
                       "date_of_birth": format_date_of_birth
                   }

                   """Add user to the DB []"""
                   user_database.append(new_user)
                   print("You have Successfully Signed up.")
       else:
           print("The Password must initiate with alphabets followed by either one of @, & and ending with numeric. (For Example: Sam@0125, Sam&25)")
           sign_up()
    else:
        print("Your password are not matching.\nPlease start again")
    start()

"""This is the user checker
this function check the database '[]'
for a user"""
def getUser(username_phone):
    for user in user_database:
        if user["name"] == username_phone or user["mobile_number"] == username_phone:
            return user
        else:
            return None

"""This is for sign in
and Authentication"""
def signIn(numbe_of_trial):
    username_phone = input("Please enter your Username (Mobile number):")
    password = input("Please enter your password:")
    user = getUser(username_phone)
    numbe_of_trial += 1         #counter for check for failed sign in limit
    if user:
        if user["password"] == password:
            print(f"You have successfully Signed in\nWelcome {user['name']}")
            signInOption()
        else:
            if (numbe_of_trial == 3 ):
                print("You have used the maximum attempt of login:")
                sign_up()
            else:
                signIn(numbe_of_trial)
            
    else:
        print("Please you have not Signed up with this username, Please Sign up first.")
        start()

"""This function helps to reset password
after 3 trials"""
def forgetPassword():
    print("Please reset the password by entering the below details:")
    username = input("Please enter your username (Mobile number) to confirm:")
    date_of_birth = input("Enter Date of Birth in DD/MM/YYYY format, to confirm:")
    password = input("enter your new password:")
    re_enter = input("Please re-enter your password:")
    user = getUser(username)
    if user:
        count = 0
        for current_user in user_database:
            if current_user["name"] == user["name"]:
                user["password"] = password
                user_database[count] = user
                break
            count += 1
        if user["password"] == password:
            print("You can not use the password used earlier")
            sign_up()
        else:
            print("not successful")
            forgetPassword()
        
"""this display options after
login and option to reset your password"""
def signInOption():
    loginOption = int(input("Please enter 1 for resetting the Password.\nPlease enter 2 for signout."))

    if loginOption == 1:
        resetPassword()
    elif loginOption == 2:
        start()

"""this give user the privillege
to change their password to a new one"""
def resetPassword():
    username_phone = input("Please enter your Username (Mobile Number):")
    password = input("Please enter your password: ")
    user = getUser(username_phone)
    if user:
        if user["password"] == password:
            old_password = input("Please enter old password:")
            if user["password"] == old_password:
                new_password = input("Please enter your new password:")
                count = 0
                for current_user in user_database:
                    if current_user["name"] == user["name"]:
                        user["password"] = new_password
                        user_database[count] = user
                        break
                    count += 1
                if user["password"] == new_password:
                    print("Your Password has been reset successfully.")
                    signInOption()
                else:
                    resetPassword()
            else:
                resetPassword()
        else:
            print("You have not signed up with this contact Number, Please sign up first")
            start()
    else:
        print("You have not signed up with this contact Number, Please sign up first")
        start()

start()