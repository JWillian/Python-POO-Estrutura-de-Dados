#While

import os


i=0

while i <9:
    print(i)
    i+=1
print("FIM")

print("\n")


x=0

while x<9:
    print(x)
    x+=1
    if(x>=5):
        break
print("FIM")


print("\n")

y=9

while y>=1:
    print(y)
    y-=1
    if(y<=5):
        break


#Laço de Carros


carros=["ford","BMW","WOLKS","Mercedez"]

i=0

tam=len(carros)

while i < tam:
    print(carros[i])
    i+=1
print("FIM")

i=0

cores=[]
cores=input("Digite sua cor: ")

while cores != "-1":
    cores.append(cores)
    cores=input("Digite sua cor: ")
    

os.system('cls')

for x in cores:
    print(x)


print("FIM")