from Customer import Customer
from Display import Display
from Manager import Manager
import mysql.connector
import time

display = Display()
customer = Customer()
manager = Manager()
t = 1.2
mysqlconnect = mysql.connector.connect(host = "localhost", user = "root",password = "", database = "miggymart")
cursor = mysqlconnect.cursor()

class Menu:
    def customer(self):
        display.clear_screan()
        display.logo()
        display.registration_menu()
        choice = int(input("Enter Choice: "))
        if choice == 1:
            customer.customerRegistration()
        elif choice == 2:
            display.clear_screan()
            display.logo()
            customer_id = int(input("Enter Customer ID: "))
            customer_password = input("Enter Customer Password: ")
            display.clear_screan()
            cursor.execute("SELECT * FROM customer WHERE customerid = %s AND password = %s", (customer_id , customer_password))
            result = cursor.fetchone()
            while True:
                try:
                    if result:
                        display.logo()
                        display.customer_menu()
                        choice = int(input("\nEnter Choice: "))
                        if choice == 1:
                            customer.addtocart()
                        elif choice == 2:
                            customer.removeFromCart()
                        elif choice == 3:
                            customer.retrieve_cart()  
                        elif choice == 4:
                            customer.checkout()
                        elif choice == 5:
                            customer.showCategory()
                        elif choice == 6:
                            customer.retrieve_inventory()
                        elif choice == 7:
                            customer.exit_program_clear_cart()
                            display.logo()
                            print("Thank you for using our program!")
                            exit()
                        else:
                            display.logo()
                            display.print_c("!Invalid credentials","red")
                            time.sleep(t)
                            display.clear_screan()
                    else:
                        display.logo()
                        display.print_c("!Invalid credentials","red")
                        time.sleep(t)
                        display.clear_screan()
                        break
                except ValueError:
                    display.print_c("!Invalid credentials","red")
                    time.sleep(t)
                    display.clear_screan()
    def manager(self):
        display.clear_screan()
        display.logo()
        manager_id = int(input("Enter Manager ID: "))
        manager_password = input("Enter password: ")
        while True:
            try:
                display.clear_screan()
                cursor.execute("SELECT * FROM manager WHERE managerid = %s AND password = %s", (manager_id, manager_password))
                result = cursor.fetchone()
                                    #Manager Login
                if result:
                    display.print_c("Login successful\n","green")
                    display.clear_screan()
                    display.logo()
                    display.manager_menu()
                    choice = int(input("Enter choice here: "))
                    while True:                            
                        if choice == 1:
                            manager.add_item_to_inventory()                            
                        elif choice == 2:
                            manager.remove_expired_items_from_directory()
                        elif choice == 3:
                            manager.update_item_price()
                        elif choice == 4:
                            display.clear_screan()
                            display.logo()
                            print("Thank you for using our program!")
                            exit()
                        else:
                            display.print_c("Invalid credentials","red")
                            time.sleep(t)
                            display.clear_screan()
                            break
            except ValueError:
                display.print_c("!Enter a valid value","red")
                time.sleep(t)
                display.clear_screan()
            except mysql.connector.Error as err:
                print("Error:", err)
                time.sleep(t)
                display.clear_screan()