#print("hello world")

# "This game focuses on the user having to guess the randomly generated word. You can create a list from which the word would have to be guessed and also set a cap on the number of guesses allowed"

#Take user input, use conditionals to match word to list, set guess limit; create code for displaying if won or lost (if lost, maybe reset button?), high score determined by number of guesses, game start button

#Extras(if enough time): High scores, personalize text color?

guessCount = 3

print("Guessing Words Game Begin!")

fruitList = [
    "Strawberry", "Apple", "Watermelon", "Tomato", "Laychee", "Cherry"
]

sportsList = [
    "Hockey", "Badminton", "Surfing", "Archery", "Frisbee", "Swimming"
]

fruitHint = "Hint: These fruits are red"

sportsHint = "Hint: These sports don't include a ball"

categoryChoice = False

while categoryChoice == False:
    userChoice = input("Pick a category: Fruits or Sports: ")

    if str.lower(userChoice) == "fruits":
        wordList = fruitList
        wordHint = fruitHint
        categoryChoice = True

    elif str.lower(userChoice) == "sports":
        wordList = sportsList
        wordHint = sportsHint
        categoryChoice = True

    else:
        print("Invalid category, try again")

for guess in range(guessCount):
    print("- You have " + str(guessCount) + " guesse(s) left!")
    if guessCount == 1:
        print(wordHint)
    userResponse = input("Guess what word it is! ")

    # Lets assume word is not found
    found = False

    # Lets try and see if word is found?
    for word in wordList:
        if str.lower(userResponse) == str.lower(word):
            print("You are correct!")
            found = True

    if found == False:
        print("You are incorrect")

    else:
        break

    guessCount = guessCount - 1