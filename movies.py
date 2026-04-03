age = int(input("How old are you? "))
print(age)

if age <= 0:
    print("You are not born yet!")
    exit()

if age >= 65:
    ticketprice = 6
elif age >= 12:
    ticketprice = 4
else: 
    ticketprice = 10
print("Your ticket price is: ", ticketprice)
