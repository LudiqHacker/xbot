import random
import os
import time
os.system("clear")

list = ["Koi te pita?", "si ti"]
for i in range(100000):
  input()
  roast = random.choice(list)
  time.sleep(1)
  print(roast)