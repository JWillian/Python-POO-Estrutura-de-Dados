#Tuplas

l_carros=["HRV","BMW","Mercedez","Mesarati"]
t_carros=("HRV","BMW","Mercedez","Mesarati")

#Converter tupla com list

l_carros=list(t_carros)
l_carros[2]="focus"

#Converter lista com tuple

t_carros=tuple(l_carros)


for x in t_carros:
    print(x)
