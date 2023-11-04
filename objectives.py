import main
import bank

# Code Block For Account Deletion Banking Facility
if (facility_selected_by user == 7):
    confirmation_to_delete_account = input("Plwease confirm the account deletion(y/n): ")
    if(confirmation_to_delete_account.lower() == 'y'):
        main.cursor_to_create_tables_in_bank_Database.execute("DELETE * FROM .......... WHERE accountNumber = %s", [f'{accountNumberEnteredByUsers}'])
        print("Account Deleted Successfully")
        main_function()
    else:
        print("Okay Account Is Not Deleted")
        

# Code Block for help
print("help")

