# 14889
from copy import deepcopy
import sys
N = int(sys.stdin.readline())
graph = []
sum = 0
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
def synergy(team):
    team_synergy = 0
    for i in range(len(team)):
        for j in team:
            team_synergy += graph[team[i]-1][j-1]
    return team_synergy
def combination(origin_list, combi_list, start, end):
    if len(stack) == end:
        combi_list.append(deepcopy(stack))
        return
    for i in range(start, len(origin_list)):
        
        stack.append(origin_list[i])
        combination(origin_list, combi_list, i+1, end)
        stack.pop()
    # 1,2 / 1,3/ 1,4/ 2,3 / 3,4 

team = N//2
combi = []
lists = []
num_list = list(range(1,N+1))
stack = []
min = sys.maxsize
combination(num_list,lists,0, team)
for i in range(len(lists)//2):
    if min == 0:
        break
    star_team = lists[i]
    link_team = lists[-i-1]
    gap = abs(synergy(star_team) - synergy(link_team))
    if gap<min:
        min = gap
print(min)