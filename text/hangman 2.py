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
