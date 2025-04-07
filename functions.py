import random
import os

# ------------------ Loot Functions ------------------

def use_loot(belt, health_points, combat_strength):
    print("    |    !!You see a monster in the distance! So you quickly use your items:")
    while belt:
        item_used = belt.pop(0)
        if item_used == "Health Potion":
            health_gain = 5
            health_points = min(100, health_points + health_gain)
            print(f"    |    You used {item_used}, increasing your health by {health_gain} to {health_points}.")
        elif item_used == "Leather Boots":
            shield = 3
            health_points = min(100, health_points + shield)
            print(f"    |    You used {item_used}, giving you a shield of {shield}. Total life + shield is now {health_points}.")
        elif item_used == "Poison Potion":
            decrease_health = 3
            health_points = max(0, health_points - decrease_health)
            print(f"    |    You used {item_used}, decreasing your health by {decrease_health} to {health_points}.")
        elif item_used == "Secret Note":
            combat_strength += 2
            print(f"    |    You read the {item_used} and gained a strategic advantage! Combat strength increased by 2 to {combat_strength}.")
        else:
            print(f"    |    You used {item_used}, but it appears to be ineffective.")
    return belt, health_points, combat_strength

def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    if len(loot_options) < 4:
        print("Not enough items to choose from!")
        return loot_options, belt
    selected_items = random.sample(loot_options, 4)
    pairs = [(selected_items[i], selected_items[i + 1]) for i in range(0, 4, 2)]
    for idx, (item1, item2) in enumerate(pairs, start=1):
        print(f"\n    |    Pair {idx}: {item1} and {item2}.")
        choice = input(f"Type 1 for {item1} or 2 for {item2}: ")
        while choice not in ['1', '2']:
            print("\nInvalid input. Please enter '1' or '2'.")
            choice = input(f"Type 1 for {item1} or 2 for {item2}: ")
        chosen_item = item1 if choice == '1' else item2
        belt.append(chosen_item)
        loot_options.remove(chosen_item)
    print("\n    |    Your belt: ", belt)
    return loot_options, belt

# ------------------ Attack Functions ------------------

