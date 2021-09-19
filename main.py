import time
import subprocess
import random
from wordlist import wordlist


def countdown(t):
    while t:
        mins = t//60
        secs = t%60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time\'s up!')

t = input("Enter the time in seconds: ")

countdown(int(t))

game_on = True
count = 0
words = []

for _ in range(5):
    words.append(random.choice(wordlist))

while game_on:
    for word in words:
        user_input = input(word + "\n")
        if user_input.lower() == word.lower():
            count += 1
        else:
            words.append(random.choice(wordlist))

    if count == len(words):
        game_on = False
