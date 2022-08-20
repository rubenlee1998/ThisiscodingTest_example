n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
result = sorted(numbers, reverse=True)
for i in result:
    print(i, end=' ')