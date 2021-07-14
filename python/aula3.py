#Booleans

falso = False
verdadeiro = True

if 10 > 5 :
    print(verdadeiro)
else:
    print(falso)
print("FIM")

#Ver se existe algo dentro da variavel.

var = "conteudo"
print(bool(var))

texto = ""
if texto:
    print(verdadeiro)
else:
    print("Nao existe conteudo:",falso)
print("FIM")

#Valores diferente de 0 retornam True e igual a 0 False.

valor1 = 0
valor2 = 8

print("Valor 1:",bool(valor1),"\nValor 2:",bool(valor2))



#List

carros=["Maserati","ferrari","BMW","Mercedez"]
print(carros)

#Apend adiciona um novo item.

carros.append("Ford")
print(carros)

#Remove remove um item
carros.remove("Maserati")
print(carros)

#len conta a quantidade de Carros

print("Quantidade de Carros:",str(len(carros)))

#pop Remove o ultimo elemento da pilha.
carros.pop()
print(carros)
carros.pop()
print(carros)

#del deleta um elemento pelo indice
del carros[1]
print(carros)

#Clear limpa todos elementos da lista.
carros.clear()
print(carros)
carros=["Maserati","ferrari","BMW","Mercedez"]

#List faz uma lista
NovosCarros = list(carros)
print(NovosCarros)

#Concatenar Listas
carros=["Maserati","ferrari","BMW","Mercedez"]
CorDosCarros = ["Preto","Vermelho","Azul","Amarelo"]

lista = carros+CorDosCarros
print(lista)







