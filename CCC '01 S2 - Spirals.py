# start = int(input())
# endd = int(input())
# number_of_numbers = endd - start + 1
# directions_horizontal = [1, -1]
# directions_vertical = [1, -1]
# grid = [[" "] * 100 for _ in range(100)]

# row = 50
# col = 50

# current_num = start
# steps_to_take = 1

# grid[row][col] = str(current_num)

# while current_num < endd:
#     for direction in range(2):
#         for _ in range(steps_to_take):
#             if current_num >= endd:
#                 break
#             row += directions_vertical[direction]
#             col += directions_horizontal[direction]
#             current_num += 1
#             grid[row][col] = str(current_num)
#     steps_to_take += 1
# print(grid)

start = int(input())
endd = int(input())
number_of_numbers = endd - start + 1
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
grid = [[" "] * 100 for _ in range(100)]

row = 50
col = 50

current_num = start
steps_to_take = 1

grid[row][col] = str(current_num)


idx = 0

while current_num < endd:
    for i in range(2):  # iterate through the four directions
        for _ in range(steps_to_take):
            if current_num >= endd:
                break
            row += directions[idx][0]
            col += directions[idx][1]
            current_num += 1
            grid[row][col] = str(current_num)
            
            
        idx = (idx + 1) % 4
    steps_to_take += 1
            

print(grid)


            