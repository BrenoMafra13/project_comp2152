import random
import os

# ------------------ Loot Functions ------------------

def use_loot(belt, health_points, combat_strength):
    """
    Refined loot use: process every item in belt.
    Health Potion increases HP by 5 (capped at 100).
    Leather Boots add 3 shield (implemented here as a health bump).
    Poison Potion decreases HP by 3.
    Secret Note increases combat strength by 2.
    Any other item is ineffective.
    """
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
    """
    Presents an ASCII art loot bag and then randomly selects four items.
    Items are paired and the user chooses one from each pair.
    """
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
    """
    Hero's attack includes a lifesteal effect.
    Damage is a random integer up to combat_strength.
    If damage is enough to kill the monster, its health becomes 0.
    Otherwise, the monster loses a fixed amount (combat_strength).
    If lifesteal is active, hero heals for damage * lifesteal.
    Returns updated monster health and hero health.
    """
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
    """
    Monster's attack function with shield mechanics.
    Displays a dragon sprite, calculates damage and allows shield to absorb some damage.
    After the attack, the shield regenerates by shield_regen points.
    Returns updated hero health and shield.
    """
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
    # Apply shield absorption if available.
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

# ------------------ Legendary Quest ------------------

def legendary_quest(hero):
    print("\n*** Legendary Quest Triggered! ***")
    chest_art = r"""
           __________
          /\____;;___\
         | /         /
         `. ())oo() .
         |\(%()*^^()^\
        %| |-%-------|
       % \ | %  ))   |
       %  \|%________|
        %%%%
    """
    print(chest_art)
    challenge_result = random.randint(1, 10)
    print("You roll the challenge dice... Result:", challenge_result)
    if challenge_result >= 3:
        print("You have overcome the challenge and unlocked the legendary chest!")
        legendary_items = [
            {"name": "Relic of Power", "type": "buff", "effect": "Increase combat strength by 10", "bonus": 10, "art": r"""
                __________
               '._==_==_=_.' 
               .-\:      /-. 
              | (|:.     |) | 
               '-|:.     |-'  
                 \::.    /   
                  '::. .'
                    ) (
                  _.' '._ 
                 `"""""""` 
            """},
            {"name": "Excalibur", "type": "weapon", "effect": "Equip to gain +10 to combat and health", "bonus": 10, "art": r"""
                 _
                (_)
                |=|
                |=|
            /|__|_|__|\
           (    ( )    )
            \|\/\"/\/|/
              |  Y  |
              |  |  |
              |  |  |
             _|  |  |
          __/ |  |  |\
         /  \ |  |  |  \
        __|  |  |  |   |
      /\/  |  |  |   |\
       <   +\ | |\ />  \
        >   + \  | LJ    |
              + \|+  \  < \
        (O)      +    |    )
         |             \  /\ 
       ( | )   (o)      \/  )
      _\\|//__( | )______)_/ 
              \\|// 
            """},
            {"name": "Mystic Amulet", "type": "shield", "effect": "Provides shield regeneration of 4 per turn", "bonus": 4, "art": r"""
                o--o--=g=--o--o
               /      .'       \
               o      '.       o
                \             /
                 o           o
                  \         /
                   o       o
                    \     /
                     o   o
                      \_/
                       =
                      .^.
                     '   '
                     '. .'
                       !
            """},
            {"name": "Vampirism Cape", "type": "lifesteal", "effect": "Gain 50% of damage dealt as HP", "bonus": 0.5, "art": r"""
             ,*-~\"`^\"*u_                                _u*\"^`\"~-*,
          p!^       /  jPw                            w9j \        ^!p
        w^.._      /      \_                      _/\"     \        _.^w
             *_   /          \_      _    _      _/         \     _* 
               q /           / \q   ( `--` )   p/ \          \   p
               jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                        *_ /      \"==) ;; (==\"      \ _*
                         `/.w***,   /(    )\   ,***w.\" 
                          ^ ilmk ^c/ )    ( \c^      ^ 
                                  'V')_)(_('V'
                                      `` ``
            """}
        ]
        reward = random.choice(legendary_items)
        print(f"You have found the {reward['name']}! {reward['effect']}")
        print(reward["art"])
        if reward["name"] == "Excalibur":
            decision = input("Do you want to equip Excalibur? (y/n): ")
            if decision.lower() == "y":
                hero.combat_strength += reward["bonus"]
                hero.health_points += reward["bonus"]
                hero.weapon = "Excalibur"
                print("Excalibur equipped! Your combat and health points increased by 10 each.")
            else:
                print("You leave Excalibur behind.")
        elif reward["name"] == "Relic of Power":
            hero.combat_strength += reward["bonus"]
            hero.relic = True
            print(f"Your combat strength increases by {reward['bonus']}.")
        elif reward["name"] == "Mystic Amulet":
            hero.shield = reward["bonus"]
            print("You gain the Mystic Amulet! You now regenerate 4 shield points each turn.")
        elif reward["name"] == "Vampirism Cape":
            hero.lifesteal = reward["bonus"]
            print("You gain the Vampirism Cape! You now steal half the damage dealt as health.")
        return True
    else:
        print("You failed the legendary quest challenge. The chest vanishes!")
        return False

