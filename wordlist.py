list = []
wordlist = open('wordbank.txt').read().split()

for words in wordlist:
    if words in list:
        continue
    else:
        list.append(words)