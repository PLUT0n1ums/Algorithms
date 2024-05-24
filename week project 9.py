def min_flips_to_minimize_sum(A):
    total_sum = sum(A)
    n = len(A)
    target = total_sum // 2

    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in A:
        for j in range(total_sum, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    closest_sum = 0
    for i in range(target, -1, -1):
        if dp[i]:
            closest_sum = i
            break

    sum_to_find = closest_sum
    flips = 0
    for num in A:
        if sum_to_find <= 0:
            break
        if sum_to_find >= num and dp[sum_to_find - num]:
            sum_to_find -= num
            flips += 1

    return flips
