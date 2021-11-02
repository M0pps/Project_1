import random
from monster import Monster
from player import Player
from art import logo

player = Player()
werewolf = Monster()

game_is_on = True


def game_over():
    print("Game over.")
    play_again()


def play_again():
    print("Do you want to play again? (Yes or No)")
    answer2 = input(">").lower()
    if "yes" in answer2:
        title_screen()
    if "no" in answer2:
        game_over()


def title_screen():
    print(logo)
    answer2 = input(">").upper()
    if "START" in answer2:
        start()


def resolution():
    print("With the sword in your hand you approach the broken beast.")
    print("Do you let the creature live? (MERCY)\nDo you slay the werewolf once and for all? (SLAY)")
    final_choice = input(">").upper()
    if "MERCY" in final_choice:
        player.mercy()
        print(werewolf.mercy_loot)
        print(random.choice(werewolf.special_mercy_loot))
        play_again()
    elif "SLAY" in final_choice:
        player.slay()
        print(werewolf.slay_loot)
        print(random.choice(werewolf.special_slay_loot))
        play_again()


def werewolf_attack():
    damage2 = werewolf.attack
    if damage2 == 25:
        print(random.choice(werewolf.critical))
        damage2 = damage2 * 2
        player.player_damage(damage2)
    elif 21 <= damage2 <= 24:
        print(random.choice(werewolf.above_avg))
        damage2 = damage2 * .75
        player.player_damage(damage2)
    elif 16 <= damage2 <= 20:
        print(random.choice(werewolf.average))
        damage2 = damage2 * .75
        player.player_damage(damage2)
    elif 11 <= damage2 <= 15:
        print(random.choice(werewolf.below_average))
        damage2 = damage2 * .55
        player.player_damage(damage2)
    elif damage2 == 10:
        print(random.choice(werewolf.miss))
        damage2 = damage2 * .75
        player.player_damage(damage2)


def attack_sword():
    while player.health > 0:
        while werewolf.health > 0:
            print(f"Werewolf Health: {werewolf.health}/150")
            print(f"User Health: {player.health} / 115")
            attack = input("Attack with sword (ATTACK)\nEvade (EVADE)\n>").upper()
            if "ATTACK" in attack:
                if player.attack == 20:
                    print(random.choice(player.sword_critical))
                    damage = player.attack * 1.5
                    werewolf.damage(damage)

                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()

                elif 16 <= player.attack <= 19:
                    print(random.choice(player.sword_above_average))
                    werewolf.damage(player.attack)

                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()

                elif 6 <= player.attack <= 15:
                    print(random.choice(player.sword_average))
                    werewolf.damage(player.attack)

                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        werewolf_attack()

                elif 1 <= player.attack <= 5:
                    print(random.choice(player.sword_below_average))
                    werewolf.damage(player.attack)

                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        werewolf_attack()

                elif player.attack == 0:
                    print(random.choice(player.sword_miss))
                    werewolf.damage(player.attack)

                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        werewolf_attack()

                if player.health <= 0:
                    print("You die.")
                    game_over()

            elif "EVADE" in attack:
                evade = player.evade
                heavy_attack = player.heavy_attack
                throw_sword = player.throw_sword

                if evade >= 11:
                    print(random.choice(player.evade_successful))
                    evade_op2 = input("What will you do?\n"
                                      "Heavy attack (HEAVY)\n"
                                      "Throw Sword (SPECIAL)\n"
                                      ">").upper()

                    if "HEAVY" in evade_op2:
                        if heavy_attack == 30:
                            print(random.choice(player.heavy_sword_critical))
                            heavy_attack = heavy_attack * 1.75
                            werewolf.heavy_damage(heavy_attack)

                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()

                        elif 27 <= heavy_attack <= 29:
                            print(random.choice(player.heavy_sword_above_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.heavy_damage(heavy_attack)

                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()

                        elif 16 <= heavy_attack <= 26:
                            print(random.choice(player.heavy_sword_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.heavy_damage(heavy_attack)

                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()

                        elif 11 <= heavy_attack <= 15:
                            print(random.choice(player.heavy_sword_below_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.heavy_damage(heavy_attack)

                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()

                        elif heavy_attack == 10:
                            print(random.choice(player.heavy_sword_below_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.heavy_damage(heavy_attack)

                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()

                    else:
                        if evade >= 6:
                            if throw_sword == 25:
                                print(random.choice(player.throw_sword_crit))
                                throw_sword = throw_sword * 1.50
                                werewolf.throw_damage(throw_sword)
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(player.achievement)
                                    resolution()
                            elif 21 <= throw_sword <= 24:
                                print(random.choice(player.throw_sword_above_avg))
                                werewolf.throw_damage(throw_sword)
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(player.achievement)
                                    resolution()
                            elif 16 <= throw_sword <= 20:
                                print(random.choice(player.throw_sword_above_avg))
                                werewolf.throw_damage(throw_sword)
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(player.achievement)
                                    resolution()
                            elif throw_sword == 15:
                                print(random.choice(player.throw_sword_below_avg))
                                werewolf.throw_damage(throw_sword)
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(player.achievement)
                                    resolution()
                        else:
                            print(random.choice(player.throw_sword_miss))
                            werewolf_attack()
                elif evade <= 10:
                    print(random.choice(player.evade_miss))
                    werewolf_attack()
                if player.health <= 0:
                    print("You die.")
                    game_over()


def rising_act1():
    print("'Don't hold back! When I- argh.' A guttural growl escapes from his throat and he grimaces.")
    print("Adolphus kicks the box away and looks to the night sky with a grizzly smile.")
    print("The man's muscles bulged and a mighty scream erupted from his throat.")
    print("Hair sprouted from fur, claws sprung from nails, and sabres grew from teeth.")
    print("Clothed in rags, a werewolf crouches in front of you.")
    print("What do you do?")
    attack_sword()


def ask_q1():
    print("'I'm Adolphus, and I have something for you'")
    print("Adolphus places a wood box in front of you and opens the lid")
    print("The box contains a shining sword")
    print("Pick up the weapon (Type: SWORD)")
    weapon = input(">").lower()
    if "sword" in weapon:
        print("You pick up the sword. It shudders in your grip.")
        rising_act1()
    else:
        print("You did not include 'SWORD',  in your answer. Most people get this on the first try.")
        print("Do you want to play again? (Yes or No)")
        answer4 = input(">").lower()
        if "yes" in answer4:
            start()
        else:
            game_over()


def start():
    print("You walk along a forested path while the sun begins to set behind you.")
    print(
        "A hairy man approaches you with a solemn smile. You reach for your weapon but you realize you didn't bring "
        "it with you")
    print("'Fear not traveler, the sun has not set yet.'")

    ask_q1()


title_screen()
