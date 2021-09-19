import os 
cmd = 'curl https://random-word-api.herokuapp.com/word?number=20'
words = []

for word in os.system(cmd):
    words.append(word)
print(words)
