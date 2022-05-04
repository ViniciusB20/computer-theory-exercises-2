#-------------------------------------------------
# EXERCICIO 4 - LISTA 2
import random
numeros = []
dividido = []

for c in range (0, 15):
  rand = random.randint(0, 50)
  numeros.append(rand)
  #numeros.append(int(input(f'Digite o numero {c} : ')))
  
  if c == 0:
    maior = numeros[c]
  else:
    if numeros[c] > maior:
      maior = numeros[c]
    
for l in range (0, 15):
  valor = numeros[l]
  div = valor/maior
  dividido.append(div)


print("")
print('*' * 30)
print("")

print(f'Números : {numeros}')
print(f'O maior número é: {maior}')
print(f'Números depois da divisão: {dividido}')