wlist = []
wordlist = open('wordbank.txt').read().split()

for words in wordlist:
    if words in wlist:
        continue
    else:
        wlist.append(words)
