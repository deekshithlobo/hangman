#Step 2

import random
from words import word_list 
from design import stages,logo
#just a comment to check version
wrong_guesses=[]
print(logo)
chosen_word = random.choice(word_list)
counter = 6
ls = ['_']*(len(chosen_word))
print(''.join(ls))
ct = ''
while (ct != chosen_word) and (counter > 0):
  guess = input("\nGuess a letter: ").lower()
  if len(guess)>1:
    print('please enter a single character\n')
    continue
#add wrong guesses to a list in-order to inform the player to
#if they have already guessed it
  if(guess in wrong_guesses)or(guess in ls):
      print("You have already guessed it")
      continue
  if(guess not in chosen_word):
    wrong_guesses.append(guess)
    print(stages[counter-1])
    counter =counter - 1
#replace blanks with guess words
  for i in range(len(chosen_word)):
    if chosen_word[i]  == guess:
      ls[i]= guess
  ct = ''.join(ls)
  print(ct)

if ct == chosen_word:
  print("You Win")
elif ct != chosen_word and counter <= 0:
  print("You lose! It was",chosen_word)
  