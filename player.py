import random
# from adventure import werewolf


class Player:
    def __init__(self):
        self.health = 115
        self.evade = random.randint(0, 20)
        self.attack = random.randint(0, 20)
        self.heavy_attack = random.randint(10, 30)
        self.throw_sword = random.randint(15, 25)

        self.achievement = ["[ACHIEVEMENT] EXECUTIONER: Kill the werewolf by throwing your sword"]

        self.sword_critical = [
            "[CRITICAL]\n[STUN]\nEither by luck or skill, your blade rips through its hide at the perfect angle. ",
            "[CRITICAL]\n[STUN]\nYou're swift attack brutalizes the creature both physically and emotionally.",
            "[CRITICAL]\n[STUN]\nYour blade rips through the werewolf with no hesitation. The steel soaks in the "
            "blood."]
        self.sword_above_average = ["[STUN]\nYour blade slices your enemy and draws blood.",
                                    "[STUN]\nYour sword dances in your hand as you slice and dice.",
                                    "[STUN]\nYour blade moves so quick its a blur."]

        self.sword_average = ["Your sword hits your opponent No more, no less.",
                              "You lunge and puncture your opponent. How average.",
                              "Your sword says hello with the werewolf. The werewolf responds by bleeding."]

        self.sword_below_average = ["Your technique is off and your enthusiasm is pitiful.",
                                    "Your blade glances off your opponent like its afraid to hurt them",
                                    "Your should have spent more time practicing with your sword rather than "
                                    "polishing it."]

        self.sword_miss = ["Your father raised a disgrace.",
                           "Your blade whistles in the air.",
                           "Nothing happens.",
                           "You're a monkey with a stick."]

        self.evade_successful = ["You pivot around the lumbering werewolf to open space.",
                                 "You successfully bought yourself some time.",
                                 "You dash away from the beast."]

        self.evade_miss = ["You attempt to skirt around the beast but trip on a small stone instead.",
                           "The werewolf's petrifying gaze roots you to the spot.",
                           "The masochist in you wants the pain. You let the werewolf hit you."]

        self.heavy_sword_critical = ["[CRITICAL]\nYour weapon no longer cuts, it smashes, and you just dropped the "
                                     "hammer.",
                                     "[CRITICAL]\nYou crash the sword into the werewolf. Your muscles contract so "
                                     "hard they "
                                     "tear, but you decimate the werewolf's bones",
                                     "[CRITICAL]\nYour body rips past its natural limits as you slam the hilt of the "
                                     "sword into the werewolf's skull. The hilt warps in your terrifying grip."]

        self.heavy_sword_above_avg = ["Years of fury allows you to wallop the beast.",
                                      "You sword hits the beast with a mighty crash.",
                                      "Your sword whizzes through the air and steel meets blood."]

        self.heavy_sword_avg = ["You slam the sword into the beast.",
                                "Your attack is the exact same as a regular attack except you use both hands this time",
                                "You are angry and you have a pointy stick. 2 + 2 = 4"]

        self.heavy_sword_below_avg = ["You wield the sword with the finesse of a hungry ape",
                                      "Your heavy attack glances off the beast's hide, but still holds significant "
                                      "force "
                                      "behind it.",
                                      "Your muscles fail you, your heavy attack is weakened."]

        self.throw_sword_crit = ["[CRITICAL]\nYou have thrown things all your life and it shows.",
                                 "[CRITICAL]\nYou hurl your sword at the werewolf and it rips through the beast like a "
                                 "bullet.",
                                 "[CRITICAL]\nYour sword flies so fast it somehow breaks the sound barrier."]

        self.throw_sword_above_avg = ["Your sword flies true and buries itself into the belly of the beast.",
                                      "You throw the sword with impressive speed.",
                                      "The flying sword manages to slice the werewolf."]

        self.throw_sword_avg = ["You throw the sword and it hits the beast. Simple as that.",
                                "You fling the sword at the creature and manage to hurt it.",
                                "You lob the sword at the werewolf and it cuts the beast."]

        self.throw_sword_below_avg = ["You fling the sword at the werewolf with the power of a small child.",
                                      "You throw the sword but manage to hit the beast with the hilt instead of the "
                                      "blade.",
                                      "Your throw your blade but the sword moves so slow it merely pokes the werewolf."]

        self.throw_sword_miss = [
            "You throw your sword with enough power to split a tree, too bad it flies directly over the beast",
            "You wind back to throw your sword but let go to early. Instead of the sword hitting the werewolf it "
            "falls behind you.",
            "Millions of years of evolution gave humans the dexterity and precision to throw things with accuracy. "
            "You are the exception to evolution."]

    def player_damage(self, damage):
        self.health = self.health - damage
        print(f"You take {damage} damage. ")

    def mercy(self):
        print("Your hand trembles as you stand before the werewolf, but you stand still and watch.")
        print("Hours pass as you stand vigilant. Finally, the rays of the sun peak over the horizon.")
        print("As the beams of the sun hit the beast, the werewolf began to morph.")
        print("Fur fell in clumps, claws crumbled, canines fell out, and muscles shrunk.")
        print("A man in rags stands before you. It was still Adolphus.")
        print(
            "'Thank you traveler, I didn't think you could do it. Who knows what else I would've done if you hadn't "
            "stopped me.")
        print("'Here, take this.'")
        print(
            "Adolphus stumbles toward the forgotten boxes slung near a tree and picked them up. Adolphus murmured a "
            "few "
            "words before he reaches elbow-deep into the small bag.")
        print("As you pick up the golden sword, a jolt of electricity runs through you.")
        print(
            "'That's a gold-copper alloy, gives you the higher tensile strength of the copper, but the magical "
            "properties "
            "of the sword. Use it well'")
        print(
            "Adolphus hobbles into the woods with his boxes. You toss the battered sword aside as you inspect your new "
            "sword.")
        print("Your grip the sword with renewed aplomb and scream at the burgeoning sun.")

    def slay(self):
        print("You kick the werewolf over before plunging your sword hilt-deep into the belly of the beast.")
        print("A mighty roar rattles your bones before the creature's heart beats for the last time.")
        print("You plunder the beast for its valuables.")
        print("You sling the hide over your body and head to town.\nThe moon above shines upon you.")