from random import random
import sys

n = int(sys.argv[1])
inC = 0

for i in range(n):
    x = random()
    y = random()
    if (x * x + y * y) <= 1:
        inC += 1

print(inC / n * 4)
