import time
import subprocess
import random
from callwords import word_bank


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

for _ in range(20):
    words.append(random.choice(word_bank))

while game_on:
    for word in words:
        user_input = input(word)
        if user_input.lower() == word.lower():
            count += 1
        else:
            words.append(random.choice(word_bank))

    if count == len(words):
        game_on = False
