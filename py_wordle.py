import random
import sys

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
    global correct_letters
    correct_letters = []
    for x in range(len(user_input)):
        if user_input[x] == word[x]:
            print(f"Letter {x+1} Match!")
            correct_letters.append(user_input[x])
            blank[x] = user_input[x]
        elif user_input[x] in word:
            print(f"Letter {x+1} Wrong spot, right letter!")
            correct_letters.append(user_input[x])
        else:
            print(f"Letter {x+1} Wrong letter entirely!")
            
def get_input():
    user_input = input("Guess a 5 letter word: ")
    return user_input
  
if __name__ == '__main__':
    game_word = get_word()
    print(game_word)
    blank = set_array(game_word)
    while True:
        for x in blank:
            sys.stdout.write(x + ' ')
        print()
        if ''.join(blank) == game_word:
            print(f"You Won!\nThe word is: {game_word}")
            break
        else:
            user_input = get_input()
            if len(user_input) != 5:
                print("Must be 5 letters! Try again!")
                continue
            else:
                check_guess(user_input,game_word,blank)
                print(correct_letters)
    









