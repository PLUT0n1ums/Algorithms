import math

def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    d = [1, 0] + [0] * (n - 1)
    for i in range(2, n + 1):
        d[i] = (i - 1) * (d[i - 1] + d[i - 2])
    return d[n]

def count_permutations_with_k_beautiful_points(n, k):
    return math.comb(n, k) * derangement(n - k)

n, k = map(int, input().split())
print(count_permutations_with_k_beautiful_points(n, k))
