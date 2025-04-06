class Character:
    def __init__(self,name,health,attack_power,defense,speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    def attack(self,target):
        pass

    def take_damage(self,amount):
        pass

    def is_alive(self):
        pass

class Warrior(Character):
    def __init__(self,name,health,attack_power,defense,speed,rage):
        super().__init__(name,health,attack_power,defense,speed)
        self.rage = rage
    def berserkmode(self):
        if self.health < 30:
            self.attack_power *= 2 
        print(self.attack_power)    
class Mage(Character):
    def __init__(self,name,health,attack_power,defense,speed,mana):
        super().__init__(name,health,attack_power,defense,speed)
        self.mana = mana    
    def fireball(self):
        pass    
class Archer(Character):
    def __init__(self,name,health,attack_power,defense,speed,critical_chance):
        super().__init__(name,health,attack_power,defense,speed,)
        self.critical_chance = critical_chance 
    def precision_shot(self):
        pass  
w_obj = Warrior("john",4,1,10,2,8)
m_obj = Mage("vijay",2,3,4,5,6)

# obj.berserkmode()
print(w_obj.name)
print(m_obj.name)






