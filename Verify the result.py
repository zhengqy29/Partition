print('Loading data...')

f = open('p-1m1001.txt', 'r')
temp_list = f.read().splitlines()
f.close()

print('Loading complete\nConverting data')

gm1001 = list(map(lambda x: int(x), temp_list))

print('Converting complete')

def JacobiSymbol_mod_11(num):
    num %= 11
    if num == 0: return 0
    elif num == 1 or num == 3 or num == 4 or num == 5 or num == 9: return 1
    else: return -1

f = open('result.txt', 'w')

part2 = 2

for num in range(0, 1068):
    sum = gm1001[847*num+247] + 4*JacobiSymbol_mod_11(2*num+7)*gm1001[7*num+2]

    if num % 121 == 35:
        sum += gm1001[part2]
        part2 += 7

    sum %= 7

    f.write(str(num) + ' ' + str(sum) + '\n')

f.close()