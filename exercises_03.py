#-------------------------------------------------
# EXERCICIO 3 - LISTA 2
import random

matriz = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

for l in range(0, 10):
  for c in range(0, 10):
    matriz[l][c] = random.randint(0, 255)

print("")
print('*' *30, '10X10', '*' *30)
print("")

for l in range(0, 10):
  for c in range(0, 10):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()