n = int(input())
li = sorted(map(int, input().split()))

party = 0 # 파티의 수
cnt = 0  # 파티에 참여한 인원 수

for i in li:
    cnt+=1
    if cnt >= i:
        cnt = 0
        party += 1

# 공포도가 높은 놈은 배제한다. 낮은 놈들끼리 하는거지

