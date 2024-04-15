n,m=map(int,input().split())
a=list(map(int,input().split()))
inf=-2*10**5*2000*1000
dp=[[inf]*(m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    dp[i][0]=0
    for j in range(1,m+1):
        if j>i:
            continue
        dp[i][j]=max(dp[i-1][j-1]+a[i-1]*j,dp[i-1][j])

print(dp[-1][-1])`
