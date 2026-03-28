frase = str(input('Digite uma frase: ')).lower()
lista = []
if format(ord(frase[-1]), "08b") == '00101110':
    print('termina com ponto')
for i in frase:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in lista:
            lista.append(i)
if len(lista) == 26:
    print('Tem todas as letras')
if 'x' in lista:
    print('Tem x na lista')
if 'e' in lista:
    print(frase.replace('e','E'))