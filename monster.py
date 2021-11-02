import random


class Monster:
    def __init__(self):
        self.attack = random.randint(10, 25)
        self.health = 150
        self.bleed = 1
        self.critical = ["[CRITICAL]\nThe beast is an apex predator, you will not escape.",
                         "[CRITICAL]\nThe werewolf shreds whats left of your torso and will to live.",
                         "[CRITICAL]\nThe creature lunges and sinks its teeth into your arm, if you survive you "
                         "will suffer "
                         "for the rest of your life"]

        self.death = [
            "The werewolf crumples to the ground and shudders. It yips and growls as it struggles to move.\nAfter a "
            "couple minutes the creature slows down until all you can see is its body heave with every breath.",
            "The beast struggles to stay standing on its hind legs. It whines as it takes one labored step after "
            "another.\nThe creature glances at you with something akin to sadness.",
            "The creature falls on its forelimbs and stares up at the night sky.\nIt howls softly at the moon as if "
            "afraid to wake the slumbering forest."]

        self.miss = [
            "The werewolf scratches your arm enough to make the skin red, but not enough to draw blood. Still hurts...",
            "The werewolf attempts to clobber you, but instead it hits you with the back of its hand",
            "The beast swipes at you but instead hits your sword. You manage to hold on but the force crawls up your "
            "arm instead."]

        self.above_avg = ["The creature strikes a hinge joint and decimates the cartilage beneath.",
                          "The werewolf barrels into you with enough force that it sends you flying to the edge "
                          "of the "
                          "clearing.",
                          "The werewolf roars, its reverberating decibel level increases the cortisol production in "
                          "your "
                          "body."]

        self.average = ["The werewolf clubs your body with its meaty paws.",
                        "The creature drop kicks you with its powerful hindquarters.",
                        "The creature slashes your body leaving streaks of dark red behind."]

        self.below_average = ["The creature's claws glance off your shoulder.",
                              "The werewolf hits you square in the chest, but your adrenaline postpones the pain.",
                              "The beast slashes a part of your body with no blood in it. How peculiar..."]

        self.slay_loot = ["[ITEM] Monstrous Hide", "[ITEM] Savage Canines", "[ITEM] Thick Claws"]

        self.special_slay_loot = ["[SECRET ITEM] Pungent Feces (Common)", "[SECRET ITEM] Nocturnal Eyes (Rare)",
                                  "[SECRET ITEM] Vial of Pure Blood (Legendary)"]

        self.mercy_loot = ["[ITEM] Golden Sword"]

        self.special_mercy_loot = ["[SECRET ITEM] Lightly Used Fleshlight (Common)",
                                   "[SECRET ITEM] Imbued Iron Bar (Rare)",
                                   "[SECRET ITEM] Brilliant Sapphire (Legendary)"]

    def heavy_damage(self, damage):
        self.health = self.health - damage
        self.health = self.health - self.bleed
        print(f"The werewolf took {damage} damage and {self.bleed} [BLEED] damage.")

    def damage(self, damage):
        self.heavy_damage(damage)
        self.bleed = self.bleed + 1

    def throw_damage(self, damage):
        self.heavy_damage(damage)
        self.bleed = self.bleed + 3
