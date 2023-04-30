import random

class MonsterGenerator():
    def __init__(self):
        self.types = ["Shadow", "Divide", "Undead", "Fire"]
        self.syllables = ["ar", "bar", "dar", "fa", "gal", "ka", "lo", "ma", "na", "ra", "sa", "ta", "va", "za"]
        self.prefixes = ["Al", "El", "Gal", "Il", "Kel", "Mal", "Nel", "Rel", "Sel", "Tel"]
        self.suffixes = ["dor", "en", "ia", "ian", "ius", "on", "or", "us"]

    def generate_monster(self):
        name = self.generate_name()
        attack = random.randint(0, 500) * 10 + random.choice([0, 5])
        defense = random.randint(0, 500) * 10 + random.choice([0, 5])
        speed = random.randint(10, 100) * 10
        type = random.choice(self.types)
        return {"name": name, "attack": attack, "defense": defense, "speed": speed, "type": type}
    
    def generate_name(self):
        # Choose a random number of syllables to use
        num_syllables = random.randint(2, 3)
        # Choose the syllables to use
        name_syllables = random.sample(self.syllables, k=num_syllables)
        # Combine the syllables into a name
        name = "".join(name_syllables)
        # Add a prefix or suffix to the name with a 50% probability
        if random.random() < 0.5:
            name = random.choice(self.prefixes) + name
        else:
            name += random.choice(self.suffixes)
        # Capitalize the name
        name = name.capitalize()
        return name
    
    def generate_monsters(self, amount = 20):
        data = [self.generate_monster() for _  in range(amount)]
        return data

monster_print = MonsterGenerator()
"""print(monster_print.generate_monsters(50))"""
