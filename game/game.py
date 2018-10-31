##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import copy
import os
import sys

import battleArea
import player
import ship
import validations


class Game(object):
    """This is Game class. It sets up a game."""

    def __init__(self, width=5, height='E'):
        """Constructor for Game.

        Arguments:
          width (int): width of the battle area.
          height (str): height of thr battl area.
        """
        self.validate = validations.Validations()
        try:
            assert (self.validate.validate_battle_area_width(width) and
                    self.validate.validate_battle_area_height(height))
        except AssertionError:
            print "Error: Dimensions required -  with[0-9] and height[A-Z]."
            raise AssertionError
        area = battleArea.BattleArea(width, height)
        self._player_1 = player.Player(area, player_name='Player-1')
        battleArea2 = copy.deepcopy(area)
        self._player_2 = player.Player(battleArea2, player_name='Player-2')

    def get_player_1(self):
        """Returns player 1."""
        return self._player_1

    def get_player_2(self):
        """Returns player 1."""
        return self._player_2

    def add_ship(self, for_player, width=1, height=1, starts_at='A1',
                ship_type='P'):
        """Add a ship to a players battle area.

        Arguments:
          for_player (player.Player()): player for which ship is being added.
          width (int): width of the ship.
          height (int): height of the ship.
          starts_at (str): starting cell of the ship.
          ship_type (str): type of the ship.
        """
        try:
            assert self.validate.validate_ship_position(
                for_player.get_battle_area().get_width(),
                for_player.get_battle_area().get_height(),
                width, height, starts_at)
            if isinstance(for_player, player.Player):
                if ship_type == 'P':
                    ship.PShip(width, height, starts_at, for_player)
                if ship_type == 'Q':
                    ship.QShip(width, height, starts_at, for_player)
        except AssertionError:
            print """Error: Ship could not be added from the given
                starting point."""

    def set_moves(self, for_player, moves=[]):
        """Set moves of a players.

        Arguments:
          for_player (player.Player()): player for which ship is being added.
          moves (list): moves / missiles target list.
        """
        try:
            assert self.validate.validate_moves(
                moves, for_player.get_battle_area())
            if isinstance(for_player, player.Player):
                for_player.set_moves(moves)
        except AssertionError:
            print """Error: There are some out of battle area moves."""

    def fire(self, move_iterator, attaker_player, attacked_player):
        """Implements missile fire from a player to another.

        Arguments:
          move_iterator (iter(player.Player())): Iterator for player attacks.
          attaker_player (player.Player()): attacking player.
          attacked_player (player.Player()): player being attacked.
        Returns:
          (bool): True if the attacked player loses.
        """
        no_missile_message = '{0} has no more missiles left to launch'
        if attacked_player.get_missiles_over():
            print no_missile_message.format(attaker_player.get_name())
            return
        try:
            move = move_iterator.next()
            if attaker_player.attacks_on(move, attacked_player):
                self.fire(move_iterator, attaker_player, attacked_player)
        except StopIteration:
            attacked_player.set_missiles_over()
            if attacked_player.is_defeated():
                print '{0} won the battle'.format(attaker_player.get_name())
                return True

    def start(self):
        """Starts the game."""
        moves_player1 = iter(self._player_1)
        moves_player2 = iter(self._player_2)
        while True:
            if self.fire(moves_player1, self._player_1, self._player_2):
                break
            if self._player_2.is_defeated():
                print '{0} won the battle'.format(self._player_1.get_name())
                break
            if self.fire(moves_player2, self._player_2, self._player_1):
                break
            if self._player_1.is_defeated():
                print '{0} won the battle'.format(self._player_2.get_name())
                break
            if (self.get_player_1().get_missiles_over() and
                self.get_player_2().get_missiles_over()):
                print '{0} and {1} are at peace.'.format(
                    self._player_1.get_name(), self._player_2.get_name())
                break

def main():
    if len(sys.argv) < 2:
        print """Please provice file path with name
            e.g. python game.py file.txt
        """
        exit(0)
    else:
        file_name = sys.argv[1]
        if os.path.isfile(file_name) is False:
            file_name = os.getcwd() + '/' + file_name
    try:
        with open(file_name, "rb") as fb:
            lines = map(lambda x: x.strip(), fb.readlines())
            i, j = 1, 1
            game = None
            print 'Input:'
            for line in lines:
                print line
                if i == 1:
                    width, height = line.split()
                    game = Game(int(width), height)
                elif i == 2:
                    j = int(line)
                elif i-2 <= j:
                    ship_type, width, height, start_p1, start_p2 = line.split()
                    game.add_ship(game.get_player_1(), int(width), int(height),
                                starts_at=start_p1, ship_type=ship_type)
                    game.add_ship(game.get_player_2(), int(width), int(height),
                                starts_at=start_p2, ship_type=ship_type)
                elif i == j+3:
                    moves = line.split()
                    game.set_moves(game.get_player_1(), moves)
                elif i == j+4:
                    moves = line.split()
                    game.set_moves(game.get_player_2(), moves)
                i += 1
            print '\n\nOutupt:'
            if game:
                game.start()
    except Exception as e:
        print e

if __name__ == "__main__":
    """This is the script entrypoint. It reads a input file in current
    directory and sets up game based on inputs.
    """
    main()
