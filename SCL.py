def find_all_substrings(s):
    length = len(s)
    print("Original string:", s)
    print("Length of string:", length)
    print("Scanning for substrings...\n")
    count = 0
    for start in range(length):
        for end in range(start + 1, length + 1):
            substring = s[start:end]
            print(f"Substring #{count + 1}: '{substring}' (from index {start} to {end - 1})")
            count += 1
    print("\nTotal substrings found:", count)
    print("Mission complete. All fragments decoded.")

user_input = input("Enter a string to scan for substrings: ")
find_all_substrings(user_input)
