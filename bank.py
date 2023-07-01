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

def create_new_account(account_choice,name,mobile_number,city,mail,dob):
   
    print("Server Connected")
    print("sending your data")
    print("waiting for response")
    
    data = (f'{name}', f'{mobile_number}', f'{city}',f'{mail}',f'{dob}')
    
    if(account_choice == 1):
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO savingsAccountUsers (name,mobile_number,city,mail,dob) VALUES (%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Savings account😁😊😁")
    elif(account_choice == 2):
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO currentAccountUsers (name,mobile_number,city,mail,dob) VALUES (%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Current account😁😊😁")
        
    main.bank_Database_Connection.commit()


# Welcome Message
print("\n\n **************** Welcome To Bank ***************")
print("\n\nHello User, Happy To See At Our Place")

# Check IF USer Want new Account Or already have one
user_acc_check = int(input("\n\nPlease Select From Following option to proceed :\n1. Create A New Account\n2. You have an existing Account\n3. Get Assistance And Know More About Us\n4.Careers\n(press command number to select)  : "))
print("Let's Complete With Login/Signup process")


# If user wants account
if(user_acc_check == 1):
    print("\n\n Please Read Our Terms And Policy and Manual At www.blog.com")
    print("\n\n Okay Let's Proceed with Sign up process \n \n  Please cooperate with further steps by providing required information to complete your registration and open a account with us 😊😊😊 ")
    customer_name1 = input("Please Enter Your Fullname in caps(firstname secondname lastname): ")
    mobile_number = int(input("Please Enter Your Mobile Number without country code: "))
    city = input("Please Enter your residencial city: ")
    mail = input("Please Enter Your Email ID: ")
    dob_of_customer = input("Please Enter Your date of birth (NO SPECIAL CHARS LIKE slash,dash or commas)(DDMMYYYY): ")
    
    customer_choice_account_type = int(input("Please Select The type of Account You want to open\n1. Savings Account\n2. Current Acount\n3. Joint Account \n(You can Read about account opening ,their types and benefits on www.blog.com): "))
    print("Okay , Please Wait Processing Your Request With Server")
    # Connection to mysql bankdatabase 
    try:
        create_new_account(customer_choice_account_type,customer_name1,mobile_number,city,mail,dob_of_customer)       
    except:
        print("Sorry , Server Down")
            
        
        
    
# If user Already HAve Account
elif(user_acc_check == 2):
    pass