import random
number = int(input("How many names you want to enter\n"))
First_Name = []
Last_Name = []
for i in range(0,number):
    name = input("Please enter your friend's names\n")
    name = name.split(" ")
    First_Name.append(name[0])
    Last_Name.append(name[1])
jumble = number
print("The Jumbled Names are:")
for i in range(0,number):
    jumble = jumble - 1
    rand = random.randint(0,jumble)
    print(f"{First_Name[i]} {Last_Name[rand]}")
    del Last_Name[rand]