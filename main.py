# *** Bank Management Software Backend Code *** #

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

# Connection to mysql...

try:
        sql_Connection = mysql.connector.connect(
            host = "localhost", 
            user = "jenish",
            password = "jenish1235"
        )
        
        print("Successfully connected to server")
except: 
        print("Error Connecting to Server")
    

# Creating the Database For Banking Software

cursor_for_database_creation = sql_Connection.cursor()
try:
    cursor_for_database_creation.execute("CREATE DATABASE bank_Database")
    
    # print("database: bank_Database Created Succesfully")

# check statement pending 
except:
    print("error creating database")
    pass

# Connection to Database

try:
    bank_Database_Connection = mysql.connector.connect(
        host = "localhost",
        user = "jenish",
        password = "jenish1235",
        database = "bank_Database"
        
    )   
except:
    print("Unable To Connect To Database")

# Creating table for user registration in bank_Database
try:
    cursor_to_create_tables_in_bank_Database = bank_Database_Connection.cursor()
    cursor_to_create_tables_in_bank_Database.execute(
        "CREATE TABLE savings_Account_Users (customer_id INT AUTO_INCREMENT PRIMARY KEY,accountNumber INT(15),name VARCHAR(255),mobile_number VARCHAR(20),city VARCHAR(255),mail VARCHAR(255),dob INT(8),userpin INT(4),accountBalance INT(16))")
    
    cursor_to_create_tables_in_bank_Database.execute(
        "CREATE TABLE transaction_history (accountNumber INT(20) , amount INT(20),transaction VARCHAR(10))")
    
    cursor_to_create_tables_in_bank_Database.execute(
        "CREATE TABLE joint_Account_Users (customer_id INT(20),accountNumber INT(20),joint_account_holder_name VARCHAR(255),joint_account_holder_mobile_number VARCHAR(20),joint_account_holder_city VARCHAR(255),joint_account_holder_mail VARCHAR(255),joint_account_holder_dob INT(8),joint_account_holder_userpin INT(4),account_balance INT(16))"
    )
    cursor_to_create_tables_in_bank_Database.execute("INSERT INTO joint_Account_Users (customer_id,accountNumber,joint_account_holder_name,joint_account_holder_mobile_number,joint_account_holder_city,joint_account_holder_mail,joint_account_holder_dob,joint_account_holder_userpin,account_balance) VALUES (0,0,0,0,0,0,0,0,0)")
    bank_Database_Connection.commit()
    
    cursor_to_create_tables_in_bank_Database.execute("CREATE TABLE transaction_history_for_joint_accounts (accountNumber INT(20), amount INT(20), nameOfTransactor VARCHAR(255), transaction VARCHAR(10))")
    bank_Database_Connection.commit()
    
except:
    print("error creating table")



