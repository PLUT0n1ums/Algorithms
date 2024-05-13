def minimum_board_size_dp(width, height, num_diplomas):
  dp = [float('inf')] * (num_diplomas + 1)
  dp[0] = 0

  for i in range(1, num_diplomas + 1):
    for diploma_size in (width, height):
      if i >= diploma_size and dp[i - diploma_size] != float('inf'):
        dp[i] = min(dp[i], dp[i - diploma_size] + diploma_size)

  return dp[num_diplomas]

width = 10
height = 5
num_diplomas = 4

board_size = minimum_board_size_dp(width, height, num_diplomas)
print("Minimum board size (dynamic programming):", board_size)
