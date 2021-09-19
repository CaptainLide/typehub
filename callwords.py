import subprocess
cmd = "curl -s https://random-word-api.herokuapp.com/word?number=20"
words = subprocess.getoutput(cmd)

