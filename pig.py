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
        roll_result = dice.roll_result()
        return roll_result

    def player_turn(self):
        turn_score = 0
        player_will_roll = True
        while player_will_roll == True:
            if self.player_continue() == True:
                if self.player_roll() == 1:
                    turn_score = 0
                    player_will_roll = False
                else:
                    turn_score += self.player_roll()
            else:
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
        roll_result = dice.roll_result()
        return roll_result

    def ai_turn(self):
        turn_score = 0
        ai_will_roll = True
        while ai_will_roll == True:
            if self.ai_continue() == True:
                if self.ai_roll() == 1:
                    turn_score = 0
                    ai_will_roll = False
                else:
                    turn_score += self.ai_roll()
            else:
                ai_will_roll = False
        return turn_score

ai = AI()
