import random
from monster import Monster
from art import logo

werewolf = Monster()


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


achievement = ["[ACHIEVEMENT] EXECUTIONER: Kill the werewolf by throwing your sword"]
sword_crit = ["[CRITICAL]\n[STUN]\nEither by luck or skill, your blade rips through its hide at the perfect angle. ",
              "[CRITICAL]\n[STUN]\nYou're swift attack brutalizes the creature both physically and emotionally.",
              "[CRITICAL]\n[STUN]\nYour blade rips through the werewolf with no hesitation. The steel soaks in the "
              "blood."]
sword_above_avg = ["[STUN]\nYour blade slices your enemy and draws blood.",
                   "[STUN]\nYour sword dances in your hand as you slice and dice.",
                   "[STUN]\nYour blade moves so quick its a blur."]
sword_avg = ["Your sword hits your opponent No more, no less.",
             "You lunge and puncture your opponent. How average.",
             "Your sword says hello with the werewolf. The werwolf responds by bleeding."]
sword_below_avg = ["Your technique is off and your enthusiasm is pitiful.",
                   "Your blade glances off your opponent like its afraid to hurt them",
                   "Your should have spent more time practicing with your sword rather than polishing it."]
sword_miss = ["Your father raised a disgrace.",
              "Your blade whistles in the air.",
              "Nothing happens.",
              "You're a monkey with a stick."]

evade_succ = ["You pivot around the lumbering werewolf to open space.",
              "You successfully bought yourself some time.",
              "You dash away from the beast."]
evade_miss = ["You attempt to skirt around the beast but trip on a small stone instead.",
              "The werewolf's petrifying gaze roots you to the spot.",
              "The masochist in you wants the pain. You let the werewolf hit you."]
heavy_sword_crit = ["[CRITICAL]\nYour weapon no longer cuts, it smashes, and you just dropped the hammer.",
                    "[CRITICAL]\nYou crash the sword into the werewolf. Your muscles contract so hard they tear, but you decimate the werewolf's bones",
                    "[CRITICAL]\nYour body rips past its natural limits as you slam the hilt of the sword into the wereolf's skull. The hilt warps in your terrifying grip."]
heavy_sword_above_avg = ["Years of fury allows you to wallop the beast.",
                         "You sword hits the beast with a mighty crash.",
                         "Your sword whizzes through the air and steel meets blood."]
heavy_sword_avg = ["You slam the sword into the beast.",
                   "Your attack is the exact same as a regular attack except you use both hands this time.",
                   "You are angry and you have a pointy stick. 2 + 2 = 4"]
heavy_sword_below_avg = ["You wield the sword with the finesse of a hungry ape",
                         "Your heavy attack glances off the beast's hide, but still holds significant force behind it.",
                         "Your muscles fail you, your heavy attack is weakened."]
throw_sword_crit = ["[CRITICAL]\nYou have thrown things all your life and it shows.",
                    "[CRITICAL]\nYou hurl your sword at the werewolf and it rips through the beast like a bullet.",
                    "[CRITICAL]\nYour sword flies so fast it somehow breaks the sound barrier."]
throw_sword_above_avg = ["Your sword flies true and buries itself into the belly of the beast.",
                         "You throw the sword with impressive speed.",
                         "The flying sword manages to slice the werewolf."]
throw_sword_avg = ["You throw the sword and it hits the beast. Simple as that.",
                   "You fling the sword at the creature and manage to hurt it.",
                   "You lob the sword at the werewolf and it cuts the beast."]
throw_sword_below_avg = ["You fling the sword at the werewolf with the power of a small child.",
                         "You throw the sword but manage to hit the beast with the hilt instead of the blade.",
                         "Your throw your blade but the sword moves so slow it merely pokes the werewolf."]
throw_sword_miss = ["You throw your sword with enough power to split a tree, too bad it flies directly over the beast",
                    "You wind back to throw your sword but let go to early. Instead of the sword hitting the werewolf it falls behind you.",
                    "Millions of years of evolution gave humans the dexterity and precision to throw things with accuracy. You are the exception to evolution."]


def rand_int():
    import random
    return random.randint(0, 20)


def rand_int_heavy_attack():
    import random
    return random.randint(10, 30)


def rand_int_throw_sword():
    import random
    return random.randint(15, 25)


