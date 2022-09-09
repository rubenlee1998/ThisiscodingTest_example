n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))

d = [10001]*(m+1)
d[0] = 0


for i in range(n):
    for j in range(li[i], m+1):
        if d[j - li[i]] != 10001:
            print(d)
            d[j] = min(d[j], d[j-li[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])