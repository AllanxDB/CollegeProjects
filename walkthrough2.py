name = input("What is your name? ")

print("Hello, " + name + "!")

print("Per the Cleveland Clinic, you should eat 2400 calories per day.")
Calories = input("how many calories do you eat per day? ")
Calories = int(Calories)
CaloriesRemaining = 2400 - Calories
print("You have ", + CaloriesRemaining , " calories remaining for the day.")

print(name,type(name))
print(Calories,type(Calories))

players = {"Alice": 10, 
           "Bob": 15, 
           "Charlie": 20
           }
print(players)
print(type(players))
print(players["Alice"])
print(type(players["Alice"]))