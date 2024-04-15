n=int(input())
s=[]
for _ in range(n):
    si=input()
    s.append(si)
from collections import defaultdict
s_dic=defaultdict(int)
for i in range(n):
    s_dic[s[i]]+=1
    if s_dic[s[i]]==1:
        print(s[i])
    else:
        print(s[i]+'('+str(s_dic[s[i]]-1)+')')
