# Ask for the user name and find its length

# First Way
# print(len(input("what is your name? ")))

# Second way
name = input("What is your name? ")
count = 0
for ch in name:
    count+=1
print(count)
