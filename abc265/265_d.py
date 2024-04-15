N,P,Q,R = list(map(int, input().split()))
A = list(map(int, input().split()))
#
ns = [P, P + Q, P + Q + R]
#
import itertools
B = [0] + list(itertools.accumulate(A))
C = set(B)
for i in range(N):
    b = B[i]
    for n in ns:
        if n + b not in C:
            break
    else:
        print('Yes')
        exit()
#
print('No')