def hero_attacks(combat_strength, m_health_points, lifesteal=0, hero_health=0):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
    """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    damage = random.randint(1, combat_strength)
    if damage >= m_health_points:
        m_health_points = 0
        print("    |    You dealt " + str(damage) + " damage and killed the monster!")
    else:
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    if lifesteal > 0:
        heal = int(damage * lifesteal)
        hero_health += heal
        print("    |    Vampirism activated! You heal for " + str(heal) + " points. Your health is now " + str(hero_health))
    return m_health_points, hero_health

def monster_attacks(m_combat_strength, hero_health, hero_shield=0, shield_regen=0):
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
    print(dragon_art)
    damage = random.randint(1, m_combat_strength)
    print("    |    Monster's attack damage: " + str(damage))
    if hero_shield > 0:
        if damage <= hero_shield:
            print("    |    Your shield absorbed all " + str(damage) + " damage.")
            hero_shield -= damage
            damage = 0
        else:
            print("    |    Your shield absorbed " + str(hero_shield) + " damage and broke!")
            damage -= hero_shield
            hero_shield = 0
    if damage > 0:
        hero_health -= damage
        print("    |    You took " + str(damage) + " damage. Your health is now " + str(hero_health))
    else:
        print("    |    No damage got through. Your health remains at " + str(hero_health))
    if shield_regen > 0:
        hero_shield += shield_regen
        print("    |    Your shield regenerates by " + str(shield_regen) + " points. New shield value: " + str(hero_shield))
    return hero_health, hero_shield

# ------------------ Recursion ------------------

def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))

# ------------------ Save/Load Game ------------------

def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero.\n")
        file.write(f"Total monsters killed: {num_stars}\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            print("Loading from saved file")
            last_monsters_count = 0
            last_game_state = ""
            for line in file:
                if line.startswith("Total monsters killed"):
                    last_monsters_count = int(line.strip().split(":")[1].strip())
                elif line.strip():
                    last_game_state = line.strip()
            print(f"Total monsters killed: {last_monsters_count}")
            return last_game_state, last_monsters_count
    except FileNotFoundError:
        print("No previous game found, starting first game")
        return "", 0

def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game_state, total_monsters_killed = load_game()
    if last_game_state:
        if "Hero" in last_game_state and "gained" in last_game_state:
            num_stars = int(last_game_state.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game_state:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
    return combat_strength, m_combat_strength

def dream_level():
    while True:
        user_input = input("Quantity of dream levels to go down? (Enter 0 to 3): ")
        try:
            dream_lvls = int(user_input)
            if 0 <= dream_lvls <= 3:
                return dream_lvls
            else:
                print("Enter a number between 0 and 3.")
        except ValueError:
            print("Enter a valid integer.")

# ------------------ Alchemist ------------------

def alchemist(belt):
    print("\n*** You encounter a mysterious Alchemist! ***")
    if len(belt) < 2:
        print("The Alchemist needs at least two items to work with. He vanishes in disappointment.")
        return belt

    print(f"Your current belt: {belt}")
    print("He offers to fuse two of your items into something special...")

    for i, item in enumerate(belt):
        print(f"{i + 1}. {item}")

    try:
        idx1 = int(input("Choose the number of the first item to fuse: ")) - 1
        idx2 = int(input("Choose the number of the second item to fuse: ")) - 1
        if idx1 == idx2 or idx1 not in range(len(belt)) or idx2 not in range(len(belt)):
            print("Invalid selection. The Alchemist leaves.")
            return belt
    except ValueError:
        print("Invalid input. The Alchemist leaves.")
        return belt

    item1 = belt.pop(max(idx1, idx2))
    item2 = belt.pop(min(idx1, idx2))

    if (item1 == "Health Potion" and item2 == "Leather Boots") or (item2 == "Health Potion" and item1 == "Leather Boots"):
        fusion_result = "Elixir of Fortitude"
        print("Fusion successful! You created an Elixir of Fortitude (+7 HP)")
    elif (item1 == "Poison Potion" and item2 == "Secret Note") or (item2 == "Poison Potion" and item1 == "Secret Note"):
        fusion_result = "Shadow Brew"
        print("Fusion successful! You created a Shadow Brew (+3 Combat Strength)")
    else:
        print("You failed the legendary quest challenge :(. The chest vanishes!")
        return False

    belt.append(fusion_result)
    print("Updated belt:", belt)
    return belt

# ------------------ Artifact Collection ------------------

def collect_artifacts(hero, monster):
    print("\nCollecting artifacts from the defeated monster...")
    new_artifacts = [a for a in monster.loot if a not in hero.inventory]
    hero.inventory.extend(new_artifacts)
    print("Artifacts collected:", hero.inventory)

    if hero.combat_strength > 4:
        if 'Amulet of Power' in hero.inventory:
            hero.combat_strength += 2
            print("Artifact effect: Amulet of Power increases combat strength by 2.")
        elif 'Golden Sword' in hero.inventory:
            hero.combat_strength += 3
            print("Artifact effect: Golden Sword increases combat strength by 3.")
    else:
        if 'Minor Ring' in hero.inventory:
            hero.health_points += 2
            print("Artifact effect: Minor Ring increases health points by 2.")
        elif 'Boots of Speed' in hero.inventory:
            hero.combat_strength += 1
            print("Artifact effect: Boots of Speed increases combat strength by 1.")

# ------------------ Legendary quest  ------------------

def legendary_quest(hero):
    print("\n*** You accept the legendary quest! ***")
    print("You face a magical challenge...")

    challenge = random.randint(1, 3)
    if challenge == 1:
        print("You find the Shield of Light! +5 Shield")
        hero.shield = getattr(hero, "shield", 0) + 5
    elif challenge == 2:
        print("You drink a cursed potion and survive! +10 Health")
        hero.health_points = min(100, hero.health_points + 10)
    else:
        print("You master the Vampiric Blade! Lifesteal unlocked!")
        hero.lifesteal = 0.3
    return True