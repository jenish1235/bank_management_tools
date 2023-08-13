# *** Bank Management Software User End Code*** #

###*************************************************************************************************************************************### 

# Project Description:- 
# A minimalistic bank management software developed to help banking systems go online and to make the banking system quick and stable.

#Technology Used :- 

# 1. Python 3.11.4 
# Database:  MySQL 8.0.34


### Database Access Credentials over localhost 
### username : jenish , password: jenish1235, hostname:localhost

# created and managed by :   Jenish Togadiya

###*************************************************************************************************************************************###

import mysql
import mysql.connector
import main
import pwinput
from time import sleep as sleep



# function for checking account existence and registration help 
def main_function():
    integer_to_ask_customer_about_existence_of_account = None
    integer_for_selection_of_account_type_to_open_account = None
    
    integer_to_ask_customer_about_existence_of_account = int(input("\n\nPlease Select From Following option to proceed :\n1. Create A New Account\n2. You have an existing Account\n3. Get Assistance And Know More About Us\n4.Careers\n(press command number to select)  : "))
    if(integer_to_ask_customer_about_existence_of_account == 1):
        print("Okay Let's Start with the account creation process")
    elif(integer_to_ask_customer_about_existence_of_account == 2):
        print("Okay Please Login with your Credentials to use banking facilities")
    elif(integer_to_ask_customer_about_existence_of_account == 3):
        # Sasta chatbot and little gyaan to be written here
        pass
    elif(integer_to_ask_customer_about_existence_of_account == 4):
        print("Getting You to career Options... ")
        sleep(2)
    else:
        print("invalid command selected")
        main_function()


    if(integer_to_ask_customer_about_existence_of_account == 1):
        print("\n\nPlease Read Our Terms,Policy and Manual At www.blog.com")
        sleep(2)
        print("\n\nOkay Let's Proceed with Sign up process\n\nPlease cooperate with further steps by providing required information to complete your registration and open a account with us 😊😊😊 ")
        
        integer_for_selection_of_account_type_to_open_account = int(input("Please Select The type of Account You want to open\n\n1. Savings Account\n2. Joint Account \n(You can Read about account opening ,their types and benefits on www.blog.com): "))
        # If User selected to open a savings account
        if(integer_for_selection_of_account_type_to_open_account == 1):
            
            print("You selected to open a Savings Account")
            # Account holder's information collection 
            saving_account_holder_name = input("Please Enter Your Fullname in caps(firstname secondname lastname): ")
            saving_account_mobile_number = int(input("Please Enter Your Mobile Number without country code: "))
            saving_account_holder_city = input("Please Enter your residencial city: ")
            saving_account_holder_mail = input("Please Enter Your Email ID: ")
            saving_account_holder_dob = input("Please Enter Your date of birth (NO SPECIAL CHARS LIKE slash,dash or commas)(DDMMYYYY): ")     
            while (True):
                saving_account_holder_user_pin = pwinput.pwinput("Please Set pin: " , mask="*")
                saving_account_holder_confirm_user_pin = pwinput.pwinput("Please Confirm Pin: ", mask = "*")
                if(saving_account_holder_user_pin == saving_account_holder_confirm_user_pin):
                    break
                else:
                    print("Your entered pin and confirmation pin doesn't match , please try again 😢😢😢")
                    
            # Savings Account Holder's Account Number Assignment
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT customer_id from savings_Account_Users")
            account_holders_id_column_fetched_from_table = main.cursor_to_create_tables_in_bank_Database.fetchall()
               
            account_holder_id_required_to_assign_next_account_number = str( account_holders_id_column_fetched_from_table.__len__())
            final_string_account_number_assigned = "360101" + account_holder_id_required_to_assign_next_account_number
            print(f"\n\nYOUR ACCOUNT NUMBER IS:   {final_string_account_number_assigned}")
            
            # Sending information of savings account holder to table 
            try:
                funtion_to_create_new_savings_account(saving_account_holder_name,saving_account_mobile_number,saving_account_holder_city,saving_account_holder_mail,saving_account_holder_dob,saving_account_holder_user_pin,final_string_account_number_assigned)
                
                print("")
                print(f"Hello {saving_account_holder_name}, Welcome to your savings account dashboard, u can proceed further with banking facilities happily 😉😉😉")
                
                function_for_banking_Facilities_for_savings_account()
                
            except Exception as e:
                print("Unable to register a new account as following error occured: \n\n", e)
        
        elif(integer_for_selection_of_account_type_to_open_account == 2):
            print("Okay!, Please Cooperate with further process to complete Your Joint Account, You can read More about joint at www.blog.com")
            sleep(1.0)
            
            number_of_distinct_account_holders_to_include_in_joint_account = int(input("Please enter total number of members for joint account: "))
            print("Okay, Please Fill the following details for all the user")
            
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT customer_id from joint_Account_Users")
            account_holders_id_column_fetched_from_table = main.cursor_to_create_tables_in_bank_Database.fetchall()
            customer_id = int(account_holders_id_column_fetched_from_table[-1][0])+1
            account_holder_id_required_to_assign_next_account_number = str(customer_id)
            final_string_account_number_assigned = "360101" + account_holder_id_required_to_assign_next_account_number
            print(f"\n\nYOUR ACCOUNT NUMBER IS:   {final_string_account_number_assigned}")
            
                      
            for joint_account_data_collection_loop_int_i in range(number_of_distinct_account_holders_to_include_in_joint_account):
                joint_account_holder_name = input("Please Enter Your Fullname in caps(firstname secondname lastname): ")
                joint_account_mobile_number = int(input("Please Enter Your Mobile Number without country code: "))
                joint_account_holder_city = input("Please Enter your residencial city: ")
                joint_account_holder_mail = input("Please Enter Your Email ID: ")
                joint_account_holder_dob = input("Please Enter Your date of birth (NO SPECIAL CHARS LIKE slash,dash or commas)(DDMMYYYY): ")     
                while (True):
                    joint_account_holder_user_pin = pwinput.pwinput("Please Set pin: " , mask="*")
                    joint_account_holder_confirm_user_pin = pwinput.pwinput("Please Confirm Pin: ", mask = "*")
                    if(joint_account_holder_user_pin == joint_account_holder_confirm_user_pin):
                        break
                    else:
                        print("Your entered pin and confirmation pin doesn't match , please try again 😢😢😢")
                function_to_create_new_joint_account(customer_id,final_string_account_number_assigned,joint_account_holder_name,joint_account_mobile_number,joint_account_holder_city,joint_account_holder_mail,joint_account_holder_dob,joint_account_holder_user_pin)    
            
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT joint_account_holder_name FROM joint_Account_Users WHERE accountNumber = %s",[f'{final_string_account_number_assigned}'])
            list_type_gathered_information_of_new_created_account = main.cursor_to_create_tables_in_bank_Database.fetchall()
            print("")
            print("Successfully created your joint account with following Members: ")
            for i in range(number_of_distinct_account_holders_to_include_in_joint_account):
                print(str(i+1),")", list_type_gathered_information_of_new_created_account[i-1][0])
            
            
                
    
    
    elif(integer_to_ask_customer_about_existence_of_account == 2 ):
        function_for_banking_Facilities_for_savings_account()
