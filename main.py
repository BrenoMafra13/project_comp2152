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


skeleton_art = r"""
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \
               f'. _,,-'                   \ \
              ()--  |                       \ \
                \.  |                       /  \
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \
                                             |lllj
                                             ||||| 
"""

bat_art = r"""
  ___
. --.`-._^,
|,;::;-._ `-._
 |`::::`; ;-. `_
 | ;::::; ::`-. `,                       _,-'.  .. ` ---.____
  ; ;;;;` :::::`.`                      ;  :::` `:; `;;.     `---._
  | : ::' ::::::`.`                    ; .':::'  ;:. `.;;;;;;;;;
  ; :::`, :::::::`.`.     ^          .' /\ :::`, ':::.   `;;; ; ;;;
 : :::::` `;::::::`.`-._ / \   ______;,' ; ::::` :::::::. `.;;;;;;;
 | ::::::; |:::::::`-.   ) ,; '       `.( :::::; `::::::::. `;;;;;
 | ::::::` ::::::::: `   ; `;; ;\  _ _ ;/ ::: :`  ;: ::::::: ;;;;;
 ; ;:::::; |::::::::: )  `-.\( `o}' ` _(   ::: ;  '::::::::: `;;;;
: ;::::::; ;:: :::::: \              `v'. :::::`; :::::::::`. ;;;;
| :::::::|  ` :::::::: `.   `-._ `.-._;_; ::::::` `:::::::::: `;;;
| :::::: :;;, `::::::::.`-.     `.`._`'`'  : :::;  ;:: :::::`. ;;;;
| ::::::::  :  ;: :::::: .'      `-._;   ; :: ::`  ::::::::::: `;;;
| ::::::::::`; `.::::::: `.   ::         : ::: ::. `.:::::::::: `;;
| ;::::::::::: ;::::::::: :.    ;;  ;;  | :::::: `  ;: :::::::: ;;
`v'.:::::::::: ;:::::::::: :      ;;   .'::::::::`;  ::::::::::: ;'
    ~~~`.::::: ;:::::::::: |           : :::::::::`. `::::::::/`v'
         \:: .,;:::::::   _;'    :;;  .'_ ;;:::::::;  ,:::,'
          ~\ ;;::::::: ,-',-':   `    :-.`_  ::::::`. ;;,-'
           | ;--.::::: ;;  .:`.       ;..`.`. ;::::::  /
           `v'    `-.; :; .... `------ ...`.: ,-'    : ;
                      )|| . ......; ;  ... :|/       `v
                     __;| .... ...; ` .... :|
                    ((c-.`._ .... `.`. . . ;`-.__
                    ""   `' `. ....`.`; .. ))~`-))
                              `-. . ;.'. ,/"    ""
                                 `._ Y ,/
                                    \`/
"""

vampire_art = r"""
                  __,-----,,,,  ,,,--------,__ 
                _-/|\\/|\\/|\\\|\//\\\//|/|//|\\_ 
               /|\/\//\\\\\\\\\\//////////////\\\\ 
             //|//           \\\///            |\\|\ 
            ///|\/             \/               \|\|\ 
           |/|//                                 |\\|\  
          |/|/                                    \|\|\
          ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\
         |/|/   '"          `'     '"          "'   ;|\|
         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|
         /|||;  :  /       \~~-___-~~/       \  :  ;|\| 
         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;||
         |\|;      ~-____--~'  ; ;  '~--____-~      ;\|
          ||;            ,`   ;   ;   ',            ;||
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~   \|/;    ,'`        ~~ ~~        `',    ;|\   ~-,_ 
  ,'         ||;  '                           '  ;\|/       `, 
 , _          ; ,         _--~~-~~--_           ;            _',
,-' `;-,        ;        ,; |_| | |_| ;,       ;;        ,-;' `-,
      ; `,      ;       ;_| : `~'~' : |_;       ;      ,' ;
       ;  `,     ;     :  `\/       \/   :     ;     ,'  ;
        ;   `,    ;     :               ;     ;    ,'   ;
         ;    `,_  ;     ;./\_     _/\.;     ;   _,    ;
spb   _-'        ;  ;     ~~--|~|~|--~~     ;   ;       '-_
  _,-'            ;  ;        ~~~~~        ;   ;           `-,_
,~                 ;  \`~--__         __--~/  ;                ~,
                    ;   \   ~~-----~~    /   ;
                     ~-_  \  /  |  \   /  _-~
                        ~~-\/   |   \/ -~~
                       (=)=;==========;=(=)
"""

