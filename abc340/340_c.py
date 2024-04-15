import math
N = int(input())
#n_multipier=math.floor(math.log2(n))
n_multipier=len(bin(N))-3
two_multipier=N-pow(2,n_multipier)

ans=N*n_multipier+2*two_multipier
print(ans)

