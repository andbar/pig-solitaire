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
        player_response = input("Roll or hold? Enter 'r' or 'h' ")
        if player_response.lower() == 'r':
            return True
        elif player_response.lower() == 'h':
            return False
        else:
            print("That's not an 'r' or an 'h'. Please try again.")
            self.player_continue()

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
                    print("Oh, no! You rolled a 1. You get 0 points this turn.")
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
                        print("Oh, no! You rolled a 1. You get 0 points this turn.")
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
                    print("Oh, no! Player 2 rolled a 1. Player 2 gets 0 points this turn.")
                    ai_will_roll = False
                    count = 1
                else:
                    turn_score += roll_result
                    print("Player 2 rolled a {}.".format(roll_result))
                    print("Player 2 currently has {} points this turn.".format(turn_score))
                    count = 1
            else:
                if self.ai_continue() == True:
                    roll_result = self.ai_roll()
                    if roll_result == 1:
                        turn_score = 0
                        print("Oh, no! Player 2 rolled a 1. Player 2 gets 0 points this turn.")
                        ai_will_roll = False
                    else:
                        turn_score += roll_result
                        print("Player 2 rolled a {}.".format(roll_result))
                        print("Player 2 currently has {} points this turn.".format(turn_score))
                else:
                    print("Player 2 added {} points to their score this turn.".format(turn_score))
                    ai_will_roll = False
        return turn_score


ai = AI()


class Game:

    def __init__(self, player1=player, player2=ai, rounds=7):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds


    def update_player_scores(self, round_scores): #tracks the current score of players
        player.current_score += round_scores[0]
        ai.current_score += round_scores[1]

    def game_round(self): #plays a round and returns score for each player
        player1_round_score = player.player_turn()
        player2_round_score = ai.ai_turn()
        round_scores = [player1_round_score, player2_round_score]
        return round_scores

    def game_play(self):
        print("Welcome to The Game of Pig\n")
        print("You will take turns with another player, rolling a dice to accumulate points.")
        print("While it is your turn, you may roll as many times as you'd like to collect points on that turn.")
        print("However, if you roll a 1, you lose all points from that current turn and your turn is over.")
        print("To keep the points collected on your turn, choose hold rather than rolling again "
              "and the current points will be added to your total.")
        print("Each player will have {} turns. You get to go first. Let's get started!".format(self.rounds))
        current_round = 1
        while current_round <= self.rounds:
            print("\nStarting Turn {} of {}".format(current_round, self.rounds))
            print("Current total points: You - {}  Player 2 - {}\n".format(player.current_score, ai.current_score))
            round_scores = self.game_round()
            self.update_player_scores(round_scores)
            current_round += 1
        final_score = [player.current_score, ai.current_score]
        if player.current_score > ai.current_score:
            print("\nCongratulations! You won, {} to {}.".format(player.current_score, ai.current_score))
        elif player.current_score < ai.current_score:
            print("\nBummer, you lost, {} to {}.".format(player.current_score, ai.current_score))
        elif player.current_score == ai.current_score:
            print("\nLooks like a tie! {} to {}.".format(player.current_score, ai.current_score))


game = Game()

#game.game_play()