alchemist_art = r"""
                       ,---.
                       /    |
                      /     |
                     /      | 
                    /       |
               ___,'        |
             <  -'          :
              `-.__..--'``-,_\_
                 |o/ ` :,.)_`>
                 :/ `     ||/)
                 (_.).__,-` |\
                 /( `.``   `| :
                 \'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\
/,'-.__\\  ``-./ :`      ;       \
`\ `\  `\\  \ :  (   `  /  ,   `. \
  \` \   \\   |  | `   :  :     .\ \
   \ `\_  ))  :  ;     |  |      ): :
  (`-.-'\ ||  |\ \   ` ;  ;       | |
   \-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\__/_,'         ; |
       \:: :     /     `     ,   /  |
        || |    (        ,' /   /   |
        ||                ,'   /    |
"""

# --- Input Phase: Get valid combat strengths ---
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
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .               
             /     # @   *               
                 ,     %                
            @&@           @&@
    """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, combat_strength + weapon_roll)
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))
    combat_strength, m_combat_strength = functions.adjust_combat_strength(combat_strength, m_combat_strength)

    # --- Weapon Analysis ---
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("    |    --- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("    |    --- Your weapon is mediocre")
    else:
        print("    |    --- Great weapon, friend!")
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- At least you didn't get stuck with only your fists...")

    # --- Health Points ---
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")
    print("    |", end="    ")
    input("Roll for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Monster rolled " + str(m_health_points) + " health points")

    # --- Loot Collection ---
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 4 items:")
    input("Press enter to see what's inside and make your choices...")
    loot_options, belt = functions.collect_loot(loot_options, belt)


    belt, health_points, combat_strength = functions.use_loot(belt, health_points, combat_strength)
    print("    |    Updated combat strength after using items: " + str(combat_strength))

    # --- Strength and Health Check ---
    print("    ------------------------------------------------------------------")
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # --- Optional Legendary Quest ---
    if random.random() < 1.0:
        print("\n*** A legendary treasure chest appears! ***")


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
            if getattr(temp_hero, "weapon", None):
                print("    |    New weapon equipped:", temp_hero.weapon)
            if getattr(temp_hero, "shield", 0) > 0:
                print("    |    New shield acquired:", temp_hero.shield)
                shield = temp_hero.shield
            if getattr(temp_hero, "lifesteal", 0) > 0:
                print("    |    New lifesteal ability acquired:", temp_hero.lifesteal)
        lifesteal = temp_hero.lifesteal



# --- Story Introduction ---
    print("\nWelcome, brave warrior, to the Quest of the Fallen Kingdom!")
    print("Long ago, the Kingdom of Eldoria thrived in peace and prosperity,")
    print("until a dark curse fell upon the land. A mysterious force corrupted its guardians,")
    print("transforming noble protectors into fearsome adversaries.")
    print("Ancient artifacts scattered throughout the realm hold the key to restoring balance.")
    print("Your journey will take you through treacherous dungeons, enchanted forests, and crumbling ruins,")
    print("where you must gather mystical items, master your combat skills, and overcome monstrous foes.")
    print("Face terrifying enemies such as the cursed Skeleton King and the dreaded Vampire King, Cazador,")
    print("all while preparing for your final trial: the epic battle against a legendary Dragon whose fury")
    print("threatens to engulf the entire kingdom in darkness.")
    print("The fate of Eldoria rests on your shoulders...\n")

# --- Input Phase: Get valid combat strengths ---

    print("\n------------------------------------------------------------------")
    print("Suddenly, you step into a dark corridor of crumbling walls and eerie silence.")
    print("In the distance, you hear the echo of rattling bones. Torches flicker as you approach.")
    print("A towering figure of cursed armor emerges, an ancient presence known as the:")
    print("THE ARMORED SKELETON KING!\n")
    print("You hear the sharp clink of its rusted sword being raised. A menacing grin can be sensed\n"
          "beneath the skeletal visage as it readies for battle...\n")
    print(skeleton_art)

    skeleton_hp = random.randint(6, 15)   
    skeleton_cs = random.randint(2, 5)    
    print("    |    The Armored Skeleton King roars with a Combat Strength of:", skeleton_cs)
    print("    |    Its bones seem to glow with an unholy aura. Health Points:", skeleton_hp)

    while skeleton_hp > 0 and health_points > 0:
        print("\n    |", end="    ")
        input("Roll to see who strikes first against the Skeleton King (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if attack_roll % 2 != 0:

            print("    |", end="    ")
            input("You strike (Press enter)")
            skeleton_hp, health_points = functions.hero_attacks(combat_strength, skeleton_hp, lifesteal,
                                                                health_points)
            if skeleton_hp == 0:
                num_stars = 2
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The Skeleton King swings its rusted blade! (Press enter)")
                health_points, shield = functions.monster_attacks(skeleton_cs, health_points, shield, 0)
                if shield > 0:
                    shield += shield_regen
                    print("    |    Your shield regenerates by " + str(shield_regen) +
                          " points. New shield value: " + str(shield))
                if health_points == 0:
                    num_stars = 1
        else:

            print("    |", end="    ")
            input("The Skeleton King lunges forward! (Press enter)")
            health_points, shield = functions.monster_attacks(skeleton_cs, health_points, shield, 0)
            if shield > 0:
                shield += shield_regen
                print("    |    Your shield regenerates by " + str(shield_regen) +
                      " points. New shield value: " + str(shield))
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The hero counterattacks!! (Press enter)")
                skeleton_hp, health_points = functions.hero_attacks(combat_strength, skeleton_hp, lifesteal,
                                                                    health_points)
                if skeleton_hp == 0:
                    num_stars = 2

    if skeleton_hp <= 0:
        print("\nYou have shattered the Armored Skeleton King into a pile of bones!")
        print("As the last bone clinks to the ground, the hallway grows silent again...\n")
        winner_skel = "Hero"
    else:
        print("\nYou have been defeated by the Armored Skeleton King. Your adventure ends here...")
        winner_skel = "Monster"
        exit() 


    print("------------------------------------------------------------------")
    print("Moments later, you enter a grand chamber with a massive throne in the center.")
    print("Crimson carpets lie soaked with fresh blood, leading up to the dais.")
    print("Above the throne, near a tall stained-glass window, a shadowy figure looms.\n")
    print("Suddenly, a small bat drops from the window and swoops toward you!")
    print(bat_art)
    print("\nYou dodge quickly, and the bat circles around, heading back to the throne.\n"
          "In a swirl of dark mist, the bat morphs into a pale figure clad in regal attire.\n"
          "He reveals himself with a cold, echoing laugh:\n")
    print(vampire_art)
    print("\"I am Cazador, the King of Vampires... Ruler of this forsaken domain.\"\n")
    print("He casts a twisted grin, baring his fangs:\n")
    print("\"Your blood will be a fine vintage. Prepare yourself for my eternal night!\"\n")


    vampire_hp = random.randint(8, 18)
    vampire_cs = random.randint(3, 6)
    print("    |    Cazador's Combat Strength:", vampire_cs)
    print("    |    His pale skin glimmers with dark power. Health Points:", vampire_hp)

    while vampire_hp > 0 and health_points > 0:
        print("\n    |", end="    ")
        input("Roll to see who strikes first against the Vampire (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if attack_roll % 2 != 0:

            print("    |", end="    ")
            input("You attack Cazador (Press enter)")
            vampire_hp, health_points = functions.hero_attacks(combat_strength, vampire_hp, lifesteal,
                                                               health_points)
            if vampire_hp == 0:
                num_stars = 2
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    Cazador lunges at you with supernatural speed! (Press enter)")
                health_points, shield = functions.monster_attacks(vampire_cs, health_points, shield, 0)
                if shield > 0:
                    shield += shield_regen
                    print("    |    Your shield regenerates by " + str(shield_regen) +
                          " points. New shield value: " + str(shield))
                if health_points == 0:
                    num_stars = 1
        else:

            print("    |", end="    ")
            input("Cazador rushes forward in a blur! (Press enter)")
            health_points, shield = functions.monster_attacks(vampire_cs, health_points, shield, 0)
            if shield > 0:
                shield += shield_regen
                print("    |    Your shield regenerates by " + str(shield_regen) +
                      " points. New shield value: " + str(shield))
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    You seize a moment to strike back! (Press enter)")
                vampire_hp, health_points = functions.hero_attacks(combat_strength, vampire_hp, lifesteal,
                                                                   health_points)
                if vampire_hp == 0:
                    num_stars = 2

    if vampire_hp <= 0:
        print("\nCazador collapses onto his throne, dissolving into ashes!")
        print("\"You may have... defeated me... but darkness never dies...\"")
        print("With his last breath, the throne room falls eerily silent.\n")
        winner_vamp = "Hero"
    else:
        print("\nYour lifeblood has been drained by Cazador. The reign of the Vampire King continues...")
        winner_vamp = "Monster"
        exit()  

    print("------------------------------------------------------------------")
    print("As you catch your breath, a figure steps out from behind the throne's pillar.")
    print("He wears tattered robes stained with strange elixirs, a sorrowful look on his face.\n")
    print(alchemist_art)
    print("He speaks softly:\n")
    print("\"I was forced to brew potions for Cazador's army... Thank you for freeing me.\"")
    print("\"I am but an Alchemist, longing to escape this nightmare. Here, take this gift.\"")
    print("\"May it restore you for the challenges yet to come.\" \n")


    alchemist_heal = random.randint(5, 15)
    old_hp = health_points
    health_points = min(100, health_points + alchemist_heal)
    print(f"The Alchemist hands you a sparkling vial. You drink it, healing {alchemist_heal} HP.")
    print(f"Your health rises from {old_hp} to {health_points}.\n")

    print("He bows in gratitude and slips away into the shadows...\n")


    print("As the ashes of Cazador's defeat settle, a mysterious parchment flutters at your feet.")
    print("The ancient script reveals a prophecy: the true source of darkness lies beyond vampiric tyranny,")
    print("hidden deep beneath a dormant volcano where a colossal Dragon has awakened.")
    print("With renewed determination and the mystical artifacts you've gathered,")
    print("you set forth to confront this fiery menace and restore hope to the kingdom.\n")

    print(dragon_art)
    print("    |    You meet the dragon. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if attack_roll % 2 != 0:
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal,
                                                                    health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The dragon strikes (Press enter)!!!")
                health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, 0)
                if shield > 0:
                    shield += shield_regen
                    print("    |    Your shield regenerates by " + str(shield_regen) +
                          " points. New shield value: " + str(shield))
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The dragon strikes (Press enter)")
            health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, 0)
            if shield > 0:
                shield += shield_regen
                print("    |    Your shield regenerates by " + str(shield_regen) +
                      " points. New shield value: " + str(shield))
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The hero strikes!! (Press enter)")
                m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal,
                                                                        health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if m_health_points <= 0:
        winner = "Hero"
        print("\nYou defeated the dragon!")


        hero_obj = Hero()
        hero_obj.combat_strength = combat_strength
        hero_obj.health_points = health_points
        hero_obj.inventory = []

    
        monster_obj = Monster()

        monster_obj.loot = ["Amulet of Power", "Golden Sword", "Minor Ring", "Boots of Speed"]

        print("\nCollecting artifacts from the defeated monster...")
        new_artifacts = [a for a in monster_obj.loot if a not in hero_obj.inventory]
        hero_obj.inventory.extend(new_artifacts)
        print("Artifacts collected:", hero_obj.inventory)

        if hero_obj.combat_strength > 4:
            if 'Amulet of Power' in hero_obj.inventory:
                hero_obj.combat_strength += 2
                print("Artifact effect applied: Amulet of Power increases combat strength by 2.")
            elif 'Golden Sword' in hero_obj.inventory:
                hero_obj.combat_strength += 3
                print("Artifact effect applied: Golden Sword increases combat strength by 3.")
        else:
            if 'Minor Ring' in hero_obj.inventory:
                hero_obj.health_points += 2
                print("Artifact effect applied: Minor Ring increases health points by 2.")
            elif 'Boots of Speed' in hero_obj.inventory:
                hero_obj.combat_strength += 1
                print("Artifact effect applied: Boots of Speed increases combat strength by 1.")


        combat_strength = hero_obj.combat_strength
        health_points = hero_obj.health_points
    else:
        winner = "Monster"
        print("You lost the fight with the dragon! Game over.")
        exit()

    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words): ")
        name_parts = hero_name.split()
        if len(name_parts) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        elif not (name_parts[0].isalpha() and name_parts[1].isalpha()):
            print("    |    Please enter an alphabetical name")
            tries += 1
        else:
            short_name = name_parts[0][:2] + name_parts[1][:1]
            print("    |    I'm going to call you " + short_name + " for short")
            input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
        print("    ------------------------------------------------------------------------------------------------------------")
        print("    |    Game saved")
        print("    ------------------------------------------------------------------------------------------------------------")
        print("    |    Thank you for playing")
        print("    ------------------------------------------------------------------------------------------------------------")
        print("    |    Game created by Gustavo Miranda, Lucas Tavares Criscuolo, Carlos Figuera La Riva and Breno Lopes Mafra")
        print("    ------------------------------------------------------------------------------------------------------------")