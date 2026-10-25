
MOD = 10**9 + 7

k, n = map(int, input().split())

if k > n:
    print(0)
else:
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

    print(dp[n][k])
