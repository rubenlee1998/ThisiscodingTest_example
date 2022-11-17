def solution(food_times, k):
    for i in range(k):
        i = i%len(food_times)
        if food_times[i] != 0:
            food_times[i] -= 1
        result = i

    return result