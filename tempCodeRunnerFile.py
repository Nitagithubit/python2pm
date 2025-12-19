
print("kathmanu Total Distance:", total_distance, "km")
print("Ticket price per 5 km: Rs.", Ticket_price)
print("\nRoutes Ticket Details:\n")
for routes, distance in routes.items():
    ticket = distance // 5
    fare = ticket * Ticket_price
    print(routes, ":", fare, "rupees")
