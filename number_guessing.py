print(f'''

     Guess the number on the card from 1 to 100
                .----------------. 
                | .--------------. |     
                | |    ______    | |
                | |   / _ __ `.  | | 
                | |  |_/____) |  | |
                | |    /  ___.'  | |
                | |    |_|       | |
                | |    (_)       | |
                | |              | |
                | '--------------' |
                '----------------' 
Type "easy" for 10 attempts, or type "hard" for 5 attempts:
''')

from random import randint
secret = randint(1, 100)
level = input()


def game():
    if level == "hard":
        attempts = 5
    else:   
        attempts = 10
    while attempts > 0:
        print(f"you have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == secret:
            print(f"You got it! The answer is {secret}")
            return 1
        elif guess > secret:
            print("Too high, try again.")
            attempts -= 1
        else:
            print("Too low, try again.")
            attempts -= 1
    return 0 

if game() == 1:
    print(f"You win!\nThe number was {secret}")
else:
    print(f"You lose.\n The number was {secret}")
       
