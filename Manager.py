from tabulate import tabulate 
from CustomerQueries import CustomerQueries
from Display import Display
from Manager import Manager
import mysql.connector

#TODO Manager class and methods
#temporary class#create new customer
display = Display()
mysqlconnect = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")
cursor = mysqlconnect.cursor()
Flag = True
while Flag:
    display.print_colored("\n[Welcome to MIGGIEMART]\n", "cyan")#testing
    print("\nPlease Enter a Login Option\n")
    print("[1] Customer\n"
          "[2] Manager\n"
          "[3] Exit")
    try:
        user = int(input("Enter choice here: "))
        if user < 1 or user > 3:
            print("\n[Out of range please try again]")
        else:
            display.clear_screan()
            while Flag:  
                try:
                    if user == 1:#If user chooses customer mode
                        customerquery = CustomerQueries()
                        print("\n[1] Register")
                        print("[2] Login")
                        choice = int(input("Enter Choice: "))
                        if choice == 1:# Customer registration
                            display.clear_screan()
                            print("[Customer Registration]\n")
                            customer_id = int(input("Enter Customer ID: "))
                            customer_name = input("Enter Customer Name: ")
                            customer_age = int(input("Enter Customer Age: "))
                            customer_contactNum = int(input("Enter Customer No.: "))
                            customer_state = input("Enter Customer State: ")
                            customer_city = input("Enter Customer City: ")
                            customer_email = input("Enter Customer email: ")
                            customer_balance = int(input("Enter Customer Balance: "))
                            customer_password = input("Set Customer Password: ")
                            display.clear_screan()
                            customerquery.customer_registration(customer_id,customer_name,customer_age,customer_contactNum,customer_state,customer_city,customer_email,customer_balance,customer_password) 
                        elif choice == 2:#customer login
                            customer_id = int(input("Enter Customer ID: "))
                            customer_password = input("Enter Customer Password: ")
                            display.clear_screan()
                            try:
                                cursor.execute("SELECT * FROM customer WHERE customerid = %s AND password = %s", (customer_id , customer_password))
                                result = cursor.fetchone()
                                if result:
                                    while Flag:
                                        print("\n[Welcome to MIGGIEMART]")
                                        print("\nCustomer Cart:"
                                            "\n[1] Add to Cart"
                                            "\n[2] Remove from Cart"
                                            "\n[3] Display Cart"
                                            "\n[4] Checkout\n"
                                            "\nGrocery Items:"
                                            "\n[5] Search by category"
                                            "\n[6] Display items for sale\n"
                                            "\nExit:"
                                            "\n[7] Exit Program")
                                        choice = int(input("\nEnter Choice: "))
                                        if choice == 1:
                                            display.clear_screan()
                                            #Calls the retrieve_info function
                                            product_id = input("Enter Product ID: ")
                                            customer_id = input("Enter Customer ID: ")
                                            if product_id == "" or customer_id == "" :
                                                print("ID is required, Please try again")
                                            else:
                                                customerquery.add_cart(int(product_id), int(customer_id))
                                    
                                        elif choice == 2:
                                            display.clear_screan()
                                            customerquery.retrieve_cart()
                                            product_id = input("Enter Product ID: ")
                                            cart_id = input("Enter Cart ID: ")
                                            if product_id == "" or cart_id == "" :
                                                print("\nID is required, Please try again")
                                            else:
                                                customerquery.remove_item(int(product_id), int(cart_id))
                                            pass

                                        elif choice == 3:
                                            display.clear_screan()
                                            customerquery.retrieve_cart()
                                            pass

                                        elif choice == 4:
                                            display.clear_screan()
                                            customerquery.checkout()
                                            pass

                                        elif choice == 5:
                                            display.clear_screan()
                                            print("All categories: ")
                                            cursor.execute('select distinct(type) from inventory')
                                            types = cursor.fetchall()
                                            headers = [i[0] for i in cursor.description]                                                              
                                            rows = [[str(cell) for cell in record] for record in types] 
                                            print(tabulate(rows, headers=headers, tablefmt='grid'))
                                            type_id = input("Enter a category here: ")
                                            if type_id.lower() != "bakery" or type_id.lower() != "dairy" or type_id.lower() != "fruit" or type_id.lower() != "vegetable" or type_id.lower() != "meat" or type_id.lower() != "seafood":
                                                print("Category not found")
                                            else:
                                                customerquery.category_search(type_id)
                                                Flag = False

                                        elif choice == 6:
                                            display.clear_screan()
                                            customerquery.retrieve_inventory()
                                        elif choice == 7:
                                            customerquery.exit_program_clear_cart()
                                            print("Thank you for using our program!")
                                            exit()
                                        else:
                                            print("[Invalid Choice]")
                                else:
                                    print("[Invalid credentials]")
                                    break
                            except mysql.connector.Error as err:
                                print("Error:", err)
                    elif user == 2:
                        manager = Manager()
                        manager_id = int(input("Enter Manager ID: "))
                        manager_password = input("Enter password: ")
                        try:
                            display.clear_screan()
                            cursor.execute("SELECT * FROM manager WHERE managerid = %s AND password = %s", (manager_id, manager_password))
                            result = cursor.fetchone()
                            while Flag:
                                if result:
                                    print("Login successful.")
                                    print("\n[ Miggy Mart ADMIN ACCESS ]")
                                    print("[1] Add item to inventory")
                                    print("[2] Remove Expired Item")
                                    print("[3] Update Item Prices")
                                    print("[4] Exit")
                                    choice = int(input("Enter choice here: "))
                                    if choice == 1:
                                        display.clear_screan()
                                        productID = int(input("Enter Product ID: "))
                                        product_description = input("Enter Product Description: ")
                                        product_type = input("Enter Product type: ")
                                        price = float(input("Enter Product price: "))
                                        date = input("Enter Expiration Date: ")
                                        quantity = int(input("Enter Quantity: "))

                                        manager.add_item_to_inventory(productID,product_description,product_type,price,date,quantity)
                                    elif choice == 2:
                                        display.clear_screan()
                                        productID = int(input("Enter Product ID: "))
                                        manager.remove_expired_items_from_directory(productID)
                                    elif choice == 3:
                                        display.clear_screan()
                                        productID = int(input("Enter Product ID: "))
                                        price = float(input("Enter Updated Product price: "))
                                        manager.update_item_price(productID, price)
                                    elif choice == 4:
                                        print("Thank you for using our program!")
                                        exit()
                                    Flag = False
                                else:
                                    display.clear_screan()
                                    print("Invalid credentials.")
                                    break
                        except mysql.connector.Error as err:
                            print("Error:", err)
                    elif user == 3:
                        print("Thank you for using our program!")
                        exit()   
                except ValueError:
                    display.clear_screan()
                    print("[Enter Valid a Value]")
    except ValueError:
        display.clear_screan()
        print("[Enter Valid a Value]")
    #Checks if mysql connected with python.
    if mysqlconnect.is_connected():  #print('Connected Successfully')
        print()
    else:
        print('Failed to connect')
        mysqlconnect.close()

            
    
        


