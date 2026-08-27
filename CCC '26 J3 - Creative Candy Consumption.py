from collections import deque

first = input()
second = input()

alex = deque(first)
ethan = deque(second)

alex_count = 0
ethan_count = 0

maximum = max(len(alex), len(ethan))
while len(alex) > 0 and len(ethan) > 0:
    if alex[0] == ethan[0]:
        alex.popleft()
        ethan.popleft()
        alex_count+=1
        ethan_count+=1
    elif alex[0] == 'R' and ethan[0] == 'G':
        ethan.popleft()
        alex_count+=1
    elif alex[0] == 'G' and ethan[0] == 'R':
        alex.popleft()
        ethan_count+=1
    elif alex[0] == 'G' and ethan[0] == 'B':
        ethan.popleft()
        alex_count+=1
    elif alex[0] == 'B' and ethan[0] == 'G':
        alex.popleft()
        ethan_count+=1
    elif alex[0] == 'B' and ethan[0] == 'R':
        ethan.popleft()
        alex_count+=1
    elif alex[0] == 'R' and ethan[0] == 'B':
        alex.popleft()
        ethan_count+=1
if len(alex) > len(ethan):
    alex_count += len(alex)
elif len(ethan) > len(alex):
    ethan_count += len(ethan)

print(alex_count)
print(ethan_count)