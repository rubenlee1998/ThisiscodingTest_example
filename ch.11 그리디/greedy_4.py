# from itertools import *
#
# n = int(input())
# coin_li = list(map(int, input().split()))
# tmp_i = 0
# sum_coin = sum(coin_li)
# coin_li.sort()
# result = 0
# # if coin_li[0] != 1:
# #     print(1)
# # else:
# #     for i in range(2, sum_coin+1):
# #         tmp_i = i
# #         for j in range(len(coin_li)):
# #             tmp_i -= coin_li[j]
# #             if tmp_i == 0:
# #                 result = i
#
# def sum_li(arr):
#     ans = []
#     size=len(arr)
#     for i in range(1, size+1):
#         ans.append(list(permutations(arr, i)))
#     return ans
#
# print(sum_li(coin_li))
# print(len(sum_li(coin_li)))
#
# for i in range(len(coin_li)):
#     (sum_li(coin_li)[i])

n = int(input())
coin_li = list(map(int, input().split()))
coin_li.sort()

target = 1 # target값을 만들 수 있니?
for x in coin_li:
    if target < x: # target을 만들랬더니 내가 준 동전보다 작으면 당연히 못만들지 target은 못만드는구나 후..
        break
    target += x # 오 만들 수 있네 그럼 지금까지 만든 동전에

print(target)
