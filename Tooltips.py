import os


class Tooltips(object):

    @classmethod
    def tip_blood_wand(cls):
        os.system('clear')
        print("""Blood wand
-----------------
Magic attack what ignores armor and causes 3-8 damage.
However it costs warlock 3 health.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_front_stab(cls):
        os.system('clear')
        print("""Front stab
-----------------
Regular attack what causes 4-9 damage.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_sword_swing(cls):
        os.system('clear')
        print("""Sword swing
-----------------
Regular attack what causes 5-10 damage.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_wand(cls):
        os.system('clear')
        print("""Wand
-----------------
Regular attack what causes 3-8 damage.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_fire_ball(cls):
        os.system('clear')
        print("""Fireball
-----------------
Powerful spell what causes
9-24 damage to enemy. it also ignores armor. 
However, it costs 3 stars of mana and can be mimic by thief.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_ice_shard(cls):
        os.system('clear')
        print("""Ice shard
-----------------
Frost spell what causes
6-11 damage to enemy. it also ignores armor. 
However, it costs 2 stars of mana and can be mimic by thief.
It also freezes the opponent for the next round.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_armor_up(cls):
        os.system('clear')
        print("""Armor up
-----------------
Not offensive ability.
Warrior wears extra 4-9 armor against physic attacks.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_armor_bash(cls):
        os.system('clear')
        print("""Armor bash
-----------------
Powerful ability.
Warrior consumes all his armor and converts it into 2-30 damage.
Damage depends on his actual armor. This ability can be mimic by thief.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_wind_dance(cls):
        os.system('clear')
        print("""Wind dance
-----------------
Not offensive ability
Thief starts to dance lightly in the wind.
His opponent cannot hit him next round with any ability.
This can be used only once per three rounds.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_mimic(cls):
        os.system('clear')
        print("""Mimic
-----------------
Very strong ability.
Thief mimics last offensive opponents ability 
and uses it back against his opponent 0-40% stronger,
depends on actual number of dodges.
This ability requires at least 1 charge of dodge
and consumes all dodge charges.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_life_steal(cls):
        os.system('clear')
        print("""Life steal
-----------------
Spell what causes only 1-2 dmg, 
however it heals warlock for 2-8 health.
It also rips off the opponents body shard of soul.
It cannot be used two times in row.
It can be mimic by thief.\n""")
        input("Press enter to continue...")
        os.system('clear')

    @classmethod
    def tip_demonic_touch(cls):
        os.system('clear')
        print("""Demonic touch
-----------------
Very powerful spell what causes 10-35 damage,
depends on actual warlocks health. Less health means more damage.
This spell requires four soul shards, what can be obtain with life steal spell.
Using consumes all shards.
It can be mimic by thief.\n""")
        input("Press enter to continue...")
        os.system('clear')



