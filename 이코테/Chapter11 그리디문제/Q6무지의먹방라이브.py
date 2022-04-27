def solution(food_times, k):
    answer = 0

    if k >= sum(food_times):
        answer = -1

    elif k <= len(food_times) * min(food_times):
        answer = (k % len(food_times) + 1) % len(food_times)
        while food_times[answer] == 0:
            answer = (answer + 1) % len(food_times)
    else:
        min_time = min(food_times)
        for i in range(len(food_times)):
            food_times[i] -= min_time

        k -= min_time * len(food_times)

        while k != 0:
            for i in range(len(food_times)):
                if food_times[i] == 0:
                    continue
                else:
                    food_times[i] -= 1
                    k -= 1

                if k == 0:
                    answer = (i + 1) % 3 + 1
                    break

    return answer


print(solution([3, 1, 2], 5))
