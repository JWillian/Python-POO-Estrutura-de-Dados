# POO com PYTHON

#Classe NPC com seus Atributos.

class NPC:
    def __init__(self,nome,time,forca,municao,cura):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.minucao = municao
        self.life=True
        self.cura = cura
    def info(self):
        print("Nome:"+self.nome)
        print("Time:"+str(self.time))
        print("Forca:"+str(self.forca))
        print("Municao:"+str(self.municao))
        print("Life:"+("Vivo" if self.life else "Morto"))
        print("Energia:"+str(self.energia))
        print("Cura:"+str(self.cura)+"\n")



#Herança

# QUando vc cria um construtor na classe que vai herda, ele sobrescreve o construtor da classe herdada, Classe pai !!! a NPC.

# No construtor da classe que vai herdar, você precisa colocar todos os parametros da classe herdada.

#O metodo Super() faz a herança dos atributos.

#Apos chamar o Super, deve chamar o construtor e passar os parametros novamente.

class soldado(NPC):
    def __init__(self,nome,time):
        self.forca = 50
        self.municao = 50
        self.cura = 10
        super().__init__(nome,time,self.forca,self.municao,self.cura)


class guarda(NPC):
    def __init__(self,nome,time):
        self.forca = 100
        self.municao = 100
        self.cura = 50
        super().__init__(nome,time,self.forca,self.municao,self.cura)


class healer(NPC):
    def __init__(self,nome,time):
        self.forca = 50
        self.municao = 20
        self.cura = 100
        super().__init__(nome,time,self.forca,self.municao,self.cura)
    def inf(self):
            super().info()
            
ob1 = guarda("castor",1)
ob2 = soldado("Aster",1)    
ob3 = healer("Isis",1)
ob4 = soldado("Melko",2)
ob5 = guarda("ilidan",2)
ob6 = healer("Alicia",2)

ob1.info()
ob2.info()
ob3.info()
ob4.info()
ob5.info()
ob6.info()

