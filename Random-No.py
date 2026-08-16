import random
#Generate a Number Between 1 to 100
No =  random.randint(1,100)
print("Guess Number between 1 to 100")

while True :
    guess = int(input("Guess Number :"))

    if guess<No:
        print("Too Low ! try again....")
    elif guess>No:
        print("Too High ! try again...")
    else:
        print("Congratulation you got it....")

