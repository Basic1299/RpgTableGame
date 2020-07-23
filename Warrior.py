from Character import Character
from Tooltips import Tooltips
import os


class Warrior(Character):
    def __init__(self, name, cube):
        super().__init__(name, cube)
        self.char = "Warrior"
        self.damage = 4
        self.defense = 10
        self.maxDefense = 20
        self.health = 100
        self.maxHealth = 100
        self.dodgeChance = 9

    def armor_up(self):
        armorAdd = self.cube.throw() + 3
        if self.defense < self.maxDefense:
            print("Gaining more armor!")
            self.defense += armorAdd
            self.armor_fix()
        else:
            print("Armor is already full. You missed your chance this turn!")

    def decision(self, enemy, game_round):
        loop = True
        if self.alive and enemy.alive:
            if not self.frozen:
                while loop:
                    os.system('clear')
                    print(f"Round {game_round}")
                    self.info("Armor", self.defense, self.maxDefense)
                    x = input("Sword swing(1)  Armor up(2)  Armor bash(3)  Pass(4)\n>").replace(" ", "").lower()
                    if x == "1":
                        self.attack(enemy, "sword")
                        break
                    elif x == "2":
                        self.armor_up()
                        break
                    elif x == "3":
                        self.armor_bash(enemy)
                        break
                    elif x == "4":
                        Character.pass_turn()
                        break
                    elif x == "swordswing":
                        Tooltips.tip_sword_swing()
                    elif x == "armorup":
                        Tooltips.tip_armor_up()
                    elif x == "armorbash":
                        Tooltips.tip_armor_bash()

            else:
                self.info("Armor", self.defense, self.maxDefense)
                print("You are frozen this turn and can't move...")
                self.frozen = False

    def armor_bash(self, enemy):
        import math

        blocked = 0
        if self.is_alive():
            if enemy.is_alive():
                if self.defense > 0:
                    if not enemy.dodge():
                        self.attackForMimic = "ArmorBash"
                        damage = math.ceil(self.defense * 1.5)
                        self.valueForMimic = damage
                        self.defense = 0

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
                        self.attack_info(enemy, damage, "armor bash", blocked)
                    else:
                        print(f"{enemy.name} dodged!")
                        self.defense = 0
                        if enemy.char == "Thief":
                            enemy.dodges += 5
                            enemy.dodge_fix()

                else:
                    print("Armor required! You missed your your chance this turn!")

