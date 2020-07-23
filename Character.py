class Character(object):
    def __init__(self, name, cube):
        self.name = name
        self.level = 1
        self.health = 70
        self.maxHealth = 70
        self.alive = True
        self.cube = cube
        self.damage = 0
        self.defense = 0
        self.maxDefense = 0
        self.dodgeChance = 10
        self.frozen = False
        self.attackForMimic = "Nothing"
        self.valueForMimic = 0

    @staticmethod
    def pass_turn():
        print("You passed this turn!")

    # info about character
    def info(self, secondBarName, value, maxValue):
        print(f"{self.name}")
        print(self.draw_bar("Health", self.health, self.maxHealth))
        print(self.draw_bar(secondBarName, value, maxValue))
        print("For ability use write its number. For showing ability tooltip write its name.\n")

    # chance to dodge attacks and spells 10% + individual dodge
    def dodge(self):
        import random
        x = random.randint(1, self.dodgeChance)
        return x == 1

    # basic attack method
    def attack(self, enemy, typeOfAttack):
        blocked = 0
        damage = self.damage
        # attack only if both players are alive
        if self.is_alive():
            if enemy.is_alive():
                if not enemy.dodge():
                    damage += self.cube.throw()
                    armorValue = enemy.defense - damage
                    # if armorValue greater than 0 = we took 0 health from enemy but took his armor
                    if armorValue >= 0:
                        damage = 0
                        blocked = enemy.defense - armorValue
                        enemy.defense = armorValue
                    # armorValue less than 0 = our attack pierced through enemy armor and took his health
                    elif armorValue < 0:
                        enemy.health += armorValue
                        damage = armorValue * (-1)
                        blocked = enemy.defense
                        enemy.defense = 0
                        enemy.health = self.fix_health(enemy)

                    enemy.alive = enemy.is_alive()
                    self.attack_info(enemy, damage, typeOfAttack, blocked)
                else:
                    print(f"{enemy.name} dodged!")
                    if enemy.char == "Thief":
                        enemy.dodges += 5
                        enemy.dodge_fix()
            else:
                print(f"{enemy.name} is dead")
        else:
            print("You are dead")

    # set health on 0 if its below 0
    def fix_health(self, enemy):
        if enemy.health > 0:
            return enemy.health
        else:
            return 0

    # write info about cause damage
    def attack_info(self, enemy, damage, text, blocked):
        print(
            f"You dealt {damage} damage to {enemy.name} with {text}. {enemy.name} blocked {blocked} damage!")

    def spell_info(self, enemy, damage, text):
        print(f"You dealt {damage} damage to {enemy.name} with {text}.")

    # alive checker
    def is_alive(self):
        if self.health >= 1:
            return True
        else:
            return False

    # real damage number after attack throw and defense throw
    def armor_value(self, enemy):
        return enemy.defense - self.cube.throw()

    def armor_fix(self):
        if self.defense < 0:
            self.defense = 0
        if self.defense > self.maxDefense:
            self.defense = self.maxDefense

    # count visible pieces in hp bar
    def count_graphic_bar(self, number):
        starsNumber = (number * 2) // 10
        if 5 > number > 0:
            starsNumber = 1
        return starsNumber

    # draw hp bar
    def draw_bar(self, text, number, numberMax):
        bar = f"{text}: ["
        piece = "*"
        space = " "

        for x in range(0, self.count_graphic_bar(number)):
            bar += piece
        for y in range(0, self.count_graphic_space(numberMax, number)):
            bar += space
        bar += "]"

        return bar

    # count spaces in hp bar
    def count_graphic_space(self, numberMax, number):
        return (numberMax * 2) // 10 - self.count_graphic_bar(number)
