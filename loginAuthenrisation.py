#This is a login authentication and authorisation code

# The following are required tests:
#login using email and checks if email exists in the database.An OTP should be generted after password entered which should be used for login as well

#For any transaction that needs to be carried out, a PIN will be entered.

#The following were used in the codes: 
   #Random function to generate random numbers which where then concatenated to generate an OTP.
   #float function is used to wrap the in-built input function so as to accept float entry from the users when supplying amount to redeem or subscribe.
   #displaying numbers to have commas: The format method was used to format the numbers for better presentation such that the thousands have commas. "{:,}".format(variable storing the number to be formated)
   #functions where also called within a function, both the function itself and another function.


import random

database_email={
    "junaid@gmail.com":"00001",
    "idris@gmail.com":"00002",
    "abiodun@gmail.com":"00003"
}

database_pwd={
    "00001":"password1",
    "00002":"password2",
    "00003":"password3"
}

database_pin={
    "00001":"0000",
    "00002":"1111",
    "00003":"2222"
}

currentBalance= {
    "00001":1000000.00,
    "00002":1500000.00,
    "00003":2400000.00
}

#This function is used inside the login function after successful login. The argument is from the login output and further used to reference the balance as well as other necessary actions within the function.
def transProcessing(userid):
    accountBal= round(currentBalance[userid],2)
    accountBalToStr="{:,}".format(accountBal)
    print(f"Your current balance is: {accountBalToStr}")

    print ("Do you want to subscribe (1) or redeem (2)?")
    userAction=input ("Enter transaction type (1 or 2) \n")

    if userAction == "1":    
        addSubscription=float(input("Enter the amount you wish to subscribe \n"))
        userPIN=input("Enter your static pin  \n")
        if userPIN==database_pin[userid]:
            accountBal=round(accountBal+addSubscription,2)
            accountBalToStr="{:,}".format(accountBal)
            print(f"Your new balance is: {accountBalToStr}")
        else:
            print("You have entered a wrong pin")
        
    elif userAction=="2":
        amtToRedeem=float(input("Enter redemption amount \n"))
        userPIN=input("Enter your static pin  \n")
        if userPIN==database_pin[userid]:
            amtToRedeemToStr="{:,}".format(amtToRedeem)
            accountBalaferRed=accountBal-amtToRedeem
            accountBalAfterRedToStr="{:,}".format(accountBalaferRed)
            if amtToRedeem <= accountBal:
                print(f"You have successfully redeemed {amtToRedeemToStr}")
                print(f"Your account balance is now {accountBalAfterRedToStr}")
            else:
                print(f"You do not have sufficient balance to process this redemption. You current balance is {accountBalToStr}")
        else:
            print("You have entered a wrong pin")
    else:
        print("You have selected a wrong option. Please select 1 for subscription or 2 for redemption")

def loginDetails ():
    email= input("Enter email address \n")
    password=input("Enter password \n")

#testing for authentication
    if email in database_email.keys():
        idNumber= database_email[email]
        systemPwd= database_pwd[idNumber]
        if password == systemPwd:
            num1=str((random.randint(0,9)))
            num2=str((random.randint(0,9)))
            num3=str((random.randint(0,9)))
            num4=str((random.randint(0,9)))
            num5=str((random.randint(0,9)))
            num6=str((random.randint(0,9)))
            token= f"{num1}{num2}{num3}{num4}{num5}{num6}"
            print(token)
            userTokenInput=input("Enter OTP  \n")

            if token==userTokenInput:
                print("You have successfully logged in")
                transProcessing(idNumber)



            else:
                print("You have entered a wrong OTP")
                loginDetails ()

        else:
            print("You have entered wrong credentials")
            loginDetails ()

    else:
        print("You have entered wrong credentials")
        loginDetails ()






loginDetails()

