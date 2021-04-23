#Uses python3
import sys

def better_number(num, maxNum):
    if num + maxNum > maxNum + num:
        return True
    else:
        return False

def largest_number(a):
    res = ""
    while a:
        maxNumStr = a[0]
        for num in a:
            if better_number(num, str(maxNumStr)):
                maxNumStr = num
        res += maxNumStr
        a.remove(maxNumStr)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
