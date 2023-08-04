# *** Bank Management Software User End Code*** #

###*************************************************************************************************************************************### 

# Project Description:- 
# A minimalistic bank management software developed to help banking systems go online and to make the banking system quick and stable.

#Technology Used :- 

# 1. Python 3.11.4 
# Database:  MySQL 8.0.33


### Database Access Credentials over localhost 
### username : jenish , password: jenish1235, hostname:localhost

# created and managed by :   Jenish Togadiya

###*************************************************************************************************************************************###


import mysql
import mysql.connector
import main
import pwinput

# Welcome Message
print("\n\n **************** Welcome To Bank ***************")
print("\n\nHello User, Happy To See At Our Place")

# Check IF User Want new Account Or already have one
user_acc_check = int(input("\n\nPlease Select From Following option to proceed :\n1. Create A New Account\n2. You have an existing Account\n3. Get Assistance And Know More About Us\n4.Careers\n(press command number to select)  : "))
print("\n\nLet's Complete With Login/Signup process")



# New Account Creation Function
def create_new_account(account_choice,accountNumber,name,mobile_number,city,mail,dob,userpin):
   
    print("Server Connected")
    print("sending your data")
    print("waiting for response")
       
    if(account_choice == 1):
        data = (f'{accountNumber}',f'{name}', f'{mobile_number}', f'{city}',f'{mail}',f'{dob}',f'{userpin}',1000)
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO savings_Account_Users (accountNumber,name,mobile_number,city,mail,dob,userpin,accountBalance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Savings account😁😊😁")
    main.bank_Database_Connection.commit()


# Banking Facilities Function
def bankingOption(account_choice,name,mobile_number,city,mail,dob):
    accNumber = int(input("Please Enter Your Account Your Number: "))
    userpinentered = int(pwinput.pwinput('Enter User Pin: '))
    main.cursor_to_create_tables_in_bank_Database.execute("SELECT * from savings_Account_Users WHERE accountNumber = %s" , [f'{accNumber}'])
    foundedUser = main.cursor_to_create_tables_in_bank_Database.fetchall()
    
    while True:
        if(userpinentered == foundedUser[0][7]):
            print("Authentication Successful😊😊")
            break
        else:
            print("Authentication Failed")
            userpinentered = int(pwinput.pwinput("You Entered A Wrong Pin 😡😡😡😡😡😡, Enter Your Pin Again: "))
        
        
    while (True):
        user_action_selection = int(input("Please Select An Action TO Perform: \n1.Account Info   2.Check Account Balance   3.Deposit Money    4.Withdraw Money   5. Check Transaction History: "))
        
        if(user_action_selection == 1):
            if(account_choice == 1):
                print("ACCOUNT TYPE: Savings Account")
            elif(account_choice ==2):
                print("ACCOUNT TYPE: Current Account")
            elif(account_choice == 3):
                print("ACCOUNT TYPE: Joint Account")
            acc_holder_name = str.upper(name)
            print(f"Name Of Account Holder: {acc_holder_name}")
            print(f"Account Holder Mobile Number: {mobile_number}")
            print(f"Account Number: {accNumber}")
            print(f"Date Of Birth: {dob}")
            print(f"Residence: {city}")
            print(f"Account Holder's Email Address: {mail}")
                    
        elif(user_action_selection == 2):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{accNumber}'])
            Account_Balance_Of_User = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]
            print(f"ACCOUNT BALANCE: {Account_Balance_Of_User}  Rupees")
            
            
        elif(user_action_selection == 3):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{accNumber}'])
            Account_Balance_Of_User = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]
            amount_to_deposit = int(input("Please Enter Amount Of Money To Deposit: "))
            new_Account_Balance_after_deposit = int(Account_Balance_Of_User)+amount_to_deposit
            main.cursor_to_create_tables_in_bank_Database.execute("UPDATE savings_Account_Users SET accountBalance = %s WHERE accountNumber = %s" , [f'{new_Account_Balance_after_deposit}',f'{accNumber}'])
            main.bank_Database_Connection.commit()
            Account_Balance_Of_User = new_Account_Balance_after_deposit
            transaction_info = [f'{accNumber}',f'{amount_to_deposit}', 'credited']
            main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO transaction_history(accountNumber,amount,transaction) VALUES (%s,%s,%s) ", transaction_info)
            main.bank_Database_Connection.commit()
            
            
        elif(user_action_selection == 4):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{accNumber}'])
            Account_Balance_Of_User = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]            
            amount_to_withdraw = int(input("Please Enter Amount Of Money TO withdraw: "))
            new_Account_Balance_after_withdraw = int(Account_Balance_Of_User)-amount_to_withdraw
            main.cursor_to_create_tables_in_bank_Database.execute("UPDATE savings_Account_Users SET accountBalance = %s WHERE accountNumber = %s" , [f'{new_Account_Balance_after_withdraw}',f'{accNumber}'])
            main.bank_Database_Connection.commit()
            Account_Balance_Of_User = new_Account_Balance_after_withdraw
            transaction_info = [f'{accNumber}',f'{amount_to_withdraw}', 'debited']
            main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO transaction_history(accountNumber,amount,transaction) VALUES (%s,%s,%s) ", transaction_info)
            main.bank_Database_Connection.commit()
        
        elif(user_action_selection == 5):
            print("Fetching Your Transaction History")
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT * FROM transaction_history WHERE accountNumber = %s", [f'{accNumber}'])
            transaction_history_of_user = main.cursor_to_create_tables_in_bank_Database.fetchall()
            print(transaction_history_of_user)





