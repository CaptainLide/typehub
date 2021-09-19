import time   

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
