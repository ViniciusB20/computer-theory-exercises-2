#-------------------------------------------------
# EXERCICIO 5 - LISTA 2
import random
import string

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))

def usuario (nome:str, sobrenome:str):
  return nome[0]+sobrenome

def senha(tamanho = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""

    for i in range(0, tamanho):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

senha_gerada = senha(tamanho = 8)

print("")
print('*' * 30)
print("")
print("Username :", usuario(nome,sobrenome))
print(f"Senha : {senha_gerada}")