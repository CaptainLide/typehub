import time
import subprocess
from callwords import words



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

while game_on:
    print("hi")
    for word in words:
        user_input = input(word)
        if user_input.lower() == word.lower():
            count += 1
        else:
            cmd = "curl -s https://random-word-api.herokuapp.com/word?number=1"
            words.append(subprocess.getoutput(cmd))

    if count == len(words):
        game_on = False
