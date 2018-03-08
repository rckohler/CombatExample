import random

class Guy():
    def __init__(self):
        self.attackSkill = 1
        self.defenseSkill = 1
        self.armor = 0

    def attack(self,victim):
        attackRoll = random.randint(1,20) + self.attackSkill
        defenseRoll = random.randint(1,20) + self.defenseSkill


    def receiveDamage(self,damage):
        pass


