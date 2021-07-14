


print("ola")

#As variaveis São Dinamicas !! elas recebem seu tipo automaticamente.

nome = "jose"
idade = 28

nota1 = 5
nota2 = 5

#A virgula separa as variaveis E o + concatena as Variaveis.

print("Meu nome e:",nome,"e eu tenho",idade,"anos!")

print(nota1,nota2)

""" Este é um
Comentário de Multiplas 
Linhas """ 

#Variaveis recebem outras viriaveis com o ultimo endereço.
num1=num2=res=0

#Laço  de IF e ELSE em Pyton!
if 2 > 5:
    print("Maior")
else:
    print("Menor")
print("FIM")




#Estrutura da função!!
#retorna a Mensagem como retorno. A mensagem existe apenas dentro da função.
def func():
    mensagem = "Isso e o retorno de uma funcao!!"
    print(mensagem) 

func()



#Transformando a variavel mensagem em global dentro do escopo da função.
def func():
    global mensagem
    mensagem = "Isso e o retorno de uma funcao!!"
    print(mensagem) 

func()

#chamando a variavel mensagem pois transformei ela em global.
print(mensagem)

#verificar o Tipo da Variavel
x=1
print("valor:"+str(x))
print("Tipo:"+str(type(x)))


x=1
x="String"
x=1.5
x=True
n1=5;n2=2;x=complex(n1,n2)

print(x.real)
print(x.imag)

#Array
array=["Rapaz","Menina","Crianca"]

#Array com varios tipos de variavel.
array2=["Menina","Rapaz","Crianca",1.5,3,True] 


print(array)
print(array[0])
print(array[1])
print(array[2])

#tupla
tupla=("Menina","Rapaz","Crianca")

#Criando um List facil com a func RANGE de 0 a 100.
array3=range(0,100,1)

print("valor:"+str(array3[10]))
print("Tipo:"+str(type(array3)))

#Chaves / Diconário.
chave={
    "primeiro":"1",
    "Segundo":"2",
    "Terceiro":"3"
}
print("Valor:"+chave["primeiro"])

#SET, quando ele é chamado, o mesmo, não repete Valores.
chave2={2,3,4,5,6,7,8,3,5}
print("Numeros:",chave2)
print("Tipo"+str(type(chave2)))






