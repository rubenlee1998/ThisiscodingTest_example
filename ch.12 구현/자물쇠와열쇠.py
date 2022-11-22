# 2차원 리스트를 90도 회전하는 함수
def rotate_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a[0])  # 열
    # 90도 회전한 후 결과값 다음 2차원 리스트(행, 열 Transpose)
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]  # n=행의 개수
    return result


def check(new_lock):
    origin_lock_len = len(new_lock) // 3
    for i in range(origin_lock_len, origin_lock_len * 2):
        for j in range(origin_lock_len, origin_lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 길이를 3배로 늘리기
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 늘린 자물쇠에 원래 자물쇠 값 갱신
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]  # 이때, n = 원래 자물쇠 길이

    # 4가지 방향에 대해 탐색
    for _ in range(4):
        key = rotate_matrix_by_90_degree(key)  # 열쇠 90도 회전
        # 회전시킨 열쇠를 자물쇠의 중앙부분에 합치기
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 열쇠 돌기랑 자물쇠 홈이 맞는지 체크
                if check(new_lock):
                    return True

                # 안맞는 열쇠는 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False