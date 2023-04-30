class Monster:
    def __init__(self, name, attack, defense, speed, type):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = type

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Type: {self.type}")