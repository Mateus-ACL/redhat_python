frase = str(input('Digite uma frase: '))
prim_le = frase[0]
prim_le_rep = frase.count(prim_le) 
ult_le = frase[-1]
ult_le_rep = frase.count(ult_le) 
print(f'a primeira letra é "{prim_le}" e se repete {prim_le_rep} vez(es)')
print(f'a ultima letra é "{ult_le}" e se repete {ult_le_rep} vez(es)')

