num = (int(input('digite um número: ')), int(input('digite um número: ')))
numsorted = sorted(num)
soma = 0
for i in range (num[0],num[1]+1):
    soma+=i
print(soma)