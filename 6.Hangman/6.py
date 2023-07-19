logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

word_list = ["aardvark", "baboon", "camel"]
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word= random.choice(word_list)
print(f'Pssst,the solution is {chosen_word}.')
display=[]
word_length=len(chosen_word)
lives=6
for _ in range(word_length):
  display +="-"
print(display)
end_of_game= False
while not end_of_game:
  guess=input("guess a letter=").lower()
  for position in range(word_length):
      letter=chosen_word[position]
      #print(f"current position: {position}\n current 
  #letter: {letter}\n guessed letter: {guess}")
      if letter==guess:
        display[position]=letter
  if guess not in chosen_word:
    print(f"you guessed {guess},that's not in the word.you lose a life.")
    lives -=1
    if lives == 0:
      end_of_game= True
      print("you lose.")
    
  print(f"{''.join(display)}") 
  if "-" not in display:
    end_of_game=True
    print("you win!!")
  print(stages[lives])  
  
    


