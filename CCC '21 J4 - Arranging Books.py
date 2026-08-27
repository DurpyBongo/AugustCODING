book = input()
many_book = list(book)
L_count = many_book.count('L')
M_count = many_book.count('M')

M_inL = many_book[:L_count].count('M')
S_inL = many_book[:L_count].count('S')

L_inM = many_book[L_count:L_count + M_count].count('L')
S_inM = many_book[L_count:L_count + M_count].count('S')

lm = min(M_inL, L_inM)

total = S_inL + S_inM + L_inM + M_inL -lm
print(total)