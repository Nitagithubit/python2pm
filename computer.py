    
# #welcome to============computer bazar====
# 1. Dell(Rs:20000)
# 2. Toshiba(Rs:30000)
# 3.MAC(Rs:50000)
# enter option
# Delivery option:
#  1. Home(Rs:1000)
#  2.Pickup Free

#  Packing Option
#   1. Plastic bag(Rs:1000)
#    2. Bag(Rs:2000)
#     3. Gift box(Rs:5000)
    
#     location:
#     1. KTM(Rs 13% tax)
#      2. BKT(Free)
#       3.Lalitpur(Free)

#       Username?
#       Product name?
#       Quantity?
#       Tax Amount?
        # Grand Total?
  #ANS:

print("=======Welcome to computer bazar========")
print("1. Dell(Rs.20000) 2.Toshiba(Rs:30000) 3. MAC(5000)")
option =int(input("Select your option: "))
productname=''
dell_price=0
hp_price=0
apple_price=0
if option == 1:
    qu =int(input("Enter quantity"))
    dell_price = qu*20000
    productname='Dell'
       
elif option == 2:    
    qu =int(input("Enter quantity"))
    Toshiba_price = qu*30000
    productname='Toshiba'

elif option ==3:
    qu =int(input("Enter quantity"))
    MAC_price = qu*50000
    productname='MAC'    

else:
    print("Invalid")    

print("Delivery option: 1.Home(Rs.1000) 2.Store pickup(Rs.0)")
Delivery_option =int(input("Select your delivery option: "))
Delivery_price =0

if Delivery_option==1:
    Delivery_price=1000


print("packing 1. PLastic(Rs:100) 2. Bag(Rs:2000) 3. Gife box(Rs:3000)")
packing_price=0
packing_option=int(input("selcet your packing option:"))
if packing_option==1:
    packing_price=1000
elif packing_option==2:
     packing_price=3000

print("location 1.KTM(Rs. 13%) 2.ltp(Rs. 0) 3.BkT(Rs. 0)")

total = dell_price + hp_price + apple_price
tax_amount=0
location_option=int(input("Select your option"))
if location_option==1:
    tax_amount= total*0.13

name =input("Enter your name:")
grand_total=total + Delivery_price + packing_price + tax_amount

print("=========Invoice=====")
print("Customer Name:",name)
print("Product Name:",productname)
print("product price:",total)
print("Delivery Price:",Delivery_price)
print("packing price:",packing_price)
print("Tax Amount:",tax_amount)
print("Grand total:",grand_total)




