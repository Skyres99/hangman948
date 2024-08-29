import random

word_list = ['apple', 'banana', 'peach', 'pineapple', 'strawberry']
print(word_list)

word = random.choice(word_list)

guess = input('Please enter your choice!')
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops that is not a valid input')      