import csv
with open('sales_tax.csv','w',newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['Product_Name', 'Product_CostPrice ', 'Country', 'Product_SalesTax', 'Product_FinalPrice'])
    number_of_products = int(input("Enter the number of products : "))
    product_sales_tax = 10
    for i in range(number_of_products):
        product_name = input("Enter the product name :")
        product_cost_price = input("Enter the cost price :")
        country = input("Enter the country name :")
        product_final_price = product_cost_price * product_sales_tax

        thewriter.writerow([product_name,product_cost_price,country,product_sales_tax,product_final_price])