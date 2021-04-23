from random import *

def StressTest(N, M):

    while True:
        n = randint(2, N)
        a = [None] * n

        for i in range(n):
            a[i] = randint(0, M)
        
        