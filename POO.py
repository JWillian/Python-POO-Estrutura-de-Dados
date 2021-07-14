class Boss:
    def  __init__(self,nome,forca,defesa,aura):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.aura = aura
    def info(self):
        print("\nNome:"+self.nome)
        print("Forca:"+str(self.forca))
        print("Defesa:"+str(self.defesa))
        print("Aura:"+str(self.aura))
        

class Baium(Boss):
    def  __init__(self):
        self.nome = "baium"
        self.forca = 100
        self.defesa = 100
        self.aura = 90
        super().__init__(self.nome,self.forca,self.defesa,self.aura)
    

class Antharas(Boss):
    def  __init__(self):
        self.nome = "Antharas"
        self.forca =200
        self.defesa = 200
        self.aura = 190
        super().__init__(self.nome,self.forca,self.defesa,self.aura)


    def info(self):
         super().info()

boss = Baium()
boss2 = Antharas()

boss.info()
boss2.info()