def mercy():
    print("Your hand trembles as you stand before the werwolf, but you stand still and watch.")
    print("Hours pass as you stand vigilant. Finally, the rays of the sun peak over the horizon.")
    print("As the beams of the sun hit the beast, the werewolf began to morph.")
    print("Fur fell in clumps, claws crumbled, canines fell out, and muscles shrunk.")
    print("A man in rags stands before you. It was still Adolphus.")
    print(
        "'Thank you traveler, I didn't think you could do it. Who knows what else I would've done if you hadn't stopped me.")
    print("'Here, take this.'")
    print(
        "Adolphus stumbles toward the forgotten boxes slung near a tree and picked them up. Adolphus murmered a few words before he reaches elbow-deep into the small bag.")
    print(werewolf.mercy_loot)
    print(random.choice(werewolf.special_mercy_loot))
    print("As you pick up the golden sword, a jolt of electricity runs through you.")
    print(
        "'That's a gold-copper alloy, gives you the higher tensile strength of the copper, but the magical properties of the sword. Use it well'")
    print(
        "Adolphus hobbles into the woods with his boxes. You toss the battered sword aside as you inspect your new sword.")
    print("Your grip the sword with renewed aplomb and scream at the burgeoning sun.")
    play_again()


def slay():
    print("You kick the werewolf over before plunging your sword hilt-deep into the belly of the beast.")
    print("A mighty roar rattles your bones before the creature's heart beats for the last time.")
    print("You plunder the beast for its valuables.")
    print(werewolf.slay_loot)
    print(random.choice(werewolf.special_slay_loot))
    print("You sling the hide over your body and head to town.\nThe moon above shines upon you.")
    play_again()


def resolution():
    print("With the sword in your hand you approach the broken beast.")
    print("Do you let the creature live? (MERCY)\nDo you slay the werewolf once and for all? (SLAY)")
    final_choice = input(">").upper()
    if "MERCY" in final_choice:
        mercy()
    elif "SLAY" in final_choice:
        slay()


