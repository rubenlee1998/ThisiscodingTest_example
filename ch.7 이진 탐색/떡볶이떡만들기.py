n, m = map(int, input().split())

n_li = list(map(int, input().split()))

max_num = max(n_li)


def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        cnt = 0
        mid = (start+end) // 2
        for i in arr:
            if i > mid:
                cnt += i-mid
        if cnt < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return print(result)

binary_search(n_li, m, 0, max_num)
