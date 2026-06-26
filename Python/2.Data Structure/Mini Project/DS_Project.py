s = input("Enter a string: ")

count = 0
for i in range(len(s) - 4 + 1):
    if s[i:i+5] == "Alex":
        count += 1

print(count)