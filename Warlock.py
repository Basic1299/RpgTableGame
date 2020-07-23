from Character import Character
from Tooltips import Tooltips
import os


class Warlock(Character):
    def __init__(self, name, cube):
        super().__init__(name, cube)
        self.char = "Warlock"
        self.health = 100
        self.maxHealth = 100
        self.damage = 2
        self.shards = 0
        self.maxShards = 20
        self.lifeStealUsed = 0

    def blood_wand(self, enemy):
        if self.is_alive():
            if enemy.is_alive():
                self.health -= 3
                if not enemy.dodge():
                    damage = self.cube.throw() + self.damage
                    enemy.health -= damage
                    enemy.health = self.fix_health(enemy)
                    enemy.alive = enemy.is_alive()
                    self.spell_info(enemy, damage, "blood wand")
                else:
                    print(f"{enemy.name} resisted!")
                    if enemy.char == "Thief":
                        enemy.dodges += 5
                        enemy.dodge_fix()

# decision to make every turn
    def decision(self, enemy, game_round):
        if self.lifeStealUsed > 0:
            self.lifeStealUsed -= 1
        loop = True
        if self.alive and enemy.alive:
            if not self.frozen:
                while loop:
                    os.system('clear')
                    print(f"Round {game_round}")
                    self.info("Soul shards", self.shards, self.maxShards)
                    x = input("Blood wand(1)  Life steal(2)  Demonic touch(3)  Pass(4)\n>").replace(" ", "").lower()
                    if x == "1":
                        self.blood_wand(enemy)
                        break
                    elif x == "2":
                        self.life_steal(enemy)
                        break
                    elif x == "3":
                        self.demonic_touch(enemy)
                        break
                    elif x == "4":
                        Character.pass_turn()
                        break
                    elif x == "bloodwand":
                        Tooltips.tip_blood_wand()
                    elif x == "lifesteal":
                        Tooltips.tip_life_steal()
                    elif x == "demonictouch":
                        Tooltips.tip_demonic_touch()
            else:
                self.info("Soul shards", self.shards, self.maxShards)
                print("You are frozen this turn and can't move...")
                self.frozen = False

    def visual_shards_fix(self):
        return self.shards // 5

    # limit 35 damage for demonic touch
    def demonic_touch_damage_limit(self, damage):
        if damage > 35:
            return 35
        else:
            return damage

    def demonic_touch(self, enemy):
        import math

        if self.is_alive():
            if enemy.is_alive():
                if self.visual_shards_fix() == 4:
                    if not enemy.dodge():
                        self.attackForMimic = "DemonicTouch"
                        self.shards = 0
                        damage = self.demonic_touch_damage_limit(math.ceil(self.maxHealth - self.health + 10))
                        self.valueForMimic = damage

                        enemy.health -= damage
                        enemy.health = self.fix_health(enemy)
                        enemy.alive = enemy.is_alive()

                        print(f"{self.name} touched {enemy.name}'s soul and dealt {damage} damage.")
                    else:
                        print(f"{enemy.name} resisted!")
                        if enemy.char == "Thief":
                            enemy.dodges += 5
                            enemy.dodge_fix()
                        self.shards = 0
                else:
                    print("Four shards required. You missed your change this turn!")

    def add_shard(self, number):
        if self.visual_shards_fix() < 4:
            self.shards += number * 5
            print("Piece of life added to your pocket!")
        else:
            print("Your life pocket is full!")

    def life_steal(self, enemy):
        import random
        damage = random.randint(1, 3)
        lifeSteal = damage + random.randint(1, 6)

        if self.lifeStealUsed <= 0:
            if self.is_alive():
                if enemy.is_alive():
                    if not enemy.dodge():
                        self.attackForMimic = "LifeSteal"
                        enemy.health -= damage
                        enemy.health = self.fix_health(enemy)
                        if self.health + lifeSteal >= self.maxHealth:
                            restored = self.maxHealth - self.health
                            self.health = self.maxHealth
                        else:
                            restored = lifeSteal
                            self.health += lifeSteal

                        self.valueForMimic = restored
                        enemy.alive = enemy.is_alive()

                        self.spell_info(enemy, damage, "life steal")
                        print(f"{restored} health have been drained.")
                        self.add_shard(1)
                        self.lifeStealUsed = 2
                    else:
                        print(f"{enemy.name} resisted!")
                        if enemy.char == "Thief":
                            enemy.dodges += 5
                            enemy.dodge_fix()
                else:
                    print("Enemy is dead")
            else:
                print("You are dead")
        else:
            print("You cannot drain health two times in row. You missed your chance this turn!")













