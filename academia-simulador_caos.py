import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 ==0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()
    
    def reiniciar_o_dia(self):
        self.porta_halteres = {i:i for i in self.halteres}
    
    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def pegar_haltere(self, peso):
        halt_pos = [self.porta_halteres.values()].index(peso)
        key_halt = [self.porta_halteres.keys()][halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso
    
    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)

self = Academia()
