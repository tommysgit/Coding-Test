x, y, w, h = map(int, input().split())
hMin = (h-y) if y>(h-y) else y
wMin = w-x if x>(w-x) else x
output = hMin if hMin<wMin else wMin

print(output)