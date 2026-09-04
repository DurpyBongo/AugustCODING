x, y = map(int, input().split())

start_x, start_y = 0, 0


while True:
    move_x, move_y = map(int, input().split())
    if move_x == 0 and move_y == 0:
        break
    start_x = start_x + move_x
    start_y = start_y + move_y
    if start_x <0:
        start_x = 0
    elif start_x > x:
        start_x = x
    if start_y < 0:
        start_y = 0
    if start_y > y:
        start_y = y
    print(start_x, start_y)
