import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health



    def battle(self, opponent):
        '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        print(f"{self.name} battles {opponent}!")
    
        winner = random.choice([self, opponent])
        print(f"{winner} wins the battle!")



if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200

    my_hero1 = Hero("iron man", 200)
    print(my_hero1.name)            # iron man
    print(my_hero1.current_health)  # 200

    my_hero1.battle("Zombie flash")