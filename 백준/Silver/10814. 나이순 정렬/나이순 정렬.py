N = int(input())
student_list = [[0 for col in range(3)] for row in range(N)]
for i in range(N):
    old, name = map(str, input().split())
    student_list[i][0] = int(old)
    student_list[i][1] = name
    student_list[i][2] = int(i)
student_list.sort(key= lambda  x: (x[0], x[2]))
for i in student_list:
    print(i[0], i[1]) 