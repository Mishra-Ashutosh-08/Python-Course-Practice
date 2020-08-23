import random
def guessgame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input("Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input("Enter a smaller number\n"))
            nguess += 1
    return nguess
if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessgame(a, b, actual1)
    actual2 = random.randint(a, b)
    print("Player 2's turn\n")
    g2 = guessgame(a, b, actual2)
    if g1 < g2:
        print("Player 1 won the match\n")
    elif g1 > g2:
        print("Player 2 won the match\n")
    else:
        print("Match ties")
    print(f"The number for player 1 was {actual1} and the number for player 2 was {actual2}")