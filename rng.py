import random
import math

# Generate a random number between 1 and 50
num = random.randint(1, 50)
print("Random number:", num)

# Use modulo to check if the number is even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Use a math function: square root
sqrt_value = math.sqrt(num)
print("The square root of", num, "is", round(sqrt_value, 2))