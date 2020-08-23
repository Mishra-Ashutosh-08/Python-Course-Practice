print("Enter the numbers of the list\n")
size = int(input("Enter the size of list\n"))
myList = []
for i in range(size):
    myList.append(int(input("Enter the element\n")))
print(f"Your list is {myList}\n")
reverse1 = myList[:]
reverse1.reverse()
reverse2 = myList[::-1]
print(f"My First reversed list of {myList} is {reverse1}\n")
print(f"My Second reversed list of {myList} is {reverse2}\n")
reverse3 = myList[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i]
print(f"My Third reversed list of {myList} is {reverse3}\n")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")