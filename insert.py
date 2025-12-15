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

#WAP to enter any number and check whetherbit is divisible by 3 and 5.
# num =18
# if num%6==0 and num%9==0:
#     print("divisible by 6 and 9")
# else:
#     print("not divisible by 6 and 9")    

#pre>=35 and pre<50 ->C
# #pre>=50 and pre<65 ->B   (Question)
# #pre>=65 and pre<80 ->A
# #pre>=80 ->A+

# percentage =int(input("Enter student percentage"))
# if percentage >= 35 and percentage < 50:
#     print("sita")
# elif percentage >= 50 and percentage < 65:
#     print("ram")   
# elif percentage >= 65 and percentage < 80:
#      print("shyam")
# elif percentage >= 80: 
#      print("gita")   
# else:
#     print("f")          

