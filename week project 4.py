def threeSumClosest(nums, target):
    nums.sort()  # Sort the array
    closest_sum = float('inf')

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:  # If the sum equals the target, return it
                return closest_sum

    return closest_sum


# Example usage:
A = [-1, 2, 1, -4]
B = 1
print(threeSumClosest(A, B))  # Output should be 2
