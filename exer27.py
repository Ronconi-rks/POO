from abc import ABC, abstractmethod
from rich.panel import Panel
from  rich import print
import random
from random import randint

class Personagem(ABC):
    access_Guerreiro = lambda self: self.golpes
    access_Mago = lambda self: self.golpes
    def __init__(self,nome, vida):

        self.nome = nome
        self.vida = vida


    def atacar(self,alvo,forca=0):
        ataque = randint(0,forca)
        return f'{self.nome}[cyan]({self.vida})[/] atacou [blue]{alvo.nome}({alvo.vida})[/] com um [bold blue]{self.golpes}[/] de força {forca}, [blue]{alvo.nome}[/] [red]recebeu dano de {ataque}[/]'

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    golpes = ['Soco', 'Ataque esmagador', 'Golpe giratório']
    sorteiag = random.choice(golpes)
    def __init__(self,nome,vida):
        super().__init__(nome, vida)
        self.golpes = random.choice(Guerreiro.golpes)

    def curar(self):
        cura = randint(0,self.vida)
        return f'[bold cyan]{self.nome}[/] comeu uma carne e recuperou {cura} pontos de vida '


class Mago(Personagem):
    magias = ['Bola de fogo', 'Magia congelante', 'Chuva de espinhos']
    def __init__(self,nome,vida):
        super().__init__(nome, vida)
        self.golpes = random.choice(Mago.magias)

    def curar(self):
        cura = randint(0,self.vida)
        return f'[bold cyan]{self.nome}[/] tomou uma poção de vida e recuperou {cura} pontos de vida '

p1 = Mago('Dinossauro',2000)
p2 = Guerreiro('Bruto',2020)
p3 = Mago('Feiticeira',3000)
print(p3.atacar(p2,4000))
print(p1.atacar(p2,1000))
print(p1.curar())


print(p2.atacar(p1,2000))
print(p2.curar())



