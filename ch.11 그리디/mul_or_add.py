num_li = list(map(int, input()))
print(num_li)
ans = 0
for i in num_li:
    if i==0 or i==1:
       ans += i
    else:
        if ans == 0:

            ans = 1
            ans *= i
        else:
            ans *= i

print(ans)

