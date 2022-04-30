pm5 = [1]

f = open('PartitionsP_mod_5.txt', 'w')
f.write('1\n')

for num in range(1, 100):
    if num % 10000 == 0: print(num)
    sum = 0
    power = 1
    for k in range(1, num+1):
        minusor = int(k*(3*k-1)/2)

        if minusor <= num:
            sum += pm5[num - minusor] * power
        else: break

        minusor += k
        if minusor <= num:
            sum += pm5[num - minusor] * power
        else: break

        power *= -1
    sum %= 5
    pm5.append(sum)
    f.write(str(sum) + '\n')

f.close()