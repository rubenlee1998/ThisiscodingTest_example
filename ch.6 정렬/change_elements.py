n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sor_a = sorted(a)
sor_b = sorted(b, reverse=True)
for i in range(k):
    if sor_a[i] < sor_b[i]:
        sor_a[i] = sor_b[i]

print(sum(sor_a))