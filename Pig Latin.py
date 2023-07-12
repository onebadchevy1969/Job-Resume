def Once_More(): # This is a function to see if the user would like to translate more text or not
    again = input("Would you like to translate something else?(Y/N): ") #asks for userinput
    if again.upper() == 'Y': #If the user would like to translate something else, the Pig_Latin function is started again
        Pig_Latin()

    elif again.upper() == 'N': # if the use would not like to translate something else, the program closes after print 'Goodbye!'
        print('Goodbye!')
    else: #This else statement is for if the user inputs something that is not Y or N. The program will say it dose not understand, and then bring the user to the start
        print('I am sorry I do not know what that is, please try again') #of the Once_More function
        Once_More()

def Pig_Latin():
    consonants = ('b', 'c', 'd', 'e', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'h', 'r', 'w', 'y') #this names all the the letters
#that is have 'ay' at the end of the word, after being coverted into Pig Latin
    Pig_Text = [] #this sets up the list to be used later on in the code
    Non_Pig_text = input('What would you like to make in to Pig Latin?: ')
    Non_Pig_text = Non_Pig_text.lower() #Makes Sure The Program Is NOT Case Sensitive
    Non_Pig_text = Non_Pig_text.split()
    for word in Non_Pig_text: #This Breaks The Whole String Down into Separate strings
        if word.isalpha(): #Checks to make sure the Word Starts With a Letter
            if word.startswith(consonants): #Checks to see if the word starts with a consonant
                Pig_Word = word[1:] + word[0] + 'ay' + ' ' #if it does, it takes the first letter in the word and puts it at the end, then puts 'ay' after
                Pig_Text.append(Pig_Word) #adds the translated word into a list

            else: #This is for if the word starts with a vowel
                Pig_Word = word + 'yay ' #it simply adds 'yay ' to the end of the word
                Pig_Text.append(Pig_Word) #adds the translated word into a list

        else: #This else statment is for number and other non-letter characters
            Pig_Word = word #It simply adds the characters/word in the list without doing anything to it
            Pig_Text.append(Pig_Word)

    Pig_Text = ''.join(Pig_Text) #This line makes the list into a string again
    print('Your Newly Translated Texts is: ' + Pig_Text) #Finally, the Pig Latin is displayed!
    Once_More()

Pig_Latin()