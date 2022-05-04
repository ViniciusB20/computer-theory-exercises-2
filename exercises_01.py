#-------------------------------------------------
# EXERCICIO 1 - LISTA 2
numeros = []
impar = []
par = []

for c in range (0, 10):
  numeros.append(int(input(f'Digite o numero {c} : ')))

  if numeros[c] % 2 == 0:
    par.append(numeros[c])
  else:
    impar.append(numeros[c])  
  if c == 0:
    maior = menor = numeros[c]
  else:
    if numeros[c] > maior:
      maior = numeros[c]
    if numeros[c] < menor:
      menor = numeros[c]    

media = sum(numeros)/len(numeros)

print("")
print('*' * 30)
print("")

print(f'Números pares : {par}')
print(f'Números ímpares : {impar}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A média dos números é: {media}')