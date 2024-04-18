import mysql.connector
from tabulate import tabulate
from Display import Display
import time

delay = 1.5 
display = Display()

class Customer:

    def __init__(self):                                                                                                    #constructor
        self.connection = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")  #connection attribute
        self.cursor = self.connection.cursor()
    
    # This Function store the register query.

    def registration(self,customer_id,customer_name,customer_age,customer_contactNum,customer_state,customer_city,customer_email,customer_balance,customer_password):
        try:
            self.cursor.execute(
                            "INSERT INTO customer (CustomerID, Cname, CAge, CContactNum, State, City, Email, Balance, Password)"
                            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s);",
                            (customer_id, customer_name, customer_age, customer_contactNum, customer_state, customer_city, customer_email, customer_balance, customer_password))
            self.connection.commit()
            display.print_c("\nYou have successfully registered\n","green")

        except IndexError:
            display.print_c("Everything is now printed.","green")

        except mysql.connector.IntegrityError:
            print("\n[Customer ID is already taken]")
            self.connection.rollback()

    # This Function store the retrieve cart query.
    def retrieve_cart(self):
        display.clear_screan()
        display.logo()

        try:
            self.cursor.execute('select * from cart')                                                                      #Command for subqueries
            cart = self.cursor.fetchall()
            customer = self.cursor.fetchall()
            print("Records:", self.cursor.rowcount)                                                                        #Prints the records of the cart table
            headers = [i[0] for i in self.cursor.description]                                                              #loop for column names
            rows = [[str(cell) for cell in record] for record in cart]                                                     #prints each row
            display.clear_screan()
            print(tabulate(rows, headers=headers, tablefmt='grid'))                                                        #call tabulate import, format table display and print
            
        except IndexError:
            display.print_c("Everything is now printed","green")

    # This Function store the add to cart query.
    def add_cart(self, product_id, customer_id):
        try:
            self.cursor.execute("SELECT MAX(cartID) FROM cart")
            cartIDMax = self.cursor.fetchone()[0]
            if cartIDMax is None:
                cartID = 0
            else:
                cartID = cartIDMax + 1
            # Fetch item details from inventory
            self.cursor.execute("SELECT description, type, price, expirationdate, quantity  FROM inventory WHERE ProductID = %s", (product_id,))  # Fetch item details from inventory
            item = self.cursor.fetchone()

            if item:
                description, item_type, price, expiration_date, quantity = item #used for tuple checking, most of these arent used, quantity > 0 wont work if there are no other variables
                if quantity > 0:                                                                                                                            
                    self.cursor.execute("INSERT INTO cart (cartID, ProductID, description, type, expirationdate, price, Quantity, CustomerID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (cartID, product_id, item[0], item[1], item[3], item[4], 1, customer_id))  #adds item to cart
                    self.cursor.execute("UPDATE inventory SET Quantity = Quantity - 1 WHERE ProductID = %s", (product_id,))
                    self.connection.commit()
                    display.clear_screan()
                    display.print_c("Item added to cart successfully","green")
                else:
                    display.clear_screan()
                    display.print_c("Item out of stock","red")
            else:
                display.clear_screan()
                display.print_c("Item not found in inventory","red")
        except mysql.connector.Error as err:
            print("Error:", err)

    def remove_item(self, product_id, cart_id):
        try:
            self.cursor.execute( "DELETE FROM cart WHERE ProductID = %s AND cartID = %s", (product_id, cart_id,))
            self.cursor.execute( "UPDATE inventory SET Quantity = Quantity + 1 WHERE ProductID = %s", (product_id,))
            self.connection.commit()
            display.clear_screan()
            display.print_c("Item deleted from cart successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)

    # This Function stores the clear cart query.
    def exit_program_clear_cart(self):
            self.cursor.execute('delete from cart') 
            self.connection.commit() 
            display.print_c("\nCart Cleared!","green")

    # This Function store the retrieve inventory.
    def retrieve_inventory(self):
        try:
            self.cursor.execute("SELECT MAX(cartID) FROM cart")
            cartIDMax = self.cursor.fetchone()[0]

            if cartIDMax is None:
                display.print_c("There are no items!","red")
                
            self.cursor.execute('SELECT * FROM inventory')                                                                 
            inventory = self.cursor.fetchall()
            customer = self.cursor.fetchall()
            print("Records:", self.cursor.rowcount)                                                                        #Prints the records of the cart table
            headers = [i[0] for i in self.cursor.description]                                                              #loop for column names
            rows = [[str(cell) for cell in record] for record in inventory]                                                #prints each row
            display.clear_screan()
            print(tabulate(rows, headers=headers, tablefmt='grid'))                                                        #call tabulate import, format table display and print   
        #Catches a Index inbound error
        except IndexError:
            display.print_c("Everything is now printed","green")

    def checkout(self):
        display.clear_screan()
        display.logo()
        try:
            self.cursor.execute("SELECT SUM(price) AS Total FROM cart")
            total = self.cursor.fetchone()[0]
            if total is not None:
                total = float(total)                                                      #set total as float, total from mysql is set as decimal.decimal and has conflicts with float in python which results to errors when trying to do arithmetic calculations with them
                print("Total price in the cart: P",total)

                while True:
                    payment = float(input("Enter you payment here: "))

                    if payment < total:
                        print("\nPlease enter correct amount.")
                    
                    else:

                        print("Change: P",total - payment)
                        self.cursor.execute('SELECT * FROM cart')
                        cart = self.cursor.fetchall()
                        headers = [i[0] for i in self.cursor.description]                                                              
                        rows = [[str(cell) for cell in record] for record in cart] 
                        print("\nReceipt:")
                        print(tabulate(rows, headers=headers, tablefmt='grid'))

                        self.cursor.execute('delete from cart') 
                        self.connection.commit()
                        print("\nCart Cleared!")
                        break
            else:
                print("No items in the cart.")
                time.sleep(delay)
                display.clear_screan()                                                  
        except mysql.connector.Error as err:
            print("Error:", err)

    def category_search(self, type_id):
        try:
            self.cursor.execute( "SELECT * FROM inventory WHERE type = %s", (type_id,))                                                          #by adding ',' type id can now be passed as a tuple.
            inventory = self.cursor.fetchall()
            headers = [i[0] for i in self.cursor.description]                                                              
            rows = [[str(cell) for cell in record] for record in inventory]
            display.clear_screan()
            print(tabulate(rows, headers=headers, tablefmt='grid'))
        except mysql.connector.Error as err:
            print("Error:", err)

    def exit_program_clear_cart(self):
            self.cursor.execute('delete from cart') 
            self.connection.commit()
            display.clear_screan() 
            display.print_c("\nCart Cleared!","green")


    #Customer Functions used in Menus class
    def customerRegistration(self):
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
        self.registration(customer_id,customer_name,customer_age,customer_contactNum,customer_state,customer_city,customer_email,customer_balance,customer_password) 
    
    def login(self):
        display.clear_screan()
        display.logo()
        customer_id = int(input("Enter Customer ID: "))
        customer_password = input("Enter Customer Password: ")
        display.clear_screan()
        self.cursor.execute("SELECT * FROM customer WHERE customerid = %s AND password = %s", (customer_id , customer_password))
        return self.cursor.fetchone()
    
    def addtocart(self):
        try:
            display.clear_screan()
            display.logo()
            product_id = input("Enter Product ID: ")
            customer_id = input("Enter Customer ID: ")
            if product_id == "" or customer_id == "" :
                display.print_c("ID is required, Please try again","red")
                time.sleep(delay)
                display.clear_screan()
            else:
                self.add_cart(int(product_id), int(customer_id))
        except ValueError:
            display.print_c("\n!Enter a valid value","red")
            time.sleep(delay)
            display.clear_screan()

    def removeFromCart(self):
        try:
            display.clear_screan()
            display.logo()
            self.retrieve_cart()
            product_id = input("Enter Product ID: ")
            cart_id = input("Enter Cart ID: ")
            if product_id == "" or cart_id == "" :
                display.print_c("\nID is required, Please try again","red")
                time.sleep(delay)
                display.clear_screan()
            else:
                self.remove_item(int(product_id), int(cart_id))
        except ValueError:
            display.print_c("\n!Enter a valid value","red")
            time.sleep(delay)
            display.clear_screan()
    
    def showCategory(self):
        display.clear_screan()
        display.logo()
        self.cursor.execute('SELECT DISTINCT(type) FROM inventory')
        types = self.cursor.fetchall()
        valid_types = [index[0].lower() for index in types]
        headers = [i[0] for i in self.cursor.description]
        rows = [[str(cell) for cell in record] for record in types]
        print(tabulate(rows, headers=headers, tablefmt='grid'))
        type_id = input("Enter a category here: ").lower()
        if type_id not in valid_types:
            display.print_c("Category not found","red")
            time.sleep(delay)
            display.clear_screan()
        else: 
            display.clear_screan()
            self.category_search(type_id)

    

        

        


    