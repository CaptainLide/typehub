import sys
import getch
def new_input(prefix=""):
    while True:
        key = ord(getch())
        if key == 32 or key == 13:
            break

new_input()
