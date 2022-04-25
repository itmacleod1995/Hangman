import random

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
words = ["chicken", "football", "salad", "tesla"]
wordSelected = random.choice(words)
word = []
for letter in wordSelected:
    word.append("_")

print("".join(word))

lettersAlreadyPicked = []
game = True
score = 0

while game:
    if "".join(word) == wordSelected:
        print("You win!")
        break

    if score == 6:
        print("You lose!")
        break

    letter = input("Guess a letter: ")
    if letter in lettersAlreadyPicked:
        print("You already picked that letter!")
    else:
        if letter in wordSelected:
            print("In word")
            for i in range(len(wordSelected)):
                if wordSelected[i] == letter:
                    word[i] = letter
        else:
            print("{} is not in the word".format(letter))
            score += 1

        lettersAlreadyPicked.append(letter)

        print("".join(word))
