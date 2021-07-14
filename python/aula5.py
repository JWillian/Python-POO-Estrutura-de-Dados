#Input

import os

os.system('CLS')

nome=input("digite seu nome:")
print(nome)

sobrenome=input("digite seu sobrenome:")
print(sobrenome)

NomeInteiro = nome+sobrenome

print("Nome:",NomeInteiro)

num1=int(input("Num1:"))
num2=int(input("Num2:"))


print("fim")

print("\n")

print("Escolha um operador 1--> Adicao / 2--> Subtracao / 3--> Multiplicacao / 4-->Divisao")

op=int(input("OP:"))

if(op==1):
    res=num1+num2
    print("Resultado:",res)
elif(op==2):
    res=num1-num2
    print("Resultado:",res)
elif(op==3):
    res=num1*num2
    print("Resultado:",res)
elif(op==4):
    res=num1/num2
    print("Resultado:",res)
print("FIM")


x=input(":")