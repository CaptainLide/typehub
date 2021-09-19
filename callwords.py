import os 
cmd = 'curl https://random-word-api.herokuapp.com/word?number=20'
words = os.system(cmd)
print(words) 