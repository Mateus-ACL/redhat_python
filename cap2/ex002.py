num = float(input('Digite um número: '))
if num%1 != 0:
    print('Não é inteiro')
else:
    print('É inteiro')
    num = str(int(num))
    for digito in num:
        print(digito)