n = int(input())
li = []
for _ in range(n):
    li.append(list(input().split()))

sor_li = sorted(li, key= lambda x:int(x[1]))

for i in range(n):
    print(sor_li[i][0], end=' ')
