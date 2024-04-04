class Solution:
    def solve(self, A, B):
        i = 0
        j = 0
        pre = 0
        ans = 0

        while i < len(A) and j < len(A):
            pre += A[j]
            if (j - i + 1) - pre <= B:
                j += 1
                ans = max(ans, j - i)
            else:
                i += 1
                pre -= A[i - 1]

        return ans