def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    max_count = 0
    current_count = 0

    for digit in binary:
        if digit == '1':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count

num = int(input("Enter your number: "))
result = longest_consecutive_ones(num)
print("Longest consecutive 1’s length :", result)
