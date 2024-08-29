import random

word_list = ['apple', 'banana', 'peach', 'pineapple', 'strawberry'] # List of 5 words that computer has to choose
word = random.choice(word_list) # Randomly chosen word by computer

guess = input('Please enter your choice!')
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops that is not a valid input')      