# funtion to create the saving account
def funtion_to_create_new_savings_account(saving_account_holder_name,saving_account_mobile_number,saving_account_holder_city,saving_account_holder_mail,saving_account_holder_dob,saving_account_holder_user_pin,final_string_account_number_assigned):
    print("Connecting Database")
    sleep(1.0)
    
    print("Database Connected Successfully\nSending Information to register new savings account\nWaiting for response")
    data = (f'{final_string_account_number_assigned}',f'{saving_account_holder_name}', f'{saving_account_mobile_number}', f'{saving_account_holder_city}',f'{saving_account_holder_mail}',f'{saving_account_holder_dob}',f'{saving_account_holder_user_pin}',0)
    main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO savings_Account_Users (accountNumber,name,mobile_number,city,mail,dob,userpin,accountBalance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",data)
    
    main.bank_Database_Connection.commit()
    sleep(1.0)
    print("Succesfully Created your Savings account😁😊😁")
# Funtion for banking facilities for saving account holders
def function_for_banking_Facilities_for_savings_account():
    account_number_entered_by_user_to_check_in_saving_account_table = str(int(input("Please enter your account number: ")))
    account_pin_entered_by_user_to_check_in_savings_account_table = int(pwinput.pwinput('Enter pin: '))
    print("Searching User")
    
    # Searching for Account holder in savings account table
    try:
        main.cursor_to_create_tables_in_bank_Database.execute("SELECT * from savings_Account_Users WHERE accountNumber = %s" , [f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
        founded_account_holder = main.cursor_to_create_tables_in_bank_Database.fetchall()
        sleep(1)
        print("Account Founded")
    
    except Exception as e:
        print("Can't complete request because: ",e)
    
    # Loop to compare pin entered by user with pin set while register a saving account
    while True:
        if(account_pin_entered_by_user_to_check_in_savings_account_table == founded_account_holder[0][7]):
            print("Authentication Successful😊😊")
            break
        else:
            print("Authentication Failed")
            account_pin_entered_by_user_to_check_in_savings_account_table = int(pwinput.pwinput("You Entered A Wrong Pin 😡😡😡😡😡😡, Enter Your Pin Again: "))
    
    # Loop For Banking Facilities
    while (True):
        facility_selected_by_account_holder = int(input("Please Select An Action TO Perform: \n1.Account Info   2.Check Account Balance   3.Deposit Money    4.Withdraw Money   5. Check Transaction History 6: Go back : "))
        
        if(facility_selected_by_account_holder == 1):
            
            founded_saving_account_holder_name = founded_account_holder[0][2]
            founded_saving_account_holder_mobile_number = founded_account_holder[0][3]
            founded_saving_account_holder_city = founded_account_holder[0][4]
            founded_saving_account_holder_mail = founded_account_holder[0][5]
            founded_saving_account_holder_dob = founded_account_holder[0][6]
            
            print("ACCOUNT TYPE: Savings Account")
            print(f"Account Holder's Details:\n\nNAME: {founded_saving_account_holder_name}\nMOBILE NUMBER: {founded_saving_account_holder_mobile_number}\nCITY: {founded_saving_account_holder_city}\nMAIL: {founded_saving_account_holder_mail}\nDATE OF BIRTH: {founded_saving_account_holder_dob}")

        elif(facility_selected_by_account_holder == 2):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
            integer_balance_of_account_holder = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]
            
            print(f"ACCOUNT BALANCE: {integer_balance_of_account_holder}  Rupees")

        elif(facility_selected_by_account_holder == 3):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
            integer_balance_of_account_holder = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]
            
            integer_amount_to_deposit_in_account = int(input("Please Enter Amount Of Money To Deposit: "))
            integer_account_balance_after_crediting_specified_amount = int(integer_balance_of_account_holder)+integer_amount_to_deposit_in_account
            
            print("Processing Request")
            sleep(2)
            
            try:
                main.cursor_to_create_tables_in_bank_Database.execute("UPDATE savings_Account_Users SET accountBalance = %s WHERE accountNumber = %s" , [f'{integer_account_balance_after_crediting_specified_amount}',f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
                main.bank_Database_Connection.commit()
                print(F"Request processed, money credited successfully. UPDATED ACCOUNT BALANCE: {integer_account_balance_after_crediting_specified_amount}")
                integer_balance_of_account_holder = integer_account_balance_after_crediting_specified_amount
                transaction_info = [f'{account_number_entered_by_user_to_check_in_saving_account_table}',f'{integer_amount_to_deposit_in_account}', 'credited']
                main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO transaction_history(accountNumber,amount,transaction) VALUES (%s,%s,%s) ", transaction_info)
                main.bank_Database_Connection.commit()
            except Exception as e:
                print("Can't Complete Request Becuase: ",e) 
        
        elif(facility_selected_by_account_holder == 4):
            main.cursor_to_create_tables_in_bank_Database.execute("SELECT accountBalance FROM savings_Account_Users WHERE accountNumber = %s", [f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
            integer_balance_of_account_holder = main.cursor_to_create_tables_in_bank_Database.fetchall()[0][0]            
            
            integer_amount_to_withdraw_from_account = int(input("Please Enter Amount Of Money TO withdraw: "))
            integer_account_balance_after_withdrawing_specified_amount = int(integer_balance_of_account_holder)-integer_amount_to_withdraw_from_account
            
            print("Processing Request")
            sleep(2)
            
            try:
                main.cursor_to_create_tables_in_bank_Database.execute("UPDATE savings_Account_Users SET accountBalance = %s WHERE accountNumber = %s" , [f'{integer_account_balance_after_withdrawing_specified_amount}',f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
                main.bank_Database_Connection.commit()
                integer_balance_of_account_holder = integer_account_balance_after_withdrawing_specified_amount
                transaction_info = [f'{account_number_entered_by_user_to_check_in_saving_account_table}',f'{integer_amount_to_withdraw_from_account}', 'debited']
                main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO transaction_history(accountNumber,amount,transaction) VALUES (%s,%s,%s) ", transaction_info)
                main.bank_Database_Connection.commit()
            except Exception as e:
                print("Can't complete request because", e)
        
        elif(facility_selected_by_account_holder == 5):
            print("Fetching Your Transaction History")
            try:
                main.cursor_to_create_tables_in_bank_Database.execute("SELECT * FROM transaction_history WHERE accountNumber = %s", [f'{account_number_entered_by_user_to_check_in_saving_account_table}'])
                transaction_history_of_user_fetched_from_transaction_history_table_for_saving_accounts = main.cursor_to_create_tables_in_bank_Database.fetchall()
                print(transaction_history_of_user_fetched_from_transaction_history_table_for_saving_accounts)
            except Exception as e:
                print("Can't complete request because: ",e)
        
        elif(facility_selected_by_account_holder == 6):
            main_function()
            
        
        else:
            print("Please Select a valid command")    

def function_to_create_new_joint_account(customer_id,final_string_account_number_assigned,joint_account_holder_name,joint_account_mobile_number,joint_account_holder_city,joint_account_holder_mail,joint_account_holder_dob,joint_account_holder_user_pin):
    
    print("Connecting Database")
    sleep(1.0)
    
    print('Database Connected Successfully\nSending Information to register new joint account\n Waiting for response')
    data = (
        f"{customer_id}", 
        f"{final_string_account_number_assigned}",
        f"{joint_account_holder_name}",
        f"{joint_account_mobile_number}",
        f"{joint_account_holder_city}",
        f"{joint_account_holder_mail}",
        f"{joint_account_holder_dob}",
        f"{joint_account_holder_user_pin}",
        0)
    
    main.cursor_to_create_tables_in_bank_Database.execute("INSERT INTO joint_Account_Users (customer_id,accountNumber,joint_account_holder_name,joint_account_holder_mobile_number,joint_account_holder_city,joint_account_holder_mail,joint_account_holder_dob,joint_account_holder_userpin,account_balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",data)
    main.bank_Database_Connection.commit()
    sleep(1.0)
    print("Successfully Created Your joint Account")




















####################################################################################################################################################
#############################*/*//*/*//* This Code Runs Initially and above written functions are used during the funtioning of below code *//*/*//*/*################################
####################################################################################################################################################

#  Welcome Message
print("\n\n **************** Welcome To Bank ***************")
print("\n\nHello User, Happy To See At Our Place")

#Checking Account Existence Of User And Pre-Registration Help
main_function()        