def attack_sword():
    user_health = 115
    bleed = 1
    while user_health > 0:
        while werewolf.health > 0:
            print(f"Werewolf Health: {werewolf.health}/150")
            print("User Health: " + str(user_health) + "/115\n")
            attack = input("Attack with sword (ATTACK)\nEvade (EVADE)\n>").upper()
            if "ATTACK" in attack:
                damage = rand_int()
                damage2 = werewolf.attack
                if damage == 20:
                    print(random.choice(sword_crit))
                    damage = damage * 1.5
                    werewolf.health = werewolf.health - damage
                    werewolf.health = werewolf.health - bleed
                    print("The werewolf took " + str(damage) + " damage and " + str(bleed) + " [BLEED] damage.")
                    bleed = bleed + 1
                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                elif 16 <= damage <= 19:
                    print(random.choice(sword_above_avg))
                    werewolf.health = werewolf.health - damage
                    werewolf.health = werewolf.health - bleed
                    print("The werewolf took " + str(damage) + " damage and " + str(bleed) + " [BLEED] damage.")
                    bleed = bleed + 1
                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                elif 6 <= damage <= 15:
                    print(random.choice(sword_avg))
                    werewolf.health = werewolf.health - damage
                    werewolf.health = werewolf.health - bleed
                    print("The werewolf took " + str(damage) + " damage and " + str(bleed) + " [BLEED] damage.")
                    bleed = bleed + 1
                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        damage2 = werewolf.attack
                        if damage2 == 25:
                            print(random.choice(werewolf.critical))
                            damage2 = damage2 * 1.5
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 21 <= damage2 <= 24:
                            print(random.choice(werewolf.above_avg))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 16 <= damage2 <= 20:
                            print(random.choice(werewolf.average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 11 <= damage2 <= 15:
                            print(random.choice(werewolf.below_average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif damage2 == 10:
                            print(random.choice(werewolf.miss))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                elif 1 <= damage <= 5:
                    print(random.choice(sword_below_avg))
                    werewolf.health = werewolf.health - damage
                    werewolf.health = werewolf.health - bleed
                    print("The werewolf took " + str(damage) + " damage and " + str(bleed) + " [BLEED] damage.")
                    bleed = bleed + 1
                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        damage2 = werewolf.attack
                        if damage2 == 25:
                            print(random.choice(werewolf.critical))
                            damage2 = damage2 * 1.5
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 21 <= damage2 <= 24:
                            print(random.choice(werewolf.above_avg))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 16 <= damage2 <= 20:
                            print(random.choice(werewolf.average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 11 <= damage2 <= 15:
                            print(random.choice(werewolf.below_average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif damage2 == 10:
                            print(random.choice(werewolf.miss))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                elif damage == 0:
                    print(random.choice(sword_miss))
                    werewolf.health = werewolf.health - damage
                    werewolf.health = werewolf.health - bleed
                    print("The werewolf took " + str(damage) + " damage and " + str(bleed) + " [BLEED] damage.")
                    bleed = bleed + 1
                    if werewolf.health <= 0:
                        print(random.choice(werewolf.death))
                        resolution()
                    else:
                        damage2 = werewolf.attack()
                        if damage2 == 25:
                            print(random.choice(werewolf.critical))
                            damage2 = damage2 * 1.5
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 21 <= damage2 <= 24:
                            print(random.choice(werewolf.above_avg))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 16 <= damage2 <= 20:
                            print(random.choice(werewolf.average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif 11 <= damage2 <= 15:
                            print(random.choice(werewolf.below_average))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                        elif damage2 == 10:
                            print(random.choice(werewolf.miss))
                            user_health = user_health - damage2
                            print("You take " + str(damage2) + " damage.")
                if user_health <= 0:
                    print("You die.")
                    game_over()
            elif "EVADE" in attack:
                evade = rand_int()
                damage = rand_int()
                damage2 = werewolf.attack()
                heavy_attack = rand_int_heavy_attack()
                throw_sword = rand_int_throw_sword()
                if evade >= 11:
                    print(random.choice(evade_succ))
                    evade_op2 = input("What will you do?\n"
                                      "Heavy attack (HEAVY)\n"
                                      "Throw Sword (SPECIAL)\n"
                                      ">").upper()
                    if "HEAVY" in evade_op2:
                        if heavy_attack == 30:
                            print(random.choice(heavy_sword_crit))
                            heavy_attack = heavy_attack * 1.75
                            werewolf.health = werewolf.health - heavy_attack
                            werewolf.health = werewolf.health - bleed
                            print("The werewolf took " + str(heavy_attack) + " damage and " + str(
                                bleed) + " [BLEED] damage. ")
                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()
                        elif 27 <= heavy_attack <= 29:
                            print(random.choice(heavy_sword_above_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.health = werewolf.health - heavy_attack
                            werewolf.health = werewolf.health - bleed
                            print("The werewolf took " + str(heavy_attack) + " damage and " + str(
                                bleed) + " [BLEED] damage. ")
                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()
                        elif 16 <= heavy_attack <= 26:
                            print(random.choice(heavy_sword_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.health = werewolf.health - heavy_attack
                            werewolf.health = werewolf.health - bleed
                            print("The werewolf took " + str(heavy_attack) + " damage and " + str(
                                bleed) + " [BLEED] damage. ")
                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()
                        elif 11 <= heavy_attack <= 15:
                            print(random.choice(heavy_sword_below_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.health = werewolf.health - heavy_attack
                            werewolf.health = werewolf.health - bleed
                            print("The werewolf took " + str(heavy_attack) + " damage and " + str(
                                bleed) + " [BLEED] damage. ")
                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()
                        elif heavy_attack == 10:
                            print(random.choice(heavy_sword_below_avg))
                            heavy_attack = heavy_attack * 1.50
                            werewolf.health = werewolf.health - heavy_attack
                            werewolf.health = werewolf.health - bleed
                            print("The werewolf took " + str(heavy_attack) + " damage and " + str(
                                bleed) + " [BLEED] damage. ")
                            if werewolf.health <= 0:
                                print(random.choice(werewolf.death))
                                resolution()
                    else:
                        if evade >= 6:
                            if throw_sword == 25:
                                print(random.choice(throw_sword_crit))
                                throw_sword = throw_sword * 1.50
                                werewolf.health = werewolf.health - throw_sword
                                werewolf.health = werewolf.health - bleed
                                print("The werewolf took " + str(throw_sword) + " damage and " + str(
                                    bleed) + " [BLEED] damage")
                                bleed = bleed + 3
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(achievement)
                                    resolution()
                            elif 21 <= throw_sword <= 24:
                                print(random.choice(throw_sword_above_avg))
                                werewolf.health = werewolf.health - throw_sword
                                werewolf.health = werewolf.health - bleed
                                print("The werewolf took " + str(throw_sword) + " damage and " + str(
                                    bleed) + " [BLEED] damage")
                                bleed = bleed + 3
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(achievement)
                                    resolution()
                            elif 16 <= throw_sword <= 20:
                                print(random.choice(throw_sword_avg))
                                werewolf.health = werewolf.health - throw_sword
                                werewolf.health = werewolf.health - bleed
                                print("The werewolf took " + str(throw_sword) + " damage and " + str(
                                    bleed) + " [BLEED] damage")
                                bleed = bleed + 3
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(achievement)
                                    resolution()
                            elif throw_sword == 15:
                                print(random.choice(throw_sword_below_avg))
                                werewolf.health = werewolf.health - throw_sword
                                werewolf.health = werewolf.health - bleed
                                print("The werewolf took " + str(throw_sword) + " damage and " + str(
                                    bleed) + " [BLEED] damage")
                                bleed = bleed + 3
                                if werewolf.health <= 0:
                                    print(random.choice(werewolf.death))
                                    print(achievement)
                                    resolution()
                        else:
                            print(random.choice(throw_sword_miss))
                            damage2 = werewolf.attack()
                            if damage2 == 25:
                                print(random.choice(werewolf.critical))
                                damage2 = damage2 * 2
                                user_health = user_health - damage2
                                print("You take " + str(damage2) + " damage. ")
                            elif 21 <= damage2 <= 24:
                                print(random.choice(werewolf.above_avg))
                                damage2 = damage2 * .75
                                user_health = user_health - damage2
                                print("You take " + str(damage2) + " damage. ")
                            elif 16 <= damage2 <= 20:
                                print(random.choice(werewolf.average))
                                damage2 = damage2 * .75
                                user_health = user_health - damage2
                                print("You take " + str(damage2) + " damage. ")
                            elif 11 <= damage2 <= 15:
                                print(random.choice(werewolf.below_average))
                                damage2 = damage2 * .55
                                user_health = user_health - damage2
                                print("You take " + str(damage2) + " damage. ")
                            elif damage2 == 10:
                                print(random.choice(werewolf.miss))
                                damage2 = damage2 * .75
                                user_health = user_health - damage2
                                print("You take " + str(damage2) + " damage. ")
                elif evade <= 10:
                    print(random.choice(evade_miss))
                    damage2 = werewolf.attack()
                    if damage2 == 25:
                        print(random.choice(werewolf.critical))
                        damage2 = damage2 * 1.5
                        user_health = user_health - damage2
                        print("You take " + str(damage2) + " damage. ")
                    elif 21 <= damage2 <= 24:
                        print(random.choice(werewolf.critical))
                        damage2 = damage2 * .75
                        user_health = user_health - damage2
                        print("You take " + str(damage2) + " damage. ")
                    elif 16 <= damage2 <= 20:
                        print(random.choice(werewolf.average))
                        damage2 = damage2 * .75
                        user_health = user_health - damage2
                        print("You take " + str(damage2) + " damage. ")
                    elif 11 <= damage2 <= 15:
                        print(random.choice(werewolf.below_average))
                        damage2 = damage2 * .75
                        user_health = user_health - damage2
                        print("You take " + str(damage2) + " damage. ")
                    elif damage2 == 10:
                        print(random.choice(werewolf.miss))
                        damage2 = damage2 * .75
                        user_health = user_health - damage2
                        print("You take " + str(damage2) + " damage. ")
                if user_health <= 0:
                    print("You die.")
                    game_over()


def rising_act1():
    print("'Don't hold back! When I- argh.' A gutteral growl escapes from his throat and he grimaces.")
    print("Apolphus kicks the box away and looks to the night sky with a grizzly smile.")
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
        "A hairy man approaches you with a solemn smile. You reach for your weapon but you realize you didn't bring it with you")
    print("'Fear not traveler, the sun has not set yet.'")

    ask_q1()


title_screen()