# If user wants account
if(user_acc_check == 1):
    print("\n\nPlease Read Our Terms,Policy and Manual At www.blog.com")
    print("\n\nOkay Let's Proceed with Sign up process\n\nPlease cooperate with further steps by providing required information to complete your registration and open a account with us 😊😊😊 ")
    
    # Choose Acc. Type
    customer_choice_account_type = int(input("Please Select The type of Account You want to open\n\n1. Savings Account\n2. Current Acount\n3. Joint Account \n(You can Read about account opening ,their types and benefits on www.blog.com): "))
    
    # Customer Data Collection
    customer_name = input("Please Enter Your Fullname in caps(firstname secondname lastname): ")
    mobile_number = int(input("Please Enter Your Mobile Number without country code: "))
    city = input("Please Enter your residencial city: ")
    mail = input("Please Enter Your Email ID: ")
    dob_of_customer = input("Please Enter Your date of birth (NO SPECIAL CHARS LIKE slash,dash or commas)(DDMMYYYY): ")
    user_pin = pwinput.pwinput("Please Set pin: " , mask="*")
    confirm_user_pin = pwinput.pwinput("Please Confirm Pin: ", mask = "*")
    # Account Number Assignment
    if(customer_choice_account_type == 1):
        main.cursor_to_create_tables_in_bank_Database.execute("SELECT customer_id from savings_Account_Users")
        customer_Id_coloumn = main.cursor_to_create_tables_in_bank_Database.fetchall()
        required_customer_id = str(customer_Id_coloumn.__len__())
        required_customer_acc_number = "360101" + required_customer_id
        print(f"\n\nYOUR ACCOUNT NUMBER IS:   {required_customer_acc_number}")
    
    
    # backend data post
    try:
        create_new_account(customer_choice_account_type,required_customer_acc_number,customer_name,mobile_number,city,mail,dob_of_customer,user_pin)
        
        
        print("")
        print(f"Hello {customer_name}, Welcome TO Your Bank DashBoard Now U Can Proceed with Banking Facilities")
        bankingOption(customer_choice_account_type,customer_name,mobile_number,city,mail,dob_of_customer)
            
    except Exception as e:
        print(e)
        