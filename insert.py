# # # # # # thislist = ["bed","table"]
# # # # # # print(thislist[0])

# # # # # thislist = ["banana","apple"]
# # # # # print(thislist[1])

# # # # # thislist = ["dilmaya", "nita", "soni"]
# # # # # thislist[2] = "binita"
# # # # # print(thislist)

# # # # # thislist = ["Australia","usa","canada"]
# # # # # thislist.append("countrty")
# # # # # print(thislist)

# # # # thislist = ["Jacket", "Socks", "shorts"]
# # # # thislist.insert(2,"shoes")
# # # # print(thislist)

# # # # thislist = ["Suraj", "sonam", "rupak", "nita"]
# # # # thislist.remove("nita")
# # # # print(thislist)

# # # thislist = ["Hostel", "house", "hotel"]
# # # thislist.pop(2)
# # # print(thislist)

# # person = {"name": "Alice", "age": 25}
# # age = person.pop("name") 
# # print(person)
# # last ko remove garne ani name halasi name remove,
# # gararw age ko output aauxa, pop last bata remove hunxa () yesari khali xdahyo avne

# a = ["alex", "suraj", "hari"]
# del a[2]
# print (a)
# delete garne 2 garesi hari delete vayo, o garda alex deleete hunxa, output ma

# data = {
#     "Name": "Nita",
#     "age" : "23",
#     "contact" : 9812342727,
# "city" : {
#     "Nepal": "Morang",
# }
# }
# print(data["city"]["Nepal"])


# data = [
#     {"Name":"Priya","Age":"20"},
#     {"Name":"Simon","Age":"18"},
#     {"Name":[{"Username":"Admin","Address":["ktm"]}]}
# ]
# print(data[2]["Name"][0]["Address"][0])

# # print garda [] yo bracket vayasi 0 vayo ani [] 
# # vitra sabai 0 ma hunxa ani feri brackrt vitra vayasi arko [] huda 0 vitra 0 hunxa

# data = [
#     [{"name":"sita","city":"ktm"}],
#     [{"name":"ram","city":"brt"}],
# ]
# print(data[1][0]["name"])
# [] vayasi arko {} huda ni 0 ko 0 nai hunxa

# data = {
#     "users":[
#         {"name":"ram","address":"ktm"},
#     ],
#     "students":[
# #         {"name":"sita","address":"brt"},
# #     ]
# # }
# # print(data["students"][0]["address"])

# # students vitra [] vayako la 0 ma vayo ani 0 vitra ko address print garda brt aauxa

# a=6
# b=7
# c=a
# print(a is c)
# print(a is not c)
# print(a==c)

# true, false aauxa output a rw c same ho so true

# data=["ram","sita"]
# # print("ram in data")
# # print("ram is not in data")

# #wap to enter five subject marks and calculate total, average and percentage.
# nepali =int(input("Enter nepali marks:"))
# Math =int(input("Enter math marks:"))
# science =int(input("Enter science marks:"))
# english =int(input("enter english marks:"))
# total = nepali + Math + science + english
# per =total/4
# print("Total marks:",total)
# print("Percentage:",per)

# #wap to enter rupees and convert it into dollars.
# paisa =int(input("paisa"))
# amount =paisa/140
# print(amount)

#p,t,r = Enter principle, time and rate
# p =20
# t =67
# r =56
# si =(p * t * r)/100
# print("simple interest=",si)

# x =5
# y =8
# # if x>y:
# #      print("x is greater than y")
# # else:
# # #     print("x is not greater than y")     

# # # # WAP to enter two person's age and print who is older. 
# # ram = input("ram age:")
# # shyam = input("shyam age:")
# # # if ram>shyam:
# # #      print("ram is greater than shyam")
# # # else:
# # #     print("shyam is not greater than ram")     

# # nita =input("nita age:")
# # rita =input("rita age:")
# # if nita>rita:
# #     print("nita is greater than rita")
# # else:
# #     print("rita is not greater than nita")    

# # simon =input("simon age:")
# # priya =input("priya age:")
# # if simon>priya:
# #     print("simon is greater than priya")
# # else:
# #     print("priya is not greater than simon")

# x =89
# y =76
# # z =67
# # if z>y and y>z:
# #     print("z is greater than y and x")
# # elif y>x and y>z:
# #     print("y is greater than x and z")
# # else: 
# #     print("x is greater than z and y")     

# x =4
# y =34
# u =23
# z =34
# if x>y and u>z:
#     print("x is greater than y,u and z")
# elif y>x and z>u:
#     print ("y is greater than x,u and z")
# elif u>x and y>z:
#     print("u is greater than x,y and z") 
# else:
#     print("z is greater than x,u and y")           

# num =10
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")    

#WAP to enter any number and check whether bit is divisible by 3 and 5.
# num =18
# if num%4==0 and num%6==0:
#     print("divisible by 4 and 6")
# else:
    # print("not divisible by 4 and 6")    

#pre>=35 and pre<50 ->C
# #pre>=50 and pre<65 ->B   (Question)
# #pre>=65 and pre<80 ->A
# #pre>=80 ->A+

# percentage =int(input("Enter student percentage"))
# if percentage >= 35 and percentage <50:
#     print("sita")
# elif percentage >= 50 and percentage <65:
#     print("ram")   
# elif percentage >= 65 and percentage <80:
#      print("shyam")
# elif percentage >= 80: 
#      print("gita")   
# else:
#     print("f")          

# Username="admin"
# password="admin123"
# if Username=="admin" and password=="admin123":
#       print("login successfull")
# else:
#     print("Login Failed")      

# username = "admin"
# password = "admin123"
# if username =="admin":
#     if password=="admin123":
#         print("Login Sucessfull")
#     else:
#        print("Incorrect Password")
# else:
#     print("Username not found")   

#TOTAL QUANTITY:
# print("welcome..............To.......Computer..........Bajar")
# print("1. DELL(Rs:200000) 2. HP(Rs.250000) 3.Apple(Rs. 350000)")
# option =int(input("Select Your option:"))
# if option==1:
#     qu =int (input("Enter Quantity:"))
#     name =input("Enter your name:")
#     phone =input("Enter your phone number:")
#     Total=200000*qu
#     print("Hello{Name}")
#     print(f"Total amount: {Total}")
# elif option==2:
#     qu =int(input("Enter Quantity:"))
#     name =input("Enter your name:")
#     phone =input("Enter your phone number:")
#     Total=250000*qu
#     print(f"Total amount: {Total}")
# elif option==3:  
#     qu = int(input("Enter quantity:"))
#     name =input("Enter your name")
#     phone =input("Enter your phone number")
#     Total=350000*qu
#     print(f"Total amount: {Total}")
# else:
#     print("Invalid Option")

# #ATM WITHDRAW CODE:
# print("=========Welcome to ATM======")
# pin =int(input("Enter your pin:"))
# if pin==1234:
#      amount=10000
#      print("1. withdraw 2. Balanace Enquiry")
#      option =int(input("select your option:"))
#      if option==1:
#         namount=int(input("Enter amount to withdraw:"))
#         if namount>amount:
#             print("insufficiant balance:")
#         else:
#             wamount =amount - namount
#             print(f"Please collect your cash")
#             print(f"Withdraw amount is: {namount}")
#             print(f"Your remaining balance is:{wamount}")
#      elif option==2:
#          print(f"your balance is:{amount}")
#      else:
#             print("Invalid option")
# else:
#                 print("incorect pin")   

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