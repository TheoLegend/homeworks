import math

# Function to calculate LCM
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculating LCM
result = lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {result}")
