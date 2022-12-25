# Love calculator
name1 = input("Enter your name: ").lower()
name2 = input("Enter his/her name: ").lower()

fname = name1 + name2

T = fname.count('t')
R = fname.count('r')
U = fname.count('u')
E = fname.count('e')

L = fname.count('l')
O = fname.count('o')
V = fname.count('v')
E = fname.count('e')

true = T+R+U+E
love = L+O+V+E
strtotal = str(true) + str(love)
total = int(strtotal)

if total > 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print("Your score is {total}, you are alright together.")
else:
    print(f"You have {total}% love.")
