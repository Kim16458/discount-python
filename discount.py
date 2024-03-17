

def calculate_discount():
 original_price = int(input("Enter the original price of item:"))
 discount_percent = float(input("Enter percentage discount offered(as a decimal):"))
 discount_decimal = discount_percent/100

 if discount_percent > 20.00: 
      print(original_price - original_price*discount_decimal)
 else:
      print(original_price)

new_price = calculate_discount()


    

