n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
cnt = 0
for i in range(n-1):
    for j in range(i, n):
        if data[i]!=data[j]:
            cnt += 1
print(cnt)