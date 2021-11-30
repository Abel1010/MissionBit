#print("hello world")

# "This game focuses on the user having to guess the randomly generated word. You can create a list from which the word would have to be guessed and also set a cap on the number of guesses allowed"

#Take user input, use conditionals to match word to list, set guess limit; create code for displaying if won or lost (if lost, maybe reset button?), high score determined by number of guesses, game start button

#Extras(if enough time): High scores, personalize text color?, 


print("Guessing Words Game Begin!")

wordList = ["Peach", "Banana", "Orange", "Strawberry", "Kiwi", "Apple", "Watermelon", "Bluberry", "Lemon", "Fig", "Grape", "Tomato", "Guava", "Mango", "Laychee", "Cherry", "Baseball", "Basketball", "Tennis", "Football","Volleyball", "Badminton", "Soccer", "Hockey", "Table Tennis", "Soft Ball", "Surfing", "Archery"];

userResponse = input("Guess what word it is? ")

# Lets assume word is not found
found = False

# Lets try and see if word is found?
for word in wordList:
    if userResponse == word:
        print("You are correct!")
        found = True

if found == False:
    print("You are incorrect")

# Note from Tomas: Feel free to hit me up on slack if you have any question in between classes :)
# (And remember to commit this to git :)