class Person:

    def __init__(self, name, hp = 10, base_attak = 1, base_protection = 0.2):
        self.name = name
        self.hp = hp
        self.base_attak = base_attak
        self.base_protection = base_protection

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, уровкнь жизни: {self.hp}, атака: {self.base_attak}, процент защиты: {self.base_protection}.'


class Paladin(Person):

    def __init__(self, name):
        super().__init__(name)
        self.hp *= 2
        self.base_protection *= 2


class Warrior(Person):

    def __init__(self, name):
        super().__init__(name)
        self.base_attak *= 2

pers1 = Paladin('Gorr')
pers2 = Warrior('Bishop')

print(pers1)
print(pers2)