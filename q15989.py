dp = [[0, 0, 0] for i in range(10000)]

dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 1

for i in range(3, 10000):
    dp[i][0] = 1
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

T = int(input())

for _ in range(T):
    n = int(input())
    print(int(dp[n-1][0] + dp[n-1][1] + dp[n-1][2]))