import time
import time
import requests
import math

game_on = True
count = 0
allWords = []
URL = 'https://random-word-api.herokuapp.com/word'
PARAMS = {'number': 1, 'swear': 0}


def getWord():
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    data = r.json()
    allWords.append(data[0])
    return (data[0])


def startClock():
    clock = time.time()
    return clock


def timeLeft(c, t):
    timeElapsed = round(time.time() - c)
    return (t - timeElapsed)


def getAllWords():
    print('Here at Typehub we love learning! Here is a list of all the words you saw, if you don\'t know the meaning of one we encourage you to look it up! \n')
    for word in allWords:
        print(f"{word}: Click the link for a possible definition: ")
        URL = f'https://www.dictionary.com/browse/{word}'
        print(URL, '\n')


def mistakesAllowed(number, accuracy):
    mistakes = (accuracy/100) * number
    return (math.floor(number-mistakes))


mode = int(input('Welcome to typehub, your one stop shop for typing faster! \n Please enter 1 to play creative mode (choose your own time and number of words) \n or \n 2 to play classic mode (complete a set number of words in a set amount of time) \n'))

if (mode == 1):
    t = int(input("Enter the time in seconds: "))

    difficulty = int(
        input(f"How many words in {t} seconds would you like to achieve? "))

    a = int(input("what level of accuracy would you like to aim for? "))

    mistakes = mistakesAllowed(difficulty, a)
    print(f'you can make {mistakes} mistakes')
    mistakeCount = 0
    while game_on:
        word = getWord()
        if (count == 0):
            clock = startClock()
        if (timeLeft(clock, t) <= 0):
            print('Sorry, time ran out! Try again.')
            game_on = False
            getAllWords()

        else:
            user_input = input(word + "\n")
            if user_input.lower() == word.lower():
                count += 1
                if count == difficulty:
                    print('Congratulations, you won!')
                    game_on = False
                    getAllWords()

                else:
                    print(
                        f"\n you have {timeLeft(clock, t)}s left to complete {difficulty - count} words")

            else:
                print('Sorry, that\'s wrong.')
                mistakeCount += 1
                if (mistakeCount >= mistakes):
                    print('You\'ve lost')
                    game_on = False
                    getAllWords()
                else:
                    print(
                        f'you\'ve made {mistakeCount} mistakes out of {mistakes}')

elif (mode == 2):

    def game(t, difficulty, mistakes):
        count = 0
        mistakeCount = 0
        game_on = True
        while game_on:
            word = getWord()
            if (count == 0):
                clock = startClock()
            if (timeLeft(clock, t) <= 0):
                print('Sorry, time ran out! Try again.')
                game_on = False
                return False
            else:
                user_input = input(word + "\n")
                if user_input.lower() == word.lower():
                    count += 1
                    if count == difficulty:
                        print('Congratulations, you won! On to the next level')
                        game_on = False
                        return True
                    else:
                        print(
                            f"you have {timeLeft(clock, t)}s left to complete {difficulty - count} words")

                else:
                    print('Sorry, that\'s wrong.')
                    mistakeCount += 1
                    if (mistakeCount >= mistakes):
                        print('You\'ve lost')
                        game_on = False
                    else:
                        print(
                            f'you\'ve made {mistakeCount} mistakes out of {mistakes}')

    hardness = int(input('Please choose your starting level.\n Enter 0 for demo mode. \n Enter 1 for level 1 (30 WPM). \n Enter 2 for level 2 (40 WPM). \n Enter 3 for level 3 (50 WPM). \n Enter 4 for level 4 (60 WPM). \n'))

    def start():
        rounds = 1
        t = 60
        if (hardness == 1):
            difficulty = 20
        elif (hardness == 2):
            difficulty = 25
        elif (hardness == 3):
            difficulty = 33
        elif (hardness == 4):
            difficulty = 40
        else:
            difficulty = 5
        mistakes = mistakesAllowed(difficulty, 95)
        print(f'you can make {mistakes} mistakes')

        print(f'Round 1: Type {difficulty} words in 60s')
        success = game(t, difficulty, mistakes)
        while (success and rounds != 4):
            rounds += 1
            t = 60
            difficulty = round(difficulty * 1.15)
            mistakes = mistakesAllowed(difficulty, 95)
            print(f'you can make {mistakes} mistakes')
            print(f'Round {rounds}: Type {difficulty} words in 60s')
            success = game(t, difficulty, mistakes)

        if (success):
            print(
                f'Congrats! You succesfully typed at {difficulty}wpm. Time for the final challenge. In each round you must type {difficulty} words in 50s, then 40s, then 30s, ..., 10s')
            rounds = 1
            t = 50
            print(f'Round 1: Type {difficulty} words in 60s')
            success = game(t, difficulty)
            while (success and t > 10):
                rounds += 1
                t -= 10
                print(f'Round {rounds}: Type {difficulty} words in {t}s')
                success = game(t, difficulty)
            if (success):
                print('WINNER \n')
                getAllWords()
            else:
                print('Good try! \n')
                getAllWords()
        else:
            getAllWords()

    start()
