from array import array
import random


num_i=10
num_f=5.2
num_c=1j

x=num_i

print("valor:"+str(x)+"\n tipo:"+str(type(x)))


#Criando uma variavel que receba 6 numeros de 1 a 50 com a funcao Random.randrange!
num = [random.randrange(1,50)]

num2= [
    random.randrange(1,50),
    random.randrange(1,50),
    random.randrange(1,50),
    random.randrange(1,50),
    random.randrange(1,50)
]

print(num)

print("\n",num2)

# STRINGS


msg = "Mensagem"

print(msg[0])
print(msg[0:3])
print("Tamanho:",len(msg),"caracteres.") # Len() Quantidade de Caracteres
print(msg.lower())                       #Lower() Tudo Minusculo
print(msg.upper())                       #Upper() Tudo Maiusculo
print(msg.replace("e","o"))              #Replace() Troca um palavra ou letra por outra.


#Concatenação de STRINGS

nome = "Jonatas"
sobrenome ="Willian"

res = nome+"  "+sobrenome
print(res)

dia = 5
mes = 3
ano = 2020

print("Dia:",dia,"Mes:",mes,"Ano:",str(ano))
