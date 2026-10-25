MOD = 10**9 + 7

k, n = map(int, input().split())

if k > n:
    print(0)
else:
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    print(dp[k])
<<<<<<< HEAD
    print("hello 567 xyz")
# note moi thu2
=======
    print("Hello 123 abc")
>>>>>>> main
