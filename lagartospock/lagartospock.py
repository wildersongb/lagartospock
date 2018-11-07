import random
class Game(object):

    rules = {
      'piedra':['tijera','lagarto'], 
      'papel':['spock','piedra'],
      'tijera':['lagarto','papel'],
      'lagarto':['spock','papel'],
      'spock':['tijera','piedra'],
    }

    def __init__(self, Player1, Player2):
        self.p1 = Player1
        self.p2 = Player2
    
    #arreglar aqui
    def play(self, choice1, choice2):
    	p1choice=str(choice1)
    	p2choice=choice2

    	if p1choice and p2choice in self.rules:
    		if p1choice==p2choice:
    			return 'Empate'
    		else:
    			if p1choice in self.rules[p2choice]:
    				
    				return "Player 2 gana"#"Gana {}, de {}".format(p2choice, self.p2)
    				
    				
    			else:
    				return "Player 1 gana" #"Gana {}, de {}".format(p1choice, self.p1)
    	else:
    		return "ingrese un valor valido"

    @classmethod
    def vspc(cls, player):
        pc=Pc()
        return cls(player, pc)
    
        
class Player(object):
	"""docstring for ClassName"""
	def __init__(self, name="player"):
		self.name = name
		#self.choice=choice
	def Choice(self, choice):
		return choice

	def __str__(self):
		return self.name
class Pc(object):
    def __init__(self):
        self.name="Computadora"
    
    def randomc(self):
        choice=random.choice(['piedra', 'papel', 'tijera', 'lagarto','spock'])
        print("Pc escogio {}".format(choice))
        return choice
    def __str__(self):
        return self.name


if __name__ == '__main__':
    while True:
        print("Opciones:'piedra', 'papel', 'tijera', 'lagarto','spock")
        vs=input("para jugar contra Pc 2 /n contra un amigo 1: ")
        if vs=="2":
            a=Game.vspc(Player(input("ingrese nombre de jugador 1: ")))
            a=a.play(a.p1.Choice(input("Ingrese su mano jugador 1: ")), a.p2.randomc())
            print(a)
        else:
            a=Game(Player(input("ingrese nombre de jugador 1: ")),Player(input("ingrese nombre de jugador 2: ")))
            a=a.play(a.p1.Choice(input("Ingrese su mano jugador 1: ")), a.p2.Choice(input("Ingrese su mano jugador2: ")))
            print(a)


