
MOD = 10**9 + 7

k, n = map(int, input().split())

if k > n:
    print(0)
else:
    fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    numerator = fact[n]
    denominator = fact[k] * fact[n - k] % MOD

    ans = numerator * pow(denominator, MOD - 2, MOD) % MOD

    print(ans)
