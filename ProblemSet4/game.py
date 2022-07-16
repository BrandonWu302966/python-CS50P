import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break
        else:
            pass
ans = random.randint(1,n)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > ans:
            print("Too large!")
        elif guess < ans:
            print("Too small!")
        elif guess == ans:
            print("Just right!")
            break