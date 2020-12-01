def draw_triangle(N):
    for i in range(1,N):
        print('*'+' '*(i-2)+('*' if i > 1 else ''))
    for i in range(N,0,-1):
        print('*'+' '*(i-2)+('*' if i > 1 else ''))
draw_triangle(int(input()))