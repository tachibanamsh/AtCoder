h,w=map(int,input().split())
g_map=[]
for i in range(h):
    hw=list(map(str,input()))
    g_map.append(hw)
h_pos=0
w_pos=0
attempt_num=0
attempt_max=h*w+20
while True:
    tmp=g_map[h_pos][w_pos]
    if tmp=='U' and h_pos>0:
        h_pos-=1
    elif tmp=='U' and h_pos==0:
        print(str(h_pos + 1) + " " + str(w_pos + 1))
        exit()
    elif tmp=='D' and h_pos<h-1:
        h_pos+=1
    elif tmp=='D' and h_pos==h-1:
        print(str(h_pos + 1) + " " + str(w_pos + 1))
        exit()
    elif tmp=='L' and w_pos>0:
        w_pos-=1
    elif tmp=='L' and w_pos==0:
        print(str(h_pos + 1) + " " + str(w_pos + 1))
        exit()
    elif tmp=='R' and w_pos<w-1:
        w_pos+=1
    elif tmp=='R' and w_pos==w-1:
        print(str(h_pos + 1) + " " + str(w_pos + 1))
        exit()

    attempt_num+=1
    if attempt_num>attempt_max:
        print(-1)
        exit()
