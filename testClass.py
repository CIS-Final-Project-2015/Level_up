class Player(object):
 
    def __init__(self, name, health, xp, charClass, level, int_Mod):
        self.health = health
        self.name = name
        self.xp = xp
        self.charClass = charClass
        self.int_Mod = int_Mod
        self.level = level
        
Dave = Player("Dave", 3, 2000, "Mage", 2, 10)
Raulph = Player("Raulph", 22, 35000, "Cleric", 6, 15)
Hannah = Player("Hannah", 10, 15250, "Rogue", 4, 20)
Nick = Player("Nick", 2, 0, "Fighter", 1, 25)



players = [Dave, Raulph, Hannah, Nick]
