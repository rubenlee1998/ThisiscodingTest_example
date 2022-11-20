n = list(map(int,input()))
left_result = 0
right_result = 0

for i in range(len(n)//2):
    left_result += n[i]
for j in range(len(n)//2, 0, -1):
    right_result += n[-j]

if left_result==right_result:
    print('LUCKY')
else:
    print('READY')