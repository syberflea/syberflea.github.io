from random import choice

print("H A N G M A N")
languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
hint = language[:3] + "-" * (len(language) - 3)
guess_word = input(f"Guess the word {hint}: ")
if guess_word == language:
    print("You survived!")
else:
    print("You are hanged!")
    
------------------------------------------------------------------------------
from random import choice

print("H A N G M A N")
languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
tries = 8
answer = list("-" * len(language))
for _ in range(tries):
    print("")
    print(''.join(answer))
    char = input("Input a letter: ")
    if char not in language:
        print("No such letter in the word")
        continue

    for i in range(len(language)):
        if char == language[i]:
            answer[i] = char
else:
    print("\nThanks for playing!")
    print("We'll see how well you did in the next stage")
    
    
-----------------------------------------
from random import choice

languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
# language = 'python'
tries = 8
answer = list("-" * len(language))
history = []

print("H A N G M A N")
while tries > 0:
    print("")
    print(''.join(answer))
    char = input("Input a letter: ")

    if char in history:
        tries -= 1
        print("No improvements")
        continue
    else:
        history.append(char)

    if char not in language:
        tries -= 1
        print("No such letter in the word")
        continue

    for i in range(len(language)):
        if char == language[i]:
            answer[i] = char

    if '-' not in answer:
        print("You survived!")
        break
else:
    if tries == 0:
        print("You are hanged!")

        
===========================================================================
from random import choice

print("H A N G M A N")
languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
tries = 8
answer = list("-" * len(language))
for _ in range(tries):
    print("")
    print(''.join(answer))
    char = input("Input a letter: ")
    if char not in language:
        print("No such letter in the word")
        continue

    for i in range(len(language)):
        if char == language[i]:
            answer[i] = char
else:
    print("\nThanks for playing!")
    print("We'll see how well you did in the next stage")
    
    
-----------------------------------------
from random import choice

languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
# language = 'python'
tries = 8
answer = list("-" * len(language))
history = []

print("H A N G M A N")
while tries > 0:
    print("")
    print(''.join(answer))
    char = input("Input a letter: ")

    if char in history:
        tries -= 1
        print("No improvements")
        continue
    else:
        history.append(char)

    if char not in language:
        tries -= 1
        print("No such letter in the word")
        continue

    for i in range(len(language)):
        if char == language[i]:
            answer[i] = char

    if '-' not in answer:
        print("You survived!")
        break
else:
    if tries == 0:
        print("You are hanged!")
______________________________________________
from random import choice
from string import ascii_lowercase

languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
tries = 8
answer = list("-" * len(language))
history = set()
letters = set(language)
guess_letters = set(language)
guessed_letters = set()

print("H A N G M A N")
while tries > 0:
    if guess_letters == guessed_letters:
        print("You guessed the word!")
        break

    print("")
    print(''.join(answer))
    char = input("Input a letter: ")

    if char in guess_letters and char not in guessed_letters:
        guessed_letters.add(char)
        history.add(char)
    elif len(char) > 1:
        print("You should input a single letter")
    elif char not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
    elif char in history:
        # tries -= 1
        print("You already typed this letter ")
    else:
        tries -= 1
        history.add(char)
        print("No such letter in the word")

    for i in range(len(language)):
        if char == language[i]:
            answer[i] = char

    if '-' not in answer:
        print("You survived!")
        break
else:
    if tries == 0:
        print("You are hanged!")
