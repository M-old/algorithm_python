n, k = map(int, input().split())
result = 0
array = []

for i in range(n):
    array.append(int(input()))

array.reverse()

for i in range(n):
    if array[i] <= k:
        result += k // array[i]
        k %= array[i]

print(result)
