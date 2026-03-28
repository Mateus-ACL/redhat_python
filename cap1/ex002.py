nome = str(input('Digite seu nome: ')).strip()
sobrenome = str(input('Digite seu sobrenome: ')).strip()
completo = nome.split(' ')+sobrenome.split(' ')
print('seu nome é',end=' ')
for i in completo:
    print(i,end=' ')
print('')
print('Suas iniciais são:',end='')
for i in completo:
    print(i[0],end='')