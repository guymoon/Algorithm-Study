# https://www.acmicpc.net/problem/10971
# boj 10971 S2 외판원 순회 2 
# <메모리 : 129196, 시간 744>

import sys 
input = sys.stdin.readline
'''
#-------문제설명-----------
- 한 외판원이 어느 한 도시에서 출발 -> (N개의 도시)를 모두 거쳐 -> 다시 원래의 도시로 돌아오는 
- 한번 갔던 도시로는 갈 수 없음(맨 마지막에 출발 도시로 돌아오는 것 예외)
- 가정 적은 비용 
- 각 도시 이동 비용 W[i][j] i->j, 대칭적이지 않음
- W[i][i] = 0 이고 못가도 0
'''
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

ck = [False] * n 
visited = [] 
ans = float('inf')

def dfs(start, cnt, cur, cost):
    global ans 
    
    if cnt == n:
        if mat[cur][start] == 0:
            return 
        ans = min(ans, cost + mat[cur][start])
        return 
    
    for i in range(n):
        if ck[i] or mat[cur][i] == 0:
            continue 
        
        ck[i] = True
        dfs(start, cnt+1, i, cost+mat[cur][i])
        ck[i] = False
        
for i in range(n):
    ck[i] = True
    dfs(i, 1, i, 0)
    ck[i] = False
        
print(ans)
