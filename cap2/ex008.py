num = (int(input('digite um número: ')), int(input('digite um número: ')))
numsorted = sorted(num)
soma = 0
for i in range (numsorted[0],numsorted[1]+1):
    soma+=i
    print(soma)