class Hero:
    count = 0

    def __init__(self, name, health):
        Hero.count += 1
        self.name = name
        self.health_value = health

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health_value

    def set_new_health(self, new_health):
        self.health_value = new_health

hero_1 = Hero("Pinkie", 20)
hero_2 = Hero("Applejack", 21)
hero_3 = Hero("Rarity", 23)

# print(hero_1.get_name())
# print(hero_2.get_name())
#
# hero_1.set_new_health(21)
# hero_2.set_new_health(22)
# print(hero_1.health_value)

print(Hero.count)

