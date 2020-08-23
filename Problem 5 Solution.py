def next_pallindrome(n):
    n = n+1
    while not is_pallindrome(n):
        n += 1
    return n
def is_pallindrome(n):
    return str(n) == str(n)[::-1]
if __name__ == "__main__":
    size = int(input("Enter the size of your list\n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of the list\n")))
    print(f"You have entered {num_list}")
    new_list = []
    for element in num_list:
        if element > 10:
            n = next_pallindrome(element)
            new_list.append(n)
        else:
            new_list.append(element)
    print(f"Output list: {new_list}")