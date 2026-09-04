plain = input()
cipher = input()
solve = input()

masterlist = {}
for i in range(len(plain)):
    masterlist[cipher[i]] = plain[i]

rawr = set()
hehe = set()
alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '}
if len(masterlist) == 26:
    for key,value in masterlist.items():
        rawr.add(value)
        hehe.add(key)
    cipher_missing = list(alphabet.difference(rawr))[0]
    cipher_answer = list(alphabet.difference(hehe))[0]
    masterlist[cipher_answer] = cipher_missing
        
for u in range(len(solve)):
    print(masterlist.get(solve[u], '.'), end='')
print('')

