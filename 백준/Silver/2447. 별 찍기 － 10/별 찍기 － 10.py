def draw_star(n):
    if n == 1:
        return '*'
    stars = draw_star(n//3)
    tmp_star = []
    for star in stars:
        tmp_star.append(star*3)
    for star in stars:
        tmp_star.append(star + ' '*(n//3)+ star)
    for star in stars:
        tmp_star.append(star*3)
    return tmp_star
    
N = int(input())
S = draw_star(N)
print('\n'.join(S))