num_lines, num_letters = map(int, input().split())
for i in range(num_lines):
    line = input()
    charactesr = list(line)
    light_heavy = 0
    output = 'T'
    for u in range(len(charactesr)):
        if charactesr.count(charactesr[u])>1:
            if light_heavy == 0:
                light_heavy =2 # 1 is light, 2 is heavy
            elif light_heavy == 1:
                light_heavy = 2
            elif light_heavy == 2:
                output = 'F'
                break
        elif charactesr.count(charactesr[u])==1:
            if light_heavy ==2:
                light_heavy = 1
            elif light_heavy == 0:
                light_heavy = 1
            elif light_heavy == 1:
                output = 'F'
                break

    print(output)
            