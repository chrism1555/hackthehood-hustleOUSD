import random
from ability import Ability
from armor import Armor



class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []

    def battle(self, opponent):
        '''Fight another hero and randomly declare a winner'''

        winner = random.choice([self, opponent.name])
        print(f"{winner} wins the battle!")

    def add_ability(self, ability):
        '''Appends an ability to a hero's list of attributes'''
        self.abilities.append(ability)

    def sum_of_attacks(self):
        '''Iterates through entire list of abilities and attacks'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block



if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("iron man", 200)
    print(my_hero.name)            
    print(my_hero.current_health) 
    ability1 = Ability("Explosion", 300)
    ability2 = Ability("Web shooter", 50)
    ability3 = Ability("Electrocution", 150)
    ability4 = Ability("Punch", 15)
    my_hero.add_ability(ability1)
    my_hero.add_ability(ability4)
    my_hero2.add_ability(ability2)
    my_hero2.add_ability(ability3)
    print(my_hero.abilities)
    print(my_hero2.abilities)