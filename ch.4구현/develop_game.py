import sys

def left_90deg(D):
    if D == 0:
        D = 3
    elif D == 3:
        D = 2
    elif D == 2:
        D = 1
    elif D == 1:
        D = 0
    return D

N, M = map(int, input().split())
A, B, d = map(int, input().split())
mapp = [0 for _ in range(N)]
for i in range(N):
    mapp[i] = list(map(int, sys.stdin.readline().split()))

#동서남북 중 한곳을 바라본다. 그리고 이동한다.
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if (mapp[A-1][B] and mapp[A][B+1] and mapp[A+1][B] and mapp[A][B-1]) != 0: #동서남북 방향이 0이 아니면
        if mapp[A-dy[d]][B-dx[d]] == 1: # 게다가 뒤 방향이 바다면
            break                       # 그만
        else:                           # 내 뒤가 바다가 아니라면
            mapp[A][B] = -1             # 일단 내 위치에 -1 지정하고
            A -= dy[d]                  #뒤로갈게
            B -= dx[d]
    elif mapp[A+dy[d]][B+dx[d]] != 0:   # 사방에 0이 존재하는데 내가 향한 방향이 0이 아니면
        d = left_90deg(d)               # 보는 방향을 왼쪽으로 90도 회전시킨다.
    elif mapp[A+dy[d]][B+dx[d]] == 0:   # 사방에 0이 존재하고 내가 향한 방향이 0이라면
        mapp[A][B] = -1                 # 내가 지나온 길에 -1 표시해주고
        A += dy[d]                      # 내가 향하는 방향으로 1칸 이동
        B += dx[d]

# 맵 리스트 요소에서 -1 개수 세주고 끝
count = 0
for k in mapp:
    for l in k:
        if l==-1:
            count+=1
print(count)

# 위 코드는 x,y축을 반대로 써서 3시간
# 마지막 위치 map[A][B]를 -1 안해줘서 1시간 걸린 코드입니다.

















