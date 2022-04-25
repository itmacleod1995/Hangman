import hangmans as hangman
from random_word import RandomWords

r = RandomWords()

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/

""")

"""Select random word from list"""
wordSelected = r.get_random_word()
word = []
for letter in wordSelected:
    word.append("_")

print("".join(word))

lettersAlreadyPicked = []
game = True
score = 0

while game:
    """Prints the corresponding hangman ascii art based on score"""
    if score == 1:
        hangman.scoreIs1()
    elif score == 2:
        hangman.scoreIs2()
    elif score == 3:
        hangman.scoreIs3()
    elif score == 4:
        hangman.scoreIs4()
    elif score == 5:
        hangman.scoreIs5()
    elif score == 6:
        hangman.scoreIs6()
    else:
        hangman.scoreIs0()


    if "".join(word) == wordSelected:
        print("You win!")
        break

    if score == 6:
        print("The word was {}".format(wordSelected))
        print("You lose!")
        break

    letter = input("Guess a letter: ")
    if letter in lettersAlreadyPicked:
        print("You already picked that letter!")
    else:
        if letter in wordSelected:
            print("{} is in the word!".format(letter))
            for i in range(len(wordSelected)):
                if wordSelected[i] == letter:
                    word[i] = letter
        else:
            print("{} is not in the word".format(letter))
            score += 1

        lettersAlreadyPicked.append(letter)
        print("")
        print("".join(word))
