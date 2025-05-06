ss = [0, 0, 0]
cnt3 = [0, 0, 0]
cnt2 = [0, 0, 0]

for _ in range(int(input())):
    vote = list(map(int, input().split()))
    for i in range(3):
        ss[i] += vote[i]
    cnt3[vote.index(3)] += 1
    cnt2[vote.index(2)] += 1

mxs = max(ss)
cs = [i for i in range(3) if ss[i] == mxs]

if len(cs) == 1:
    print(cs[0] + 1, mxs)
else:
    max_cnt3 = max(cnt3[i] for i in cs)
    cs = [i for i in cs if cnt3[i] == max_cnt3]

    if len(cs) == 1:
        print(cs[0] + 1, mxs)
    else:
        max_cnt2 = max(cnt2[i] for i in cs)
        cs = [i for i in cs if cnt2[i] == max_cnt2]

        if len(cs) == 1:
            print(cs[0] + 1, mxs)
        else:
            print(0, mxs)