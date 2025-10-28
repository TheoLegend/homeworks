def reverse_bits(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    reversed_number = int(reversed_binary, 2)
    return reversed_number

def display_binary(n):
    binary = bin(n)[2:]
    return binary

def get_input():
    num = input("Enter your original number: ")
    if not num.isdigit():
        print("Invalid input. Please enter a positive integer.")
        return None
    return int(num)

def main():
    number = get_input()
    if number is None:
        return
    original_binary = display_binary(number)
    reversed_number = reverse_bits(number)
    reversed_binary = display_binary(reversed_number)
    print("Original Number:", number)
    print("Original Binary:", original_binary)
    print("Reversed Binary:", reversed_binary)
    print("Reversed Number:", reversed_number)

main()
