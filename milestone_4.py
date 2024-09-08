import random

word_list = ['apple', 'banana', 'peach', 'pineaaple', 'strawberry']

class Hangman():
           
      def __init__(self, word_list, num_lives = 5):
            self.word = random.choice(word_list)
            self.word_guessed = ['_', '_', '_', '_', '_'] * len(self.word)
            self.num_letters = len(set(self.word))
            self.num_lives = num_lives
            self.word_list = word_list
            self.list_of_guesses = []
            
      def check_guess(self, guess):
            if guess in self.word:
                  print(f'Good guess! {guess} is in the word')
                  for _ in range(len(self.word)):
                        if self.word[_] == guess:
                              self.word_guessed[_] == guess
                  self.num_letters -= 1
            else:
                  self.num_lives -= 1
                  print(f'Sorry, {guess} is not in the word.')
                  print(f'You have {self.num_lives} lives left')
            
      def ask_for_input(self):
            while True:
                  self.guess = input('Please enter your character.')
                  self.guess = self.guess.lower()
                  if len(self.guess) != 1 and not self.guess.isalpha():
                        print('Invalid letter. Please, enter a single alphabetical character.')
                  elif self.guess in self.list_of_guesses:
                        print('You alredy tried that letter!')
                  else:
                        self.list_of_guesses.append(self.guess)
                        self.check_guess(self.guess)
      
check = Hangman(word_list)
check.ask_for_input()                              