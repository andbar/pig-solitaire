import random

class Dice:

    def __init__(self):
        self.possible_rolls = [1, 2, 3, 4, 5, 6]

    def roll_result(self):
        result = random.choice(self.possible_rolls)
        return result

dice = Dice()


class Player:

    def __init__(self):
        self.current_score = 0
        self.dice = dice

    def player_continue(self):
        if input("Roll or hold? Enter 'r' or 'h' ") == "r":
            return True
        else:
            return False

    def player_roll(self):
        return dice.roll_result()


    def player_turn(self):
        turn_score = 0
        player_will_roll = True
        count = 0
        while player_will_roll == True:
            if count == 0:
                input("Your turn. Press any button to roll. ")
                roll_result = self.player_roll()
                if roll_result == 1:
                    turn_score = 0
                    print("Sorry, you rolled a 1. You get 0 points this turn.")
                    player_will_roll = False
                    count = 1
                else:
                    turn_score += roll_result
                    print("You rolled a {}.".format(roll_result))
                    print("You currently have {} points this turn.".format(turn_score))
                    count = 1
            else:
                if self.player_continue() == True:
                    roll_result = self.player_roll()
                    if roll_result == 1:
                        turn_score = 0
                        print("Sorry, you rolled a 1. You get 0 points this turn.")
                        player_will_roll = False
                    else:
                        turn_score += roll_result
                        print("You rolled a {}.".format(roll_result))
                        print("You currently have {} points this turn.".format(turn_score))
                else:
                    print("You added {} points to your score this turn.".format(turn_score))
                    player_will_roll = False
        return turn_score

player = Player()


class AI:

    def __init__(self):
        self.current_score = 0
        self.dice = dice

    def ai_continue(self):
        cont = random.randint(0,1)
        if cont == 1:
            return True
        else:
            return False

    def ai_roll(self):
        return dice.roll_result()

    def ai_turn(self):
        turn_score = 0
        ai_will_roll = True
        count = 0
        while ai_will_roll == True:
            if count == 0:
                roll_result = self.ai_roll()
                if roll_result == 1:
                    turn_score = 0
                    print("Oh, no! I've rolled a 1. I get 0 points this turn.")
                    ai_will_roll = False
                    count = 1
                else:
                    turn_score += roll_result
                    print("I rolled a {}.".format(roll_result))
                    print("I currently have {} points this turn.".format(turn_score))
                    count = 1
            else:
                if self.ai_continue() == True:
                    roll_result = self.ai_roll()
                    if roll_result == 1:
                        turn_score = 0
                        print("Oh, no! I've rolled a 1. I get 0 points this turn.")
                        ai_will_roll = False
                    else:
                        turn_score += roll_result
                        print("I rolled a {}.".format(roll_result))
                        print("I currently have {} points this turn.".format(turn_score))
                else:
                    print("I added {} points to my score this turn.".format(turn_score))
                    ai_will_roll = False
        return turn_score

ai = AI()


class Game:
    pass
