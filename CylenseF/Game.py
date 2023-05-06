from Monster import Monster
import random
import time
from os import system
from sys import platform
from NameGen import MonsterGenerator


class Game:
    def __init__(self):
        self.game_state = "game_over"
        self.is_my_turn = False
        self.my_turn_count = 0
        self.opponent_turn_count = 0
        self.gui = None

        self.data = MonsterGenerator().generate_monsters(50)
        self.cards = [Monster(**card) for card in self.data]
        random.shuffle(self.cards)
        print(self.cards)
        self.card_names = [f"ID{i}" for i in range(1, 51)]

        half = len(self.cards) // 2
        self.player_deck = self.cards[:half]
        self.bot_deck = self.cards[half:]

        self.player_hand = random.sample(self.player_deck, 5)  # hand(s) creation
        self.bot_hand = random.sample(self.bot_deck, 5)

        self.player_life = 10000  # lifepoints
        self.bot_life = 10000
        self.player_field = []  # create field
        self.bot_field = []
        self.dice = 1
        self.optionG = ["gamble", "Gamble"]
        self.optionD = ["draw", "Draw"]
        self.optionP = ["place", "Place"]
        self.optionA = ["attack", "Attack"]
        self.optionI = ["info", "Info"]

        self.player_speed = (
            self.player_hand[0].speed
            + self.player_hand[1].speed
            + self.player_hand[2].speed
            + self.player_hand[3].speed
            + self.player_hand[4].speed
        )
        self.average_player_speed = (
            self.player_speed / 5
        )  # average speed of player #used to calculate which user starts first (user with faster average hand starts first)

        self.bot_speed = (
            self.bot_hand[0].speed
            + self.bot_hand[1].speed
            + self.bot_hand[2].speed
            + self.bot_hand[3].speed
            + self.bot_hand[4].speed
        )
        self.average_bot_speed = self.bot_speed / 5  # average speed of bot

    @staticmethod
    def clear_screen():
        system("cls" if platform == "win32" else "clear")

    def playerGameStatus(self):  # playerGameStatus
        names = [card.name for card in self.player_hand]
        player_alive = [card.name for card in self.player_field]
        bot_alive = [card.name for card in self.bot_field]
        self.clear_screen()
        print("playerGameStatus:")
        print("Your HP: " + str(self.player_life))
        print("Opponent's HP: " + str(self.bot_life))
        print("Your hand: " + ", ".join(names))
        print("Your field: " + ", ".join(player_alive))
        print("Opponent's field: " + ", ".join(bot_alive))
        print("")
        print("Turn: yours")
        print("self.Dice count: " + str(self.dice))
        print("")

    def botGamesStatus(self):  # playerGameStatus
        names = [card.name for card in self.player_hand]
        player_alive = [card.name for card in self.player_field]
        bot_alive = [card.name for card in self.bot_field]
        self.clear_screen()
        print("playerGameStatus:")
        print("Your HP: " + str(self.player_life))
        print("Opponent's HP: " + str(self.bot_life))
        print("Your hand: " + ", ".join(names))
        print("Your field: " + ", ".join(player_alive))
        print("Opponent's field: " + ", ".join(bot_alive))
        print("")
        print("self.Dice count: " + str(self.dice))
        print("Turn: opponents")
        print("")

    def playerGamble(self):  # player gamble
        if self.dice == 0:
            print("No dice left!")
            self.gui.append_text("No dice left!")
        if self.dice >= 1:
            self.dice = self.dice - 1
            self.player_life
            self.bot_life
            decision = random.randint(1, 6)
            if decision == 1:
                dmg = [1000, 2000, 3000, 4000]
                dmg_chosen = random.choice(dmg)
                self.player_life = self.player_life - dmg_chosen
                self.playerGameStatus()
                self.gui.append_text(
                    "You've shot yourself in the foot and lost "
                    + str(dmg_chosen)
                    + " HP."
                )
            if decision == 2:
                dmg = [1000, 2000]
                dmg_chosen = random.choice(dmg)
                self.bot_life = self.bot_life - dmg_chosen
                self.playerGameStatus()
                self.gui.append_text(
                    "You shot your opponent with a banana pistol, they lost "
                    + str(dmg_chosen)
                    + " HP."
                )
            if decision == 3:
                self.player_field.clear()
                self.playerGameStatus()
                self.gui.append_text(
                    "You accidentally dropped an explosive into your field. All monsters have fainted."
                )
            if decision == 4:
                self.bot_field.clear()
                self.playerGameStatus()
                self.gui.append_text(
                    "You threw an explosive into the opponent's field. All monsters have fainted."
                )
            if decision == 5:
                self.player_hand.clear()
                self.playerGameStatus()
                self.gui.append_text(
                    "The wind blew away your all the cards in your hands."
                )
            if decision == 6:
                self.bot_hand.clear()
                self.playerGameStatus()
                self.gui.append_text(
                    "The wind blew away all the cards in your opponent's hands."
                )
            self.end_my_turn()

    def botGamble(self):  # bot gamble
        self.gui.append_text("Opponent is gambling...")
        decision = random.randint(1, 6)
        if decision == 1:
            dmg = [1000, 2000, 3000, 4000]
            dmg_chosen = random.choice(dmg)
            self.player_life = self.player_life - dmg_chosen
            self.botGamesStatus()
            self.gui.append_text(
                "Your opponent shot themselves in the foot and lost "
                + str(dmg_chosen)
                + " HP."
            )
        if decision == 2:
            dmg = [1000, 2000]
            dmg_chosen = random.choice(dmg)
            self.bot_life = self.bot_life - dmg_chosen
            self.botGamesStatus()
            self.gui.append_text(
                "You got shot with a banana pistol and lost " + str(dmg_chosen) + " HP."
            )
        if decision == 3:
            self.bot_field.clear()
            self.botGamesStatus()
            self.gui.append_text(
                "Your opponent accidentally dropped an explosive into their field. All monsters have fainted."
            )
        if decision == 4:
            self.player_field.clear()
            self.botGamesStatus()
            self.gui.append_text(
                "Your opponent threw an explosive into your field. All monsters have fainted."
            )
        if decision == 5:
            self.bot_hand.clear()
            self.botGamesStatus()
            self.gui.append_text(
                "The wind blew away all the cards in your opponent's hands."
            )
        if decision == 6:
            self.player_hand.clear()
            self.botGamesStatus()
            self.gui.append_text("The wind blew away your all the cards in your hand.")

    ## REMOVE?
    def diceP(self):
        chance = random.randint(1, 100)
        if chance <= 25:
            print("You randomly found a self.dice on the floor!")
            self.dice = self.dice + 1

    def playerDraw(self):  # player draw
        random_card = random.choice(self.player_deck)
        self.player_deck.remove(random_card)
        self.player_hand.append(random_card)
        self.playerGameStatus()
        self.gui.append_text("You drew " + str(random_card.name) + ".")
        self.end_my_turn()

    def botDraw(self):  # bot draw
        random_card = random.choice(self.bot_deck)
        self.bot_deck.remove(random_card)
        self.bot_hand.append(random_card)
        self.botGamesStatus()
        self.gui.append_text("Your opponent drew a card.")

    def playerPlace(self):  # player place
        self.playerGameStatus()
        while True:
            c = input("What card would you like to place down? ")
            card_found = False
            for card in self.player_hand:
                if card.name == c:
                    self.player_hand.remove(card)
                    self.player_field.append(card)
                    card_found = True
                    break
            if card_found:
                break
            print("ERROR: item not found.")
        self.playerGameStatus()
        self.gui.append_text("You have successfully placed down " + str(c) + ".")

    def botPlace(self):  # bot place
        random_number = random.randint(1, 3)
        if random_number == 1:
            card_choice = random.choice(self.bot_hand)
            self.bot_hand.remove(card_choice)
            self.bot_field.append(card_choice)
        if random_number == 2:
            card_choice = max(self.bot_hand, key=lambda x: x.attack)
            self.bot_hand.remove(card_choice)
            self.bot_field.append(card_choice)
        if random_number == 3:
            card_choice = max(self.bot_hand, key=lambda x: x.defense)
            self.bot_hand.remove(card_choice)
            self.bot_field.append(card_choice)
        self.botGamesStatus()
        self.gui.append_text(
            "Your opponent successfully placed down " + str(card_choice.name) + "."
        )

    def playerAttack(self):  # player attack
        while True:
            c = input("What card would you like to attack with? ")
            card_found = False
            for card in self.player_field:
                if card.name == c:
                    c = card
                    card_found = True
                    break
            if card_found:
                break
            print("ERROR: item not found.")
        if len(self.bot_field) > 0:
            self.bot_life
            self.player_life
            random_monster = random.choice(self.bot_field)
            if int(card.attack) > int(random_monster.defense):
                self.bot_field.remove(random_monster)
                dmg = card.attack - random_monster.defense
                self.bot_life = int(self.bot_life) - int(dmg)
                print(
                    card.name
                    + " attacked "
                    + random_monster.name
                    + ". Your opponent lost "
                    + str(dmg)
                    + " HP."
                )
            if int(card.attack) < int(random_monster.defense):
                self.player_field.remove(card)
                dmg = int(random_monster.defense) - int(card.attack)
                self.player_life = int(self.player_life) - int(dmg)
                print(
                    card.name
                    + " attacked "
                    + random_monster.name
                    + ". Attack unsuccessful, you lost "
                    + str(dmg)
                    + " HP."
                )
            if int(card.attack) == int(random_monster.defense):
                self.player_life = int(self.player_life) - 1000
                self.bot_life = int(self.bot_life) - 1000
                self.bot_field.remove(random_monster)
                self.player_field.remove(card)
                print(
                    card.name
                    + " attacked "
                    + random_monster.name
                    + ". Attack unsuccessful, both monsters have fainted."
                )
        else:
            self.bot_life = int(self.bot_life) - int(card.attack)
            print("You used " + card.name + " to attack your opponent directly.")

    def botAttack(self):  # bot attack
        highest_attack_obj = max(self.bot_field, key=lambda x: x.attack)
        if len(self.player_field) > 0:
            lowest_defense_obj = min(self.player_field, key=lambda x: x.defense)
            if (
                lowest_defense_obj is not None
                and highest_attack_obj.attack > lowest_defense_obj.defense
            ):
                dmg = highest_attack_obj.attack - lowest_defense_obj.defense
                self.player_field.remove(lowest_defense_obj)
                self.player_life = int(self.player_life) - int(dmg)
                self.botGamesStatus()
                self.gui.append_text(
                    highest_attack_obj.name
                    + " attacked "
                    + lowest_defense_obj.name
                    + ". You have lost "
                    + str(dmg)
                    + " HP."
                )
            if (
                lowest_defense_obj is not None
                and highest_attack_obj.attack < lowest_defense_obj.defense
            ):
                dmg = lowest_defense_obj.defense - highest_attack_obj.attack
                self.bot_life = int(self.bot_life) - int(dmg)
                self.bot_field.remove(highest_attack_obj)
                self.botGamesStatus()
                self.gui.append_text(
                    highest_attack_obj.name
                    + " attacked "
                    + lowest_defense_obj.name
                    + ". Your opponent lost "
                    + str(dmg)
                    + " HP."
                )
            if (
                lowest_defense_obj is not None
                and highest_attack_obj.attack == lowest_defense_obj.defense
            ):
                self.bot_field.remove(highest_attack_obj)
                self.player_field.remove(lowest_defense_obj)
                self.botGamesStatus()
                self.gui.append_text(
                    highest_attack_obj.name
                    + " attacked "
                    + lowest_defense_obj.name
                    + ". Attack unsuccessful, both monsters have fainted."
                )
                self.player_life = int(self.player_life) - 1000
                self.bot_life = int(self.bot_life) - 1000
        else:
            self.player_life = int(self.player_life) - int(highest_attack_obj.attack)
            self.gui.append_text(
                highest_attack_obj.name
                + " attacked you directly, you have lost "
                + str(highest_attack_obj.attack)
                + " HP."
            )

    def playerDeath(self):
        if self.player_life <= 0:
            self.clear_screen()
            print("Your opponent has won!")

    def botDeath(self):
        if self.bot_life <= 0:
            self.clear_screen()
            print("You won!")

    def info(self):
        self.clear_screen()
        print("Your hand:")
        for card in self.player_hand:
            print(f"{card.name}, Attack: {card.attack}, Speed: {card.speed}")
            print("Your field:")
        for card in self.player_field:
            print(f"{card.name}, Attack: {card.attack}, Speed: {card.speed}")
            print("Bots field:")
        for card in self.bot_field:
            print(f"{card.name}, Attack: {card.attack}, Speed: {card.speed}")

    def set_game_state(self, state):
        self.game_state = state

    def end_my_turn(self):
        self.is_my_turn = False
        self.my_turn_count += 1
        self.start_opponent_turn()

    def end_opponent_turn(self):
        self.is_my_turn = True
        self.opponent_turn_count += 1
        self.gui.append_text("Your turn!")

    def start_my_turn(self, action):
        self.playerDeath()
        self.botDeath()
        if action == "attack":
            self.playerAttack()
        elif action == "draw":
            self.playerDraw()
        elif action == "place":
            self.playerPlace()
        elif action == "gamble":
            self.playerGamble()

        self.is_my_turn = False
        self.my_turn_count += 1

    def start_opponent_turn(self):
        self.playerDeath()
        self.botDeath()
        if self.opponent_turn_count < 1:
            self.botPlace()
            self.opponent_turn_count += 1
        else:
            random_number = random.randint(1, 100)
            if random_number <= 20:
                if len(self.bot_deck) >= 1:
                    self.botDraw()
                if len(self.bot_deck) == 0:
                    pass
            if random_number >= 21 and random_number <= 40:
                self.botGamble()
            if random_number >= 41 and random_number <= 70:
                if len(self.bot_field) >= 1:
                    self.botAttack()
                if len(self.bot_field) == 0:
                    pass
            if random_number >= 71 and random_number <= 100:
                if len(self.bot_hand) >= 1:
                    self.botPlace()
                if len(self.bot_hand) == 0:
                    pass
        self.end_opponent_turn()

    def startGame(self):
        self.game_state = "game_running"
        self.clear_screen()  # PHASE ONE
        self.is_my_turn = self.average_player_speed > self.average_bot_speed
        return self.is_my_turn
