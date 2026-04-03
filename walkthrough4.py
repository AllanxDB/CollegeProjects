year = int(input("what year is your truck? (Enter 0 to exit)"))


while year != 0:
   
    if(year <= 2010 or year >= 2021):
        print("we only buy trucks manufactured between 2010 and 2021")
    elif year <=2015:
        print("we will pay you $15000 for your truck")
    else:
        print("we will pay you $22000 for your truck")

    year = int(input("what year is your truck? (Enter 0 to exit)"))