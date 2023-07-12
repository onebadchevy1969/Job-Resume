import random, time, sys
input = input('Rock, Paper, or Scissors? ') #asks if what they want to choose
input = str(input)
input = input.lower() #turns the input into all lower case
number = random.randint(1, 3) #1 is rock, 2 is paper, 3 is scissors
#lines 7 to 14 converts user input into number 1 to 3 (like in the number variable) the else statment is in case someone inputs something that is not rock, paper, or scissors
if input == 'rock':
    input = 1
elif input == 'paper':
    input = 2
elif input == 'scissors':
    input = 3
else:
    print('Sorry I dont know what that is...')

#lines 16 to 41 takes the number vaules and compares the user input to the computer generated number
if number == 1 and input == 1:
    print('We both got rock! It is a tie!')
elif number == 1 and input != 1:
    print('I got rock!')
    if input == 3:
        print('So I win!')
    else:
        print('So you win!')
elif number == 2 and input == 2:
    print('We both got paper! It is a tie!')
elif number == 2 and input != 2:
    print('I got paper!')
    if input == 1:
        print('So I win!')
    else:
        print('So you win!')
elif number == 3 and input == 3:
    print('We both got scissors! It is a tie!')
elif number == 3 and input != 3:
    print('I got scissors!')
    if input == 2:
        print('So I win!')
    else:
        print('So you win!')
