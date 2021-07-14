#Laço de Repetição

a=True

if a:
    print("Mensagem")
print("FIM")


a=10
b=5

if a > b:
    print("O numero:",a,"e maior que o numero:",b)
if a < b:
    print("O numero:",b,"e maior que o numero:",a)
if a == b:
    print("Os numeros sao iguais:",a,b)
print("FIM")

op = "+"

if op == "+":
    print("Adicao")
elif op == "-":
    print("Subtracao")
elif op == "*":
    print("Multiplicacao")
elif op == "/":
    print("Divisao")
else:
    print("FIM")

nome = "joao"
anos = 25
habilitacao = True

# if condicional E

if nome == "joao" and anos > 18:
    print(nome,"e maior de idade!")
else:
    print(nome,"nao é maior de idade!")

print("\n")

# if condicional E com boolean

if nome == "joao" and (anos > 18 and habilitacao == True ):
    print(nome,"e maior de idade e pode Dirigir!")
else:
    print(nome,"nao é maior de idade!")

# if condicional OU

if nome == "joao" or anos == 20:
    print(nome,"Pode ir pra Guerra")
else:
    print(nome,"nao é maior de idade!")

print("\n")

# Laço For

array=["joao","maria","carlos","joana"]
print(array)

for x in array:
    
    if x == "joao" or x == "carlos":
        print("Menino")
    else:
        print("Menina")

array2 = ["branco","vermelho","azul","preto","verde"]

print("\n")

for x in array2:
    print(x)
    if x == "azul":
        break
print("fim")


print("\n")

for x in array2:
    if x == "azul":
        break
    print(x)
print("FIM")


