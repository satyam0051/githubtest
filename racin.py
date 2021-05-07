def MinRacing(S):
    sub=0
    for i in range(2):
        skill=min(S)
        sub=abs(sub-skill)
        S.remove(min(S))
    print(sub)

N,T=map(int,input().rstrip().split())

for i in range(T):
    S=[int(input()) for j in range(N)]
    MinRacing(S)
