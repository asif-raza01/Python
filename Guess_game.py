import random

x=random.randint(1,100)
print(x)
guess=int(input("Enter the number you guessed"))

attempt=1

while(guess!=x):
    attempt+=1
    if(guess>x):
        print("guess Lower Number")
        guess=int(input("Enter the number you guessed"))
    else:
        print("guess higher number")
        guess=int(input("Enter the number you guessed"))

print("number of attempts you took:",attempt)

