import random
import os

#Este jogo tem como objetivo acertar um numero aleatorio em X vezes.

erros=0
sortedado=random.randrange(0,20)
jogador=int(input("Digite seu numero: "))

while(sortedado!=jogador):
    os.system('cls')
    if(sortedado>jogador):
        print("Erro,O Numero e maior")
    elif(sortedado<jogador):
        print("Erro,O Numero e menor")
    erros+=1
    jogador=int(input("Digite seu numero: "))

print("Numero",str(jogador),"voce acertou em",str(erros+1),"tentativas.")

nome=input("Digite seu nome:")
print("O Vencedor é:",nome)



