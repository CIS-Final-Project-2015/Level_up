import testClass
##########################################################
xpRequired = [0,2000,5000,9000,15000,23000,35000,51000,75000,105000,155000,220000,315000,445000,635000,890000,1300000,1800000,2550000,3600000]
party = testClass.players
class Level_Up(object):

    def levelUp(character, level):
        character.level += 1
        points = Level_Up.calcPoints(character)

    def applyXP(character, totalXp):
        print(character.level)
        character.xp += (totalXp / 4)
        if character.xp > xpRequired[character.level]:
            Level_Up.levelUp(character, character.level)
                    
    def calcPoints(character):
        if character.charClass == "Mage":
            points = 2 + character.int_Mod
        elif character.charClass == "Cleric":
            points = 2 + character.int_Mod
        elif character.charClass == "Rogue":
            points = 8 + character.int_Mod
        elif character.charClass == "Fighter":
            points = 4 + character.int_Mod
        else:
            points = 0
        return points
##################################################


def main(party, xpRequired):
    totalXp = 0 # we will import this from encounters
    for character in party:
        print(character.name)
        Level_Up.applyXP(character, totalXp)
Level_Up()
main(party, xpRequired)
