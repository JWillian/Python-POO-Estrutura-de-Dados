#Funções
num1=2
num2=3

def somar():
    res=num1+num2
    print("\nresultado da SOMA:"+str(res))

somar()    

def subtrair():
    

    if(num1<num2):
        print("\nO numero nao e Valido!!! \n FIM")
    elif(num1>num2):
        res = num1-num2
        print("resultado da SUBTRACAO:"+str(res))


subtrair()

def calc():
    somar()
    subtrair()

calc()


# Funcao com parametros de entrada.

def somar(n1,n2):
    r=n1+n2
    print("\n A Soma e:"+str(r))

somar(4,4)

def textos(*txt):
    for t in txt:
        print(t)

textos("\nJoao","Maria","Jonatas","Luciana")

def somar2(*num):
    r=0
    for n in num:
        r+=n
        print("Soma:"+str(r))

print("\n")
somar2(1,2,3,4)


def carros(c,cor="Preto"):
    print("\nModelo:"+c+"  Cor:"+cor)

carros("Suv")


valores=[1,5,3,2]

def somar(num):
    r=0
    for n in num:
        r+=n
    return r

r=somar(valores)

print("\nA soma dos numeros: "+str(valores)+" e de: "+str(somar(valores)))

#ou retorno com parametro R

print("\nA soma dos numeros: "+str(valores)+" e de: "+str(r))