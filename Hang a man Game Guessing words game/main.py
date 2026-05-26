import random
word_list = ['camel','abrakadabra','pikachu','ohiny']
lives = 6

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
  |   |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  |   |
  |   |
  |   |
      |
=========
''']

chose_word = random.choice(word_list)

placeholder = ''
lenght = len(chose_word)
for position in range(lenght):
    placeholder += '_'

print(placeholder)

correctLetter = []
gameOver = False
while not gameOver:
    guess = input("choose a letter: ").lower()
    display = ''
    for letters in chose_word:
        if guess == letters:
            display += letters
            correctLetter.append(letters)

        elif letters in correctLetter:
            display += letters    
        else:
            display += '_'   

    print(display)
    if '_' not in display:
        print("You win the game")
        gameOver = True

    if guess not in chose_word:
        lives-=1
        if lives == 0:
            gameOver = True
            print("You lost the game")
       
        
    print(stages[lives])    