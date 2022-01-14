import random

def display_hangman(tries):
    stages = [  '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def init_words():
    list_words = ['APPLE', 'MEMENTO', 'GUITAR']
    return list_words

def get_word(list_words):
    return random.choice(list_words)

def play(word):
    tries = 6
    replaced_word = ('_ ' * len(word)).split()
    win = False
    print(display_hangman(tries))
    print('\t' + ' '.join(replaced_word))
    while win == False and tries > 0:
        gamer_input = input("Enter word or letter: ").upper()
        if len(gamer_input) > 1 and word == gamer_input:
            win = True
            guessed_letter = True
            replaced_word = word
        elif len(gamer_input) == 1:
            guessed_letter = False
            for i, _ in enumerate(replaced_word):
                if replaced_word[i] != '_':
                    continue
                else:
                    if word[i] == gamer_input:
                        replaced_word[i] = gamer_input
                        guessed_letter = True
        if not guessed_letter:
            tries -= 1
        if replaced_word.count('_') == 0:
            win = True
        print(display_hangman(tries))
        print('\t' + ' '.join(replaced_word))
    if win == True:
        print(f'You won! Word is "{word}"')
    else:
        print(f'You lose! Word is "{word}"')

def hangman_game():
    list_words = init_words()
    word = get_word(list_words)
    play(word)    

hangman_game()