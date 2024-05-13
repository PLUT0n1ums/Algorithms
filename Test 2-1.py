def can_partition(weights, max_weight):
    current_weight = 0
    for weight in weights:
        if current_weight + weight <= max_weight:
            current_weight += weight
        else:
            return False
    return True

def min_weight_difference_binary_search(weights):
    left = max(weights)
    right = sum(weights)
    min_difference = float('inf')

    while left <= right:
        mid = left + (right - left) // 2
        if can_partition(weights, mid):
            min_difference = min(min_difference, right - mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_difference

# Test the function
weights = [10, 20, 30, 40, 50]
result = min_weight_difference_binary_search(weights)
print("The minimum possible difference between the weights of two piles (binary search) is:", result)