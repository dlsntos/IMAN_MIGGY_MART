import mysql.connector
from tabulate import tabulate
from Display import Display

display = Display()

class Manager:

    def __init__(self):                                                                                                    #constructor
        self.connection = mysql.connector.connect(host="localhost", user="root",password="", database="miggymart")  #connection attribute
        self.cursor = self.connection.cursor()
    #def manager_login(self,manager_id,password):
    def add_item_to_inventory(self, productID, product_description, product_type, price, date, quantity):
        try:
            self.cursor.execute("INSERT INTO inventory (ProductID, Description, Type, Price, ExpirationDate, Quantity) "
                            "VALUES (%s, %s, %s, %s, %s, %s);",
                            (productID, product_description, product_type, price, date, quantity))
            self.connection.commit()
            display.print_c("\nAdded to inventory successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)

    def remove_expired_items_from_directory(self, productID):
        try:
             self.cursor.execute("DELETE FROM inventory "
                                "WHERE productID = %s;",
                                 (productID,))
             self.connection.commit()
             display.print_c("\nItem removed successfully","green")
        except mysql.connector.Error as err:
            print("Error:", err)
    def update_item_price(self, productID, price):
        try:
            self.cursor.execute("UPDATE inventory "
                            "SET price = %s "
                            "WHERE productID = %s;",
                            (price, productID))
            self.connection.commit()
            display.print_c("\nPrice Updated","green")
        except mysql.connector.Error as err:
            print("Error:", err)



            
    
        


