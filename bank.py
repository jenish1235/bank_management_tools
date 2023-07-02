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

# New Account Creation Function
def create_new_account(account_choice,name,mobile_number,city,mail,dob,membername,membermobile,memberdob,userpin):
   
    print("Server Connected")
    print("sending your data")
    print("waiting for response")
    
    
    
    if(account_choice == 1):
        data = (f'{name}', f'{mobile_number}', f'{city}',f'{mail}',f'{dob}',f'{userpin}')
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO savings_Account_Users (name,mobile_number,city,mail,dob,userpin) VALUES (%s,%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Savings account😁😊😁")
    elif(account_choice == 2):
        data = (f'{name}', f'{mobile_number}', f'{city}',f'{mail}',f'{dob}',f'{userpin}')
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO current_Account_Users (name,mobile_number,city,mail,dob,userpin) VALUES (%s,%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Current account😁😊😁")
    elif(account_choice == 3):
        data = (f'{name}',f'{membername}',f'{mobile_number}',f'{membermobile}', f'{city}',f'{mail}',f'{dob}',f'{memberdob}')
        main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO joint_Account_Users (name,member,mobile_number,member_mobile,city,mail,dob,member_dob) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",data)
        print("Succesfully Created your Joint account😁😊😁")
    main.bank_Database_Connection.commit()



# Welcome Message
print("\n\n **************** Welcome To Bank ***************")
print("\n\nHello User, Happy To See At Our Place")

# Check IF USer Want new Account Or already have one
user_acc_check = int(input("\n\nPlease Select From Following option to proceed :\n1. Create A New Account\n2. You have an existing Account\n3. Get Assistance And Know More About Us\n4.Careers\n(press command number to select)  : "))
print("\n\nLet's Complete With Login/Signup process")


# If user wants account
if(user_acc_check == 1):
    print("\n\nPlease Read Our Terms,Policy and Manual At www.blog.com")
    print("\n\nOkay Let's Proceed with Sign up process\n\nPlease cooperate with further steps by providing required information to complete your registration and open a account with us 😊😊😊 ")
    
    # Choose Acc. Type
    customer_choice_account_type = int(input("Please Select The type of Account You want to open\n\n1. Savings Account\n2. Current Acount\n3. Joint Account \n(You can Read about account opening ,their types and benefits on www.blog.com): "))
    
    # Customer Data Collection
    customer_name1 = input("Please Enter Your Fullname in caps(firstname secondname lastname): ")
    mobile_number = int(input("Please Enter Your Mobile Number without country code: "))
    city = input("Please Enter your residencial city: ")
    mail = input("Please Enter Your Email ID: ")
    dob_of_customer = input("Please Enter Your date of birth (NO SPECIAL CHARS LIKE slash,dash or commas)(DDMMYYYY): ")
    user_pin = pwinput.pwinput("Please Set pin: " , mask="*")
    confirm_user_pin = pwinput.pwinput("Please Confirm Pin: ", mask = "*")
    
    
    
    if(customer_choice_account_type == 3):
        member_name = input("Please enter another member's fullname (firstnam secondname lastname): ")
        member_mobile = int(input("Please Enter Member mobile number without country code: "))
        member_dob = int(input("Please Enter Member's Date of birth(DDMMYYYY)(NO Symbols): "))
    else: 
        member_name = ""
        member_mobile = None
        member_dob = None
    
    # backend data post and account nummber assignment
    try:
        create_new_account(customer_choice_account_type,customer_name1,mobile_number,city,mail,dob_of_customer,member_name,member_mobile,member_dob,user_pin)
        
        if(customer_choice_account_type == 1):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT customer_id from savings_Account_Users")
            customer_Id_coloumn = main.cursor_to_create_tables_in_bank_Database.fetchall()
            required_customer_id = str(customer_Id_coloumn.__len__())
            required_customer_acc_number = "360101" + required_customer_id
            print(f"\n\nYOUR ACCOUNT NUMBER IS:   {required_customer_acc_number}")
            
            
            
            
    except:
        print("Sorry , Server Down")
            
        
        
    
# If user Already HAve Account
elif(user_acc_check == 2):
    user_account_type_to_check_existence_in_table = int(input("Please Select Your Account Type\n\n1. Savings Account\n2.Current Account\n3.Joint Account  : "))
    if(user_account_type_to_check_existence_in_table == 1):
        user_account_number = input("Please Enter Your account number: ")
        user_id_to_check_in_table = user_account_number.removeprefix("360101")
        main.cursor_to_create_tables_in_bank_Database.execute("SELECT * from savings_Account_Users WHERE customer_id = %s" , (user_id_to_check_in_table,))
        foundedUser = main.cursor_to_create_tables_in_bank_Database.fetchall()
        if(foundedUser[0][0] == int(user_id_to_check_in_table)):
            founded_User_Name = foundedUser[0][1]
            print(f"HELLO , {founded_User_Name}")
                        
            while(True):
                askedpassword_to_login = int(pwinput.pwinput("Please Enter Pin: ", mask = "*"))
                if(askedpassword_to_login == foundedUser[0][6]):
                    print("Login Successful😎😎😎😎😎😎😎😎")
                    break
                else:
                    print("Sorry Login Unsuccessful,PLease try Again...\n")
                
            
        
        