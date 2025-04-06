import random
import os
import platform
import functions as functions
from hero import Hero
from monster import Monster

print("Operating System:", os.name)
print("Python Version:", platform.python_version())

# Define two Dice.
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons.
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Loot options and belt.
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers.
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

num_stars = 0
lifesteal = 0
shield = 0
shield_regen = 4

# Dragon art for the final fight.
dragon_art = r"""
                           /           /
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \\############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / "" \  //#################-
  -###################\\/  (_)  \//###################-
 _#/|##########/\######(   "/"   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  ! ' !  /##/\#/  \/\#/\#/\| \|
 '  |/  V  V '   V  \\#\  \   /  /#/  V   '  V  V  \|  '
    '   '  '      '   /#\  | |  /#\   '      '  '   '
                     (  (  | |  )  )
                    __\  \ | | /  /__
                   (vvv(VVV)(VVV)vvv)
"""

# ---------------------- INPUTS -----------------------
i = 0
input_invalid = True
while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")
    if not (combat_strength.isnumeric() and m_combat_strength.isnumeric()):
        print("    |    Invalid input. Please enter integer numbers for Combat Strength.")
        i += 1
        continue
    elif int(combat_strength) not in range(1, 7) or int(m_combat_strength) not in range(1, 7):
        print("    |    Please enter a valid integer between 1 and 6.")
        i += 1
        continue
    else:
        input_invalid = False

if not input_invalid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # --- Weapon Roll ---
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, combat_strength + weapon_roll)
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))
    combat_strength, m_combat_strength = functions.adjust_combat_strength(combat_strength, m_combat_strength)

    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("    |    --- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("    |    --- Your weapon is meh")
    else:
        print("    |    --- Nice weapon, friend!")
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist.")

    # --- Health Points ---
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")
    input("Roll for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Monster rolled " + str(m_health_points) + " health points")

    # --- Loot Collection ---
    print("    |    !!You find a loot bag!!")
    input("Press enter to open it")
    loot_options, belt = functions.collect_loot(loot_options, belt)
    belt, health_points, combat_strength = functions.use_loot(belt, health_points, combat_strength)

    # --- Optional Legendary Quest ---
    if random.random() < 1.0:
        print("*** A legendary treasure chest appears! ***")
        class TempHero:
            pass
        temp_hero = TempHero()
        temp_hero.combat_strength = combat_strength
        temp_hero.health_points = health_points
        temp_hero.weapon = None
        temp_hero.shield = 0
        temp_hero.lifesteal = 0
        if functions.legendary_quest(temp_hero):
            combat_strength = temp_hero.combat_strength
            health_points = temp_hero.health_points
            shield = getattr(temp_hero, "shield", 0)
            lifesteal = getattr(temp_hero, "lifesteal", 0)

    # --- Dream Levels ---
    num_dream_lvls = functions.dream_level()
    if num_dream_lvls > 0:
        health_points -= 1
        crazy_level = functions.inception_dream(num_dream_lvls)
        combat_strength += crazy_level
        print("    |    Number of dream levels: ", num_dream_lvls)
        print("    |    Combat strength: ", combat_strength)
        print("    |    Health points: ", health_points)

    # --- Final Fight ---
    print(dragon_art)
    print("    |    You meet the dragon. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        input("Roll to see who strikes first (Press Enter)")
        if random.choice(small_dice_options) % 2 != 0:
            input("You strike (Press enter)")
            m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal, health_points)
            if m_health_points == 0:
                num_stars = 3
                break
            input("The dragon strikes (Press enter)")
            health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, shield_regen)
        else:
            input("The dragon strikes first (Press enter)")
            health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, shield_regen)
            if health_points == 0:
                num_stars = 1
                break
            input("The hero strikes back (Press enter)")
            m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal, health_points)

    # --- Final Results ---
    if m_health_points <= 0:
        winner = "Hero"
        print("You defeated the dragon!")

        hero_obj = Hero()
        hero_obj.combat_strength = combat_strength
        hero_obj.health_points = health_points
        hero_obj.inventory = []

        monster_obj = Monster()
        monster_obj.loot = ["Amulet of Power", "Golden Sword", "Minor Ring", "Boots of Speed"]

        print("Collecting artifacts from the defeated monster...")
        new_artifacts = functions.collect_artifacts(monster_obj, hero_obj)
        print("Artifacts collected:", new_artifacts)

        bonus_from_alchemy = functions.alchemist(hero_obj)
        combat_strength = hero_obj.combat_strength
        health_points = hero_obj.health_points
        print(f"    |    Alchemist power granted: {bonus_from_alchemy}")

    else:
        winner = "Monster"
        print("You lost the fight with the dragon!")
        exit()

    # --- Save Game ---
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        hero_name = input("Enter your Hero's name (in two words): ")
        name_parts = hero_name.split()
        if len(name_parts) != 2 or not all(p.isalpha() for p in name_parts):
            print("    |    Invalid name. Please use two alphabetic words.")
            tries += 1
        else:
            short_name = name_parts[0][:2] + name_parts[1][:1]
            input_invalid = False
            print("    |    I'm going to call you " + short_name + " for short")

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
        print("    |    Game saved. Thank you for playing.")
