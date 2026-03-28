num1 = int(input('Diga o valor inicial: '))
num2 = int(input('Diga o valor final: '))
num3 = int(input('Diga o valor de incremento: '))
if num3 == 0:
    print('Essa progressão não faz efeito')
elif (num1 < num2 and num3 < 0) or (num1 > num2 and num3 > 0):
    print('Essa progressão não funciona com os valores indicados')
else:
    for i in range(num1,num2,num3):
        print(i)