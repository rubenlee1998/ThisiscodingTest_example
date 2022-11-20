from collections import deque
n = list(input())
n.sort()
tmp = deque(n[:])

result = 0
for i in n:
    if ord(i) >= 48 and ord(i) <= 57:
        result += int(i)
        tmp.popleft()
tmp.append(result)

for i in range(len(tmp)):
    print(tmp[i], end='')






