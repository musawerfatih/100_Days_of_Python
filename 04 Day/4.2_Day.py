# Who will pay the bill

import random
names_str = input("Types name seperated by comma: ")
namesList = names_str.split(',')

ranNo = random.randint(0,(len(namesList)-1))
print(f"{namesList[ranNo]} is supposed to pay.")
