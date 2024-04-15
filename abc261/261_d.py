N, M = map(int, input().split())
X = list(map(int, input().split()))
B = {}
for _ in range(M):
    C, Y = map(int, input().split())
    B[C] = Y
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(i+1):
        bonus = 0
        if j+1 in B:
            bonus = B[j+1]
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i]+bonus)
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])
print(max(dp[N]))
