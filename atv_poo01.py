
#usar execução interativa do jupyter

class Circulo:
    def __init__(self, raio = 1): #atributos/função
        self.raio = raio

    def calcula_area(self):
        return self.raio * self.raio * 3.14 #metodos/função
    
    def retorna_raio(self):
        return self.raio
    
c1 = Circulo()
c2 = Circulo(2)

c1.calcula_area()
c2.calcula_area()

c1.retorna_raio()
c2.retorna_raio()