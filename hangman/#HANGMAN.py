#HANGMAN
from hangman_art import stages, logo

print(logo)

import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

lives = 6

for _ in range(word_length) :
  display += "_"
print (display)

end_of_game = False

while not end_of_game :
  guess = input("guess a letter: ").lower()
  
  if guess in display:
        print(f"You've already guessed {guess}.")

  for position in range(word_length) :
    letter = chosen_word[position]
    if letter == guess :
      display[position] = letter

  if guess not in chosen_word :
    lives -= 1
    print("You have guessed a wrong letter so you lose a life.")
    if lives == 0 :
      end_of_game = True
      print(f"You lose. The correct answer was {chosen_word}.")

  print(f"{' '.join(display)}")

  if "_" not in display :
   end_of_game = True
   print("You win.")
  print(stages[lives])