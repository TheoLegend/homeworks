def find_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

string = input("Enter string: ")
result = find_substrings(string)

for sub in result:
    print(sub)
