
      #Write a program to ktm 27 km and 5-5 distance from kalanki to chabil rs. 20 rupees, 
      #kalanki to buspark rs 20 rupees, ktm to bkt rs.20 ruppess, 
      #ktm ko pokhara rs.20 rupees, and ktm to lalitpur rs. 20 in ticket,in python......
      #(ktm(27 km)) #5-5 distance 1. kalanki to chabile rs.20,
       #jastai 5 wota banaune 20 rs vada ko...
    #=ANS
       #-Total KTM distance-27 km
       #-fare is Rs. 20 for every 5 km
       #Routes and each segment ticket = Rs.20

Ticket_price = 20
routes = {
   "kalanki to Chabahil":5,
   "kalanki to Bus park":5,
   "KTM to Bhaktapur":5,
   "KTM to pokhara":5,
   "KTM to lalitpur":5
}
total_distance = 27
print("kathmanu Total Distance:", total_distance, "km")
print("Ticket price per 5 km: Rs.", Ticket_price)
print("\nRoutes Ticket Details:\n")
for routes, distance in routes.items():
    ticket = distance // 5
    fare = ticket * Ticket_price
    print(routes, ":", fare, "rupees")
