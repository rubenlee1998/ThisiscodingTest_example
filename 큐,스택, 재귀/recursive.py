def recursive_function(i):
    if i == 5:
        return
    print(i, "번째 재귀에서", i+1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)

recursive_function(1)
