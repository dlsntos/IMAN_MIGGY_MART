import mysql.connector
from tabulate import tabulate
from Display import Display

display = Display()

class Customer:
    

    def __init__(self):                                                                                                    #constructor
        self.connection = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")  #connection attribute
        self.cursor = self.connection.cursor()
    
    def customer_registration(self,customer_id,customer_name,customer_age,customer_contactNum,customer_state,customer_city,customer_email,customer_balance,customer_password):
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

    def retrieve_cart(self):
        try:
            self.cursor.execute('select * from cart')                                                                      #Command for subqueries
            cart = self.cursor.fetchall()
            customer = self.cursor.fetchall()
            print("Records:", self.cursor.rowcount)                                                                        #Prints the records of the cart table
            headers = [i[0] for i in self.cursor.description]                                                              #loop for column names
            rows = [[str(cell) for cell in record] for record in cart]                                                     #prints each row
            display.clear_screan()
            print(tabulate(rows, headers=headers, tablefmt='grid'))                                                        #call tabulate import, format table display and print
            
        #Catches a Index outbound exception
        except IndexError:
            display.print_c("Everything is now printed","green")

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
                description, item_type, price, expiration_date, quantity = item                                                                                 #tuple checking, most of these arent used, quantity > 0 wont work if there are no other variables
                if quantity > 0:                                                                                                                            
                    self.cursor.execute("INSERT INTO cart (cartID, ProductID, description, type, expirationdate, price, Quantity, CustomerID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (cartID, product_id, item[0], item[1], item[3], item[4], 1, customer_id))  #adds item to cart
                    self.cursor.execute("UPDATE inventory SET Quantity = Quantity - 1 WHERE ProductID = %s", (product_id,))
                    self.connection.commit()
                    display.clear_screan()
                    display.print_c("Item added to cart successfully","green")
                else:
                    display.clear_screan()
                    display.clear_screan()
                    display.print_c("Item out of stock","red")
            else:
                display.clear_screan()
                display.clear_screan()
                display.print_c("Item not found in inventory","red")
        except mysql.connector.Error as err:
            print("Error:", err)

    def remove_item(self, product_id, cart_id):
        try:
            # Delete item from cart
            self.cursor.execute( "DELETE FROM cart WHERE ProductID = %s AND cartID = %s", (product_id, cart_id,))
            self.cursor.execute( "UPDATE inventory SET Quantity = Quantity + 1 WHERE ProductID = %s", (product_id,))
            self.connection.commit()
            display.clear_screan()
            display.print_c("Item deleted from cart successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)

    def retrieve_inventory(self):
        try:
            self.cursor.execute("SELECT MAX(cartID) FROM cart")
            cartIDMax = self.cursor.fetchone()[0]

            if cartIDMax is None:
                print("There are no items!")
                
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
            display.print_c("Everything is now printed","red")

    def checkout(self):
        try:
            self.cursor.execute("SELECT SUM(price) AS Total FROM cart")
            total = self.cursor.fetchone()[0]
            total = float(total)                                                      #set total as float, total from mysql is set as decimal.decimal and has conflicts with float in python which results to errors when trying to do arithmetic calculations with them
            print("Total price in the cart: P",total)

            while True:
                payment = float(input("Enter you payment here: "))

                if payment < total:
                    display.clear_screan()
                    print("\nPlease enter correct amount.")
                
                else:
                    display.clear_screan()
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

        except mysql.connector.Error as err:
            print("Error:", err)

    def category_search(self, type_id):
        try:
            self.cursor.execute("SELECT * FROM inventory WHERE type = %s", (type_id,))
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
            display.print_c("\nCart Cleared!","green")


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
        try:
            self.cursor.execute("SELECT SUM(price) AS Total FROM cart")
            total = self.cursor.fetchone()[0]
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

        except mysql.connector.Error as err:
            print("Error:", err)

    def category_search(self, type_id):
        try:
            self.cursor.execute( "SELECT * FROM inventory"
                                ,"WHERE type = %s", (type_id,))                                                          #by adding ',' type id can now be passed as a tuple.
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
            display.print_c("\nCart Cleared!","green")

        


    