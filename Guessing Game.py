import random, time, sys
ran_numb = random.randint(1,100) #call for a random number to be generated between the two vaules stated
print('I am thinking of a number between 1 and 100, you have three guesses ')
Guess_try = 3 #Number of time you can guess, when this goes down to zero the program will close!
print(ran_numb)
for guess1 in range(0,3): #the game will run, as long as you have guesses remaining, once you run out, the program will close.
    print('Guesses remaining ' + str(Guess_try))
    guess1 = input('What is your guess?' ) #asks the user to enter their number
    try:

        if int(guess1) > ran_numb:
            print('Sorry, that number is to high!')
            Guess_try = Guess_try - 1 #Subtracts one guess each time you get the number wrong

        elif int(guess1)  == ran_numb:
            print('Wow! You guessed it in one try! ')
            exit()

        elif int(guess1)  < ran_numb:
            print('Wrong! You need to go higher! ')
            Guess_try = Guess_try - 1 #Subtracts one guess each time you get the number wrong

    except ValueError: #This is here incase you enter a number bigger or less than the alotted range, this is also incase you enter words and not a number!
        print('Sorry I have no idea what ' + guess1 + ' is! ')
