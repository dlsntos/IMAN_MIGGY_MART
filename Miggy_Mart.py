from tabulate import tabulate 
from Customer import Customer
from Display import Display
from Manager import Manager
import mysql.connector
import time
t = 1.2 
display = Display()
mysqlconnect = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")
cursor = mysqlconnect.cursor()
Flag = True
while Flag:
    display.logo()#testing
    display.start_menu()
    try:
        user = int(input("\nEnter choice here: "))
        if user < 1 or user > 3:
            display.print_c("\n!Out of range please try again","red")
            time.sleep(t)
            display.clear_screan()
        else:
            while Flag:  
                try:
                    #choose customer mode
                    if user == 1:
                        display.clear_screan()
                        customer = Customer()
                        display.logo()
                        display.registration_menu()
                        choice = int(input("Enter Choice: "))
                        # Customer registration
                        if choice == 1:
                            display.clear_screan()
                            display.logo()
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
                            customer.customer_registration(customer_id,customer_name,customer_age,customer_contactNum,customer_state,customer_city,customer_email,customer_balance,customer_password) 
                        #customer login
                        elif choice == 2:
                            display.clear_screan()
                            display.logo()
                            customer_id = int(input("Enter Customer ID: "))
                            customer_password = input("Enter Customer Password: ")
                            display.clear_screan()
                            try:
                                cursor.execute("SELECT * FROM customer WHERE customerid = %s AND password = %s", (customer_id , customer_password))
                                result = cursor.fetchone()
                                if result:
                                    while Flag:
                                        display.logo()
                                        display.customer_menu()
                                        choice = int(input("\nEnter Choice: "))
                                        if choice == 1:
                                            display.clear_screan()
        #Calls the retrieve_info function
                                            product_id = input("Enter Product ID: ")
                                            customer_id = input("Enter Customer ID: ")
                                            if product_id == "" or customer_id == "" :
                                                print("ID is required, Please try again")
                                            else:
                                                customer.add_cart(int(product_id), int(customer_id))
                                    
                                        elif choice == 2:#Customer Login 
                                            display.clear_screan()
                                            display.logo()
                                            customer.retrieve_cart()
                                            product_id = input("Enter Product ID: ")
                                            cart_id = input("Enter Cart ID: ")
                                            if product_id == "" or cart_id == "" :
                                                print("\nID is required, Please try again")
                                            else:
                                                customer.remove_item(int(product_id), int(cart_id))
                                            pass

                                        elif choice == 3:
                                            display.clear_screan()
                                            display.logo()
                                            customer.retrieve_cart()
                                            pass

                                        elif choice == 4:
                                            display.clear_screan()
                                            display.logo()
                                            customer.checkout()
                                            pass

                                        elif choice == 5:
                                            display.clear_screan()
                                            display.logo()
                                            print("All categories: ")
                                            cursor.execute('select distinct(type) from inventory')
                                            types = cursor.fetchall()
                                            valid_types = [index[0].lower() for index in types]
                                            headers = [i[0] for i in cursor.description]                                                              
                                            rows = [[str(cell) for cell in record] for record in types] 
                                            print(tabulate(rows, headers=headers, tablefmt='grid'))
                                            type_id = input("Enter a category here: ")
                                            if type_id.lower() not in valid_types:
                                                print("Category not found")
                                            else:
                                                customer.category_search(type_id)

                                        elif choice == 6:
                                            display.clear_screan()
                                            display.logo()
                                            customer.retrieve_inventory()
                                        elif choice == 7:
                                            customer.exit_program_clear_cart()
                                            display.logo()
                                            print("Thank you for using our program!")
                                            exit()
                                        else:
                                            print("!Invalid Choice")
                                            time.sleep(t)
                                            display.clear_screan()
                                else:
                                    print("!Invalid credentials")
                                    time.sleep(t)
                                    display.clear_screan()
                                    break
                            except mysql.connector.Error as err:
                                print("Error:", err)
                                time.sleep(t)
                                display.clear_screan()
                    #choose Store Manager mode
                    elif user == 2:
                        display.clear_screan()
                        manager = Manager()
                        display.logo()
                        manager_id = int(input("Enter Manager ID: "))
                        manager_password = input("Enter password: ")
                        try:
                            display.clear_screan()
                            cursor.execute("SELECT * FROM manager WHERE managerid = %s AND password = %s", (manager_id, manager_password))
                            result = cursor.fetchone()
                            while Flag:
                                #Manager Login
                                if result:
                                    display.print_c("Login successful\n","green")
                                    time.sleep(t)
                                    display.clear_screan()
                                    display.logo()
                                    display.manager_menu()
                                    choice = int(input("Enter choice here: "))
                                    #Add item
                                    if choice == 1:
                                        display.clear_screan()
                                        display.logo()
                                        productID = int(input("Enter Product ID: "))
                                        product_description = input("Enter Product Description: ")
                                        product_type = input("Enter Product type: ")
                                        price = float(input("Enter Product price: "))
                                        date = input("Enter Expiration Date: ")
                                        quantity = int(input("Enter Quantity: "))
                                        manager.add_item_to_inventory(productID,product_description,product_type,price,date,quantity)
                                    #Remove item
                                    elif choice == 2:
                                        display.clear_screan()
                                        display.logo()
                                        productID = int(input("Enter Product ID: "))
                                        manager.remove_expired_items_from_directory(productID)
                                    elif choice == 3:
                                        display.clear_screan()
                                        display.logo()
                                        productID = int(input("Enter Product ID: "))
                                        price = float(input("Enter Updated Product price: "))
                                        manager.update_item_price(productID, price)
                                    elif choice == 4:
                                        display.logo()
                                        print("Thank you for using our program!")
                                        exit()
                                    Flag = False
                                else:
                                    display.print_c("Invalid credentials","red")
                                    time.sleep(t)
                                    display.clear_screan()
                                    break
                        except mysql.connector.Error as err:
                            print("Error:", err)
                            time.sleep(t)
                            display.clear_screan()
                    elif user == 3:
                        print("Thank you for using our program!")
                        exit()   
                except ValueError:
                    display.print_c("!Enter a valid value","red")
                    time.sleep(t)
                    display.clear_screan()
    except ValueError:
        display.print_c("\n!Enter a valid value","red")
        time.sleep(t)
        display.clear_screan()
    #Checks if mysql connected with python.
    if mysqlconnect.is_connected():  #print('Connected Successfully')
        print()
    else:
        print('Failed to connect')
        mysqlconnect.close()