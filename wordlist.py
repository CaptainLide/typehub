wlist = []
wordlist = open('sentences.txt').read().splitlines()

for words in wordlist:
    if words in wlist:
        continue
    else:
        wlist.append(words)
