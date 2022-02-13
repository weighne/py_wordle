import random
import sys
from os import system, name
from termcolor import colored

# getting the word list in order
# with open("words.txt") as wordlist:
#     words = [x.strip() for x in wordlist if len(x) == 6]
#
# with open("words_5.txt","a") as out_file:
#     for x in words:
#         out_file.write(x + '\n')
#
# with open('words_5.txt',"r") as in_file, open('words_5_clean.txt','a') as out_file:
#     for x in in_file:
#         if x.strip().isalpha() == True:
#             out_file.write(x)
#             print(x + "ADDED")
#         else:
#             print(x + "NOT ADDED")
#             continue

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
wrong_letters = []
user_guesses = []
guess_guides = []

def cls():
    input('Press any key to continue...')
    if name == 'nt':  # for windows
        _ = system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


def print2(text):
    for x in text:
        sys.stdout.write(f'{x} ')
    print()


def print_blue(text):
    out_list = []
    for x in text:
        if x == 'X':
            out_list.append(colored(x,'red'))
        elif x == '?':
            out_list.append(colored(x,'yellow'))
        else:
            out_list.append(colored(x,'cyan'))

    output = ' '.join(out_list)
    print(output)
    # print(colored(text, 'blue'))


def get_word():
    with open("words_5_clean.txt","r") as wordlist:
        words = [x.strip() for x in wordlist.readlines()]
        # print(words)
        word = random.choice(words)
        # print(word)
        return word


def set_array(word):
    blank = []

    for x in word:
        blank.append('_')

    return blank


def check_guess(user_input, word, blank):
    letter_guide = []
    user_guesses.append(user_input)
    print2(user_input)

    # global wrong_letters
    for x in range(len(user_input)):
        if user_input[x] == word[x]:
            # print(f"Letter {x+1} Match!")
            sys.stdout.write(user_input[x] + ' ')
            letter_guide.append(user_input[x])
            blank[x] = user_input[x]
            for y in range(len(alphabet)):
                if alphabet[y] == user_input[x]:
                    alphabet[y] = f'{user_input[x]}'
        elif user_input[x] in word:
            # print(f"Letter {x+1} Wrong spot, right letter!")
            sys.stdout.write('? ')
            letter_guide.append('?')
            for y in range(len(alphabet)):
                if alphabet[y] == user_input[x]:
                    alphabet[y] = f'({user_input[x]})'
        else:
            # print(f"Letter {x+1} Wrong letter entirely!")
            sys.stdout.write('X ')
            letter_guide.append('X')
            for y in range(len(alphabet)-1):
                if alphabet[y] == user_input[x]:
                    alphabet.pop(y)
                else:
                    continue
            if user_input[x] not in wrong_letters:
                wrong_letters.append(user_input[x])

    guess_guides.append(''.join(letter_guide))

def get_input():
    user_input = input("Guess a 5 letter word: ")
    return user_input

if __name__ == '__main__':
    guesses = 0
    game_word = get_word()
    # print(game_word)
    blank = set_array(game_word)
    while True:
        cls()
        if len(user_guesses) >= 1:
            for x in range(len(user_guesses)):
                print2(user_guesses[x])
                print_blue(guess_guides[x])

        print('\nRemaining Letters:')
        print2(alphabet)
        print('Wrong Letters:')
        print2(wrong_letters)
        print2(blank)

        if ''.join(blank) == game_word:
            print(f"You Won!\nThe word is: {game_word}")
            for x in range(len(user_guesses)-1):
                user_guesses.pop(x)
            break
        elif guesses >= 6 and ''.join(blank) != game_word:
            print(f"You Lose!\nThe word was: {game_word}")
            for x in range(len(user_guesses)-1):
                user_guesses.pop(x)
            break
        else:
            user_input = get_input()
            if len(user_input) != 5:
                print("Must be 5 letters! Try again!")
                continue
            else:
                check_guess(user_input,game_word,blank)
                guesses += 1
