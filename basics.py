import random
secret_number = random.randint(1,100)
guess = int(input("Enter your guess : "))
attempts = 1

while guess != secret_number:
    if guess > secret_number:
        print("Too high ! ")
    else : print("Too low ! ")

    guess = int(input("Try again : "))
    attempts += 1
print(f"You got it ! It took you {attempts} attemps.")