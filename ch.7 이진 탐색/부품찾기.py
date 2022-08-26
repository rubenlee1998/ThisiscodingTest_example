n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

n_li.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return print("yes", end=' ')
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return print("no", end=' ')


for i in range(m):
    binary_search(n_li, m_li[i], 0, n-1)
