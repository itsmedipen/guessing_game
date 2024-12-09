###Algorithm
# # I am thinking of a number. Try to guess the number I am thinking: 24 
# # Too Low!!! Guess Again: 50
# # Too High!!! Guess Again: 42
# # Correct you did it. Do you want to play again? [Yes, No]


import random

def guessnumber():
    return random.randint(1,100)

play=True
user_num = int(input("I am thinking of a number. Try to guess the number I am thinking: "))
Counter = 0
total_chance = 3
while play:
    random_num = guessnumber()
    if Counter == total_chance:
        print('Your chance is over')
        message = input('Do you want to play again? [Yes/No]: ')
        if message.upper() == "YES":
            Counter = 0
            random_num = guessnumber()
            user_num = int(input("I am thinking of a number. Try to guess the number I am thinking:"))
            continue
        else:
            play = False
        
            print('Thanks for playing game')
    else:
        if user_num > random_num:
            print('Too high.')
            Counter += 1
            if Counter < total_chance:
                print(f'You have {total_chance-Counter} chance left')
                user_num = int(input('Guess the number: '))
                
            
        
        elif user_num < random_num:
            print('Too low.')
            Counter += 1
            if Counter < total_chance:
                print(f'You have {total_chance-Counter} chance left')
                user_num = int(input('Guess the number: '))

        elif user_num == random_num:
            print('Congratulations! You guess it correctly')
            print('Thanks for playing a game')
            break
    
            
