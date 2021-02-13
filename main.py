from random import choice
from hangman_art import stages, logo
import requests
import json 
from tqdm import tqdm

for timeout in tqdm(range(0, 25, 5), desc='Checking internet connection'):
  try:
    # if internet is available
    # GET from api
    #print('Checking internet connection.....')
    data=requests.get('https://random-word-api.herokuapp.com/all/?swear=0', timeout=timeout).text
    words=json.loads(data)
  except:
    # If no Internet use import words
    from hangman_words import words

#words= ['aardvak', 'baboon', 'camel']
chosen_word=choice(words)
length_of_word=len(chosen_word)
display = ['_' for _ in range(length_of_word)]
lives=6

print(logo)

end_of_game=False

while not end_of_game:
  guess=input('Guess a letter: ').lower()

  if guess in display:
    print(f'You have already entered {guess}')

  for index, letter in enumerate(chosen_word):
    if letter==guess:
      display[index]=guess
  if guess not in chosen_word:
    lives-=1
    print(f'{guess} is not in word. You lost a life')
    if lives==0:
      print('You lose..')
      print(f'The word was {chosen_word}')
      end_of_game=True
    

  if '_' not in display:
    print('You win!!!!!')
    end_of_game=True

  print(' '.join(display))

  print(stages[lives])
    
     