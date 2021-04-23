# Uses python3
def calc_fib(n):

    # Case n = 1 and n = 0 returns just n
    if n <= 1:
        return n
    
    fibArray = [1, 1]
    for i in range(2, n):
        fibArray.append(fibArray[i - 1] + fibArray[i - 2])
    return fibArray[n - 1]

n = int(input())
print(calc_fib(n))
