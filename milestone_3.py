import random

word_list = ['apple', 'banana', 'peach', 'pineapple', 'strawberry']
word = random.choice(word_list)
print(word)

def check_guess(guess): 
    if guess in word:
       print(f'Good guess! {guess} is in the word')
    else:
       print(f'Sorry, {guess} is not in the word')

def ask_for_input():
    while True:
        guess = input('Please enter your character')
        if len(guess) == 1 and guess.isalpha():
           check_guess(guess)
           break
        else:
           print('Invalid letter. Please enter a signle alphabetical character')
           
ask_for_input()  

