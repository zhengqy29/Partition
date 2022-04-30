print('Loading data...')

f = open('PartitionsP_mod_5.txt', 'r')
temp_list = f.read().splitlines()
f.close()

print('Loading complete\nConverting data')

pm5 = list(map(lambda x: int(x), temp_list))

print('Converting complete')

f = open('PartitionsQ_mod_5.txt', 'w')
f.write('1\n')

for num in range(1, 10000000):
    if num % 10000 == 0: print(num)
    sum = pm5[num]
    power = -1
    for k in range(1, num+1):
        minusor = int(k*(3*k-1))

        if minusor <= num:
            sum += pm5[num - minusor] * power
        else: break

        minusor += 2*k
        if minusor <= num:
            sum += pm5[num - minusor] * power
        else: break

        power *= -1
    sum %= 5
    f.write(str(sum) + '\n')

f.close()