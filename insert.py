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
p =20
t =67
r =56
si =(p * t * r)/100
print("simple interest=",si)