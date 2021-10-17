# A program to play a game of "Guess the Number"

#define function
def play_guess_the_number():

    from random import randrange

    #get min and max from user
    print(f"Please enter the minimum value")
    u_min = int(input())
    print(f"Please enter the maximum value")
    u_max = int(input())

    #pc chooses a random number within user's range
    pc_num = (randrange(u_min, u_max, 1))
    print(f"I am thinking of a number between {u_min} and {u_max}.")
    print(f"Can you guess what it is?")

    #guessing process begins
    u_guess = int(input())
    while u_guess != pc_num:
        if u_guess > pc_num:
            print(f"Your guess is too high.")
        elif u_guess < pc_num:
            print(f"Your guess is too low.")
        else:
            print(f"this shouldn't happen")
        print(f"Try again!")
        u_guess = int(input())
    print(f"Congratulations! You guessed my number!")

play_guess_the_number()
