n,m=map(int,input().split())
a=list(map(int,input().split()))
tmp_sum=sum(a[:m])
m_sum_max=0
for i in range(1,m+1):
    m_sum_max+=a[i-1]*i
m_sum_tmp=m_sum_max
for i in range(n-m):
    m_sum_tmp=m_sum_tmp-tmp_sum+a[i+m]*m
    m_sum_max=max(m_sum_max,m_sum_tmp)
    tmp_sum=tmp_sum-a[i]+a[i+m]
print(m_sum_max)
