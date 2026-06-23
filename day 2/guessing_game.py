import random
secret = random.randint(1,50)
while True:
    guess = int(input("tell a number"))
    if guess == secret:
        print("your number if correct")
        break;
    elif guess > secret:
        print("your number is high")
    else:
        print("your number is low")