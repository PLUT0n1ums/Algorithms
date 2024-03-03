class Solution:

    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        for i in range(2, A):
            if is_prime(i) and is_prime(A - i):
                return [i, A - i]
