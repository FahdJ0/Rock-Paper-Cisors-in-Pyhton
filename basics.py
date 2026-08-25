import random
computer_choice = random.choice(['r', 'p', 's'])
r = 'rock'
p = 'paper'
s = 'scissor'

user_choice = input("Choose bewteen rock (r), paper (p) and scissors (s) : ")
if user_choice == r and computer_choice == s:
    print("User won ! ")
elif user_choice == p and computer_choice == r:
    print("User won ! ")
elif user_choice == s and computer_choice == p:
    print("User won !")
elif user_choice == computer_choice:
    print("Equality")
else :
    print("Computer won ! ")
print(f"The computer choosed {computer_choice} and you choosed {user_choice}")