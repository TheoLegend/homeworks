# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Two-digit prime numbers are:")

# Loop through two-digit numbers
for n in range(10, 100):
    if is_prime(n):
        print(n, end=" ")
