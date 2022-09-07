# 피보나치 함수를 재귀 함수로 구현
def fib(x):
    print(f"f({str(x)})", end=' ')
    if x == 1 or x == 2:
        return 1
    return fib(x-1) + fib(x-2)

print(fib(6))
