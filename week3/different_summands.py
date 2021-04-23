# Uses python3
import sys

def optimal_summands_online(n):
    summands = []
    #write your code here
    sumall = 1
    start = 1
    summands.append(start)
    #pdb.set_trace()
    while n - sumall > summands[-1]:
        summands.append(summands[-1] + 1)
        sumall += summands[-1]
    summands[-1] += (n - sumall)
    return summands

def optimal_summands(n):
    summands = []    
    remainder = n
    i = 1
    
    while remainder != 0:
        if (remainder - i - (i + 1)) >= 0:
            summands.append(i)
            remainder -= i
            i += 1
        else:
            summands.append(remainder)
            i = remainder
            remainder -= i

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
