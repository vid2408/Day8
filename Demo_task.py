class Person:
    
    def __init__(self, Product_Name, Product_CostPrice,Product_SalesTax_Percentage,Country):
        self.Product_Name = Product_Name
        self.Product_CostPrice = Product_CostPrice
        self.Product_SalesTax_Percentage = Product_SalesTax_Percentage
        self.Country = Country

    
    @classmethod
    def get_user_input(self):
        NoC = input('Number_of_country')
        while(NoC >= 0):
            try:
                Product_Name = input('Enter first name: ')
                Product_CostPrice = input('Enter last name')
                Product_SalesTax_Percentage = input('Enter last name')
                Country = input('Enter last name')
                
            except:
                print('Invalid input!')
                continue

#creating a person object and returning their full name
person3 = Person.get_user_input()
person3.show_full_name()


import csv

class Product():
    
    with open('sales_tax2.csv','w',newline='') as f:
        thewriter = csv.writer(f)
        
        thewriter.writerow(['Product_Name', 'Product_CostPrice ', 'Country', 'Product_SalesTax', 'Product_FinalPrice'])
        


        def __init__(a, Product_Name, Product_CostPrice,Product_SalesTax_Percentage,Country):
            a.Product_Name = Product_Name
            a.Product_CostPrice = Product_CostPrice
            a.Product_SalesTax_Percentage = Product_SalesTax_Percentage
            a.Country = Country
         
        def calculation(Product_Name, Product_CostPrice,Product_SalesTax_Percentage,Country):
            product_sales_tax = 10
            number_of_products = int(input('Enter the number of products'))
            for i in range(number_of_products):
                Product_Name = input("Enter product name: ")
                Product_CostPrice = input("Enter product cost price: ")
                Product_SalesTax_Percentage = input("Enter product sales tax percentage: ")
                Country = input("Enter the country name:")
                product_final_price = Product_CostPrice * product_sales_tax

# dave = Product(Product_Name, Product_CostPrice, Product_SalesTax_Percentage,Country)
