# This is a variant of the Tic Tac Toe recipe given in the easyAI library

from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player
from easyAI.AI.TT import *
from easyAI.AI.DictTT import *


class GameController(TwoPlayersGame):
    def __init__(self, players):
        # Define the players
        self.players = players

        # Define who starts the game
        self.nplayer = 1

        # Define the board
        self.board = [0] * 9

    # Define possible moves
    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]

    # Make a move
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    # Does the opponent have three in a line?
    def loss_condition(self):
        possible_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                                 [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        return any([all([(self.board[i - 1] == self.nopponent)
                         for i in combination]) for combination in possible_combinations])

    # Check if the game is over
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    # Show current position
    def show(self):
        print('\n' + '\n'.join([' '.join([['.', 'O', 'X'][self.board[3 * j + i]]
                                          for i in range(3)]) for j in range(3)]))
        if self.is_over():
            if self.loss_condition():
                print(f"\nPlayer {self.nopponent} wins!")
            else:
                print("\nIt's a draw!")

    # Compute the score
    def scoring(self):
        return -100 if self.loss_condition() else 0

    def ttentry(self):
        return "".join([".0X"[i] for i in self.board])


if __name__ == "__main__":
    # Define the algorithm
    use_tt = True
    two_ai = False
    handicap = 0
    am = 11

    if use_tt:
        print("practice game for preparing table.")
        table = TT()
        ai1 = Negamax(am)  # boosted Negamax !
        ai2 = Negamax(am, tt=table)  # boosted Negamax !
        if two_ai:
            GameController([AI_Player(ai1, name="AI 1"), AI_Player(ai2, name="AI 2")]).play()
        else:
            GameController([Human_Player(name="Human"), AI_Player(ai2, name="AI")]).play()

        print("Done.")

        # TT used negamax
        algorithm2 = Negamax(am, tt=table)
        t = 1 if am - handicap < 1 else am - handicap
        algorithm = Negamax(t)

    else:
        # plain negamax
        algorithm2 = Negamax(am)
        t = 1 if am - handicap < 1 else am - handicap
        algorithm = Negamax(t)

    # Start the game
    if two_ai:
        GameController([AI_Player(algorithm, name="AI 1"), AI_Player(algorithm2, name="AI 2")]).play()
    else:
        GameController([Human_Player(name="Human"), AI_Player(algorithm2, name="AI")]).play() 