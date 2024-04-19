import mysql.connector
from tabulate import tabulate
from Display import Display

display = Display()

class Manager:
    
    def __init__(self):                                                                                                    #constructor
        self.connection = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")  #connection attribute
        self.cursor = self.connection.cursor()

    # this function stores the add item query
    def add_item(self, productID, product_description, product_type, price, date, quantity):
        try:
            self.cursor.execute("INSERT INTO inventory (ProductID, Description, Type, Price, ExpirationDate, Quantity) "
                            "VALUES (%s, %s, %s, %s, %s, %s);",
                            (productID, product_description, product_type, price, date, quantity))
            self.connection.commit()
            display.print_c("\nAdded to inventory successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)
    # this function stores the remove item query
    def remove_item(self, productID):
        try:
             self.cursor.execute("DELETE FROM inventory "
                                "WHERE productID = %s;",
                                 (productID,))
             self.connection.commit()
             display.print_c("\nItem removed successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)
    # this function stores the update price query
    def update_price(self, productID, price):
        try:
            self.cursor.execute("UPDATE inventory "
                            "SET price = %s "
                            "WHERE productID = %s;",
                            (price, productID))
            self.connection.commit()
            display.print_c("\nPrice Updated","green")
        except mysql.connector.Error as err:
            print("Error:", err)
    

    #Manager Functions
    #this function is for manager login
    def login(self):
        display.clear_screan()
        display.logo()
        manager_id = int(input("Enter Manager ID: "))
        manager_password = input("Enter password: ")
        display.clear_screan()
        self.cursor.execute("SELECT * FROM manager WHERE managerid = %s AND password = %s", (manager_id, manager_password))
        return self.cursor.fetchone()
    
    #this function is for add item to inventory
    def add_item_to_inventory(self):
        display.clear_screan()
        display.logo()
        print("\n[ ADD TO INVENTORY ]\n")
        productID = int(input("Enter Product ID: "))
        product_description = input("Enter Product Description: ")
        product_type = input("Enter Product type: ")
        price = float(input("Enter Product price: "))
        date = input("Enter Expiration Date: ")
        quantity = int(input("Enter Quantity: "))
        self.add_item(productID,product_description,product_type,price,date,quantity)

    #this function is remove items to inventory
    def remove_expired_items_from_directory(self):
        display.clear_screan()
        display.logo()
        print("\n[ REMOVE ITEM FROM INVENTORY ]\n")
        productID = int(input("Enter Product ID: "))
        self.remove_expired_items_from_directory(productID)
    
    #this function is for update item price to inventory
    def update_item_price(self):
        display.clear_screan()
        display.logo()
        print("\n[ UPDATE PRICE ]\n")
        productID = int(input("Enter Product ID: "))
        price = float(input("Enter Updated Product price: "))
        self.update_item_price(productID, price)


            
    
        


