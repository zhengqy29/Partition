print('Loading data...')

f = open('PartitionsP_mod_5.txt', 'r')
temp_list = f.read().splitlines()
f.close()

print('Loading complete\nConverting data')

pm5 = list(map(lambda x: int(x), temp_list))

print('Converting complete')

print('Loading data...')

f = open('PartitionsQ_mod_5.txt', 'r')
temp_list = f.read().splitlines()
f.close()

print('Loading complete\nConverting data')

Qm5 = list(map(lambda x: int(x), temp_list))

print('Converting complete')

f = open('result.txt', 'w')
f.write('1\n0\n')

for num in range(1, 5000000):
    num2 = 2 * num
    if num2 % 10000 == 0: print(num2)

    sum = 0

    for i in range(0, int(num2/6)+1):
        sum += Qm5[2*i] * pm5[num - 3*i]
    sum %= 5

    f.write(str(sum) + '\n')

    num2 += 1
    sum = 0
    for i in range(0, int((num2-3)/6)+1):
        sum += Qm5[2*i+1] * pm5[num - 1 - 3*i]
        sum %= 5

    f.write(str(sum) + '\n')

f.close()