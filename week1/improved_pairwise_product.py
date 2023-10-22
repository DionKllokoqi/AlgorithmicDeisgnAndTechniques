# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

result = 0

index1 = 0

for i in range(1, n):
    if a[i] > a[index1]:
        index1 = i

if index1 == 0:
    index2 = 1
else:
    index2 = 0

for i in range(1, n):
    if i != index1 and a[i] > a[index2]:
        index2 = i

result = a[index1] * a[index2]

print(result)
