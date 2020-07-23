from Character import Character
from Tooltips import Tooltips
import os


class Mage(Character):
    def __init__(self, name, cube):
        super().__init__(name, cube)
        self.char = "Mage"
        self.mana = 20
        self.maxMana = 20
        self.damage = 2

    # attack twice and pierce through defense
    def fire_ball(self, enemy):
        damage = 6

        if self.is_alive():
            if self.can_i_spell(15):
                if enemy.is_alive():
                    if not enemy.dodge():
                        self.attackForMimic = "FireBall"
                        self.mana -= 15
                        # triple damage
                        for x in range(0, 3):
                            damage += enemy.cube.throw()
                        self.valueForMimic = damage

                        enemy.health -= damage
                        enemy.health = self.fix_health(enemy)
                        enemy.alive = enemy.is_alive()
                        self.spell_info(enemy, damage, "fire")
                    else:
                        print(f"{enemy.name} resisted!")
                        self.mana -= 15
                        if enemy.char == "Thief":
                            enemy.dodges += 5
                            enemy.dodge_fix()
                else:
                    print(f"{enemy.name} is dead")
            else:
                print("More mana required. You passed your chance this turn!")
                self.mana_regen(5)

    def ice_shard(self, enemy):
        if self.is_alive():
            if self.can_i_spell(10):
                if enemy.is_alive():
                    if not enemy.dodge():
                        self.attackForMimic = "IceShard"
                        self.mana -= 10
                        damage = self.cube.throw() + 5
                        self.valueForMimic = damage

                        enemy.frozen = True
                        enemy.health -= damage
                        enemy.health = self.fix_health(enemy)
                        enemy.alive = enemy.is_alive()
                        self.spell_info(enemy, damage, "ice")
                        print(f"{enemy.name} turned into the ice!")
                    else:
                        print(f"{enemy.name} resisted!")
                        self.mana -= 10
                        if enemy.char == "Thief":
                            enemy.dodges += 5
                            enemy.dodge_fix()
                else:
                    print(f"{enemy.name} is dead")
            else:
                print("More mana required. You passed your chance this turn!")
                self.mana_regen(5)

    # checker for possibility of spell cast
    def can_i_spell(self, manaCost):
        return self.mana - manaCost >= 0

    def mana_regen(self, value):
        if self.mana <= 15:
            self.mana += value

    # prevents mana overflow
    def mana_fix(self):
        if self.mana > self.maxMana:
            self.mana = self.maxMana

    # decision to make every turn
    def decision(self, enemy, game_round):
        self.mana_regen(5)
        loop = True
        if self.alive and enemy.alive:
            if not self.frozen:
                while loop:
                    os.system('clear')
                    print(f"Round {game_round}")
                    self.info("Mana", self.mana, self.maxMana)
                    x = input("Wand(1)  Fireball(2)  Ice shard(3)  Pass(4)\n>").replace(" ", "").lower()
                    if x == "1":
                        self.attack(enemy, "wand")
                        break
                    elif x == "2":
                        self.fire_ball(enemy)
                        break
                    elif x == "3":
                        self.ice_shard(enemy)
                        break
                    elif x == "4":
                        Character.pass_turn()
                        break
                    elif x == "wand":
                        Tooltips.tip_wand()
                    elif x == "fireball":
                        Tooltips.tip_fire_ball()
                    elif x == "iceshard":
                        Tooltips.tip_ice_shard()
            else:
                self.info("Mana", self.mana, self.maxMana)
                print("You are frozen this turn and can't move...")
                self.frozen = False



