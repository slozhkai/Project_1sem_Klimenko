n = int(input())
k = 0
while True:
    if 3 ** k >= n:
        k -= 1
        break
    k += 1
print(k)
