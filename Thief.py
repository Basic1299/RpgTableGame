from Character import Character
from Tooltips import Tooltips
import os


class Thief(Character):
    def __init__(self, name, cube):
        super().__init__(name, cube)
        self.char = "Thief"
        self.health = 70
        self.maxHealth = 70
        self.damage = 3
        self.dodgeChance = 3
        self.dodges = 0
        self.maxDodges = 20
        self.windDance = 0

    # Watching dodges overload
    def dodge_fix(self):
        if self.dodges > self.maxDodges:
            self.dodges = self.maxDodges

    def decision(self, enemy, game_round):
        loop = True
        # decrease wind dance variable every turn by 1
        if self.windDance > 0:
            self.windDance -= 1
        # 100% dodge only for one round
        if self.dodgeChance == 1:
            self.dodgeChance = 3

        if self.alive and enemy.alive:
            if not self.frozen:
                while loop:
                    os.system('clear')
                    print(f"Round {game_round}")
                    self.info("Dodges", self.dodges, self.maxDodges)
                    x = input(f"Front stab(1)  Wind dance(2)  Mimic[{enemy.attackForMimic}](3)  Pass(4)\n>").replace(" ", "").lower()
                    if x == "1":
                        self.attack(enemy, "dagger")
                        break
                    elif x == "2":
                        self.wind_dance()
                        break
                    elif x == "3":
                        self.mimic(enemy)
                        break
                    elif x == "4":
                        Character.pass_turn()
                        break
                    elif x == "frontstab":
                        Tooltips.tip_front_stab()
                    elif x == "winddance":
                        Tooltips.tip_wind_dance()
                    elif x == "mimic":
                        Tooltips.tip_mimic()
            else:
                self.info("Dodges", self.dodges, self.maxDodges)
                print("You are frozen this turn and can't move...")
                self.frozen = False

    def wind_dance(self):
        if self.windDance <= 0:
            self.dodgeChance = 1
            self.windDance = 3
            print("You are dancing in the wind...")
        else:
            print("You cannot wind dance yet!")

    # Demonic touch
    def mimic_demonic_touch(self, damage, enemy):
        enemy.health -= damage
        enemy.health = self.fix_health(enemy)
        enemy.alive = enemy.is_alive()
        print(f"{self.name} touched {enemy.name}'s soul and dealt {damage} damage by mimic.")
        self.dodges = 0
        enemy.attackForMimic = "Nothing"

    # Life steal
    def mimic_life_steal(self, lifeSteal, enemy):
        if self.health + lifeSteal >= self.maxHealth:
            restored = self.maxHealth - self.health
            self.health = self.maxHealth
        else:
            restored = lifeSteal
            self.health += lifeSteal
        print(f"{restored} health have been drained by mimic.")
        self.dodges = 0
        enemy.attackForMimic = "Nothing"

    # Fire ball
    def mimic_fire_ball(self, damage, enemy):
        enemy.health -= damage
        enemy.health = self.fix_health(enemy)
        enemy.alive = enemy.is_alive()
        self.spell_info(enemy, damage, "mimic fire")
        self.dodges = 0
        enemy.attackForMimic = "Nothing"

    # Armor bash
    def mimic_armor_bash(self, damage, enemy):
        blocked = 0
        # reducing armor or health
        armorValue = enemy.defense - damage
        if armorValue >= 0:
            damage = 0
            blocked = enemy.defense - armorValue
            enemy.defense = armorValue
        elif armorValue < 0:
            enemy.health += armorValue
            damage = armorValue * (-1)
            blocked = enemy.defense
            enemy.defense = 0
            enemy.health = self.fix_health(enemy)

        enemy.alive = enemy.is_alive()
        self.attack_info(enemy, damage, "armor bash mimic", blocked)
        self.dodges = 0
        enemy.attackForMimic = "Nothing"

    def mimic_ice_shard(self, damage, enemy):
        enemy.frozen = True
        enemy.health -= damage
        enemy.health = self.fix_health(enemy)
        enemy.alive = enemy.is_alive()
        self.spell_info(enemy, damage, "ice mimic")
        print(f"{enemy.name} turned into the ice!")
        self.dodges = 0
        enemy.attackForMimic = "Nothing"

    # mimic opponents last used ability with 100-140% dmg/heal depends on your actual dodges 
    def mimic(self, enemy):
        import math
        if self.is_alive():
            if enemy.is_alive():
                if self.dodges > 0:
                    if not enemy.dodge():
                        # No mimic value
                        if enemy.attackForMimic == "Nothing":
                            print("There is nothing to mimic...")
                        # Demonic touch
                        elif enemy.attackForMimic == "DemonicTouch":
                            self.mimic_demonic_touch(self.count_mimic_value(enemy), enemy)
                        # Life steal
                        elif enemy.attackForMimic == "LifeSteal":
                            self.mimic_life_steal(self.count_mimic_value(enemy), enemy)
                        # Ice shard
                        elif enemy.attackForMimic == "IceShard":
                            self.mimic_ice_shard(self.count_mimic_value(enemy), enemy)
                        # Fire ball
                        elif enemy.attackForMimic == "FireBall":
                            self.mimic_fire_ball(self.count_mimic_value(enemy), enemy)
                        # Armor bash
                        elif enemy.attackForMimic == "ArmorBash":
                            self.mimic_armor_bash(self.count_mimic_value(enemy), enemy)
                    else:
                        print(f"{enemy.name} resisted!")
                else:
                    print("You have not enough dodges for mimic opponents ability!")
            else:
                print("Enemy is dead")
        else:
            print("You are dead")

    # return value of opponents last ability + percentage addition by your actual dodges +(0-40%)
    def count_mimic_value(self, enemy):
        import math
        return math.ceil(enemy.valueForMimic + ((enemy.valueForMimic / 10) * (self.dodges // 5)))
