n, x = map(int, input().split())
func = [[0, 1] for _ in range(30)]
for i in range(n):
    t, a = map(int, input().split())
    for j in range(30):
        if t == 1:
            func[j][0] &= bool(a & (1 << j))
            func[j][1] &= bool(a & (1 << j))
        elif t == 2:
            func[j][0] |= bool(a & (1 << j))
            func[j][1] |= bool(a & (1 << j))
        else:
            func[j][0] ^= bool(a & (1 << j))
            func[j][1] ^= bool(a & (1 << j))
    newx = 0
    for j in range(30):
        if func[j][bool(x & (1 << j))]:
            newx |= 1 << j
    x = newx
    print(x)

