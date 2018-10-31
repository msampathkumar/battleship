##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import battleArea


class Player(object):
    """This is Player class. It sets up a player."""

    def __init__(self, battle_area=battleArea.BattleArea(),
                 moves=[], player_name='Player'):
        """Constructor for player.

        Arguments:
          battle_area (battleArea.BattleArea()): battle area to be assigned to
            current player.
          moves (list): list of moves / missiles target.
          player_name (str): name of the player.
        """
        self._battle_area = battle_area
        self._ships = set()
        self._moves = moves
        self._no_of_moves = len(moves)
        self._player_name = player_name
        self._missiles_over = False

    def set_name(self, player_name):
        """Set player name."""
        self._player_name = player_name

    def get_name(self):
        """Get player name."""
        return self._player_name

    def get_battle_area(self):
        """Get Battle Area."""
        return self._battle_area

    def add_ship(self, new_ship):
        """Add ship count."""
        import ship
        if (isinstance(new_ship, ship.Ship) and
            self._battle_area == new_ship._battle_area):
            self._ships.add(new_ship)

    def get_ships(self):
        """Return ships."""
        return self._ships

    def set_moves(self, moves):
        """Set player moves / missiles target."""
        self._moves = moves
        self._no_of_moves = len(moves)

    def __iter__(self):
        """Return iterator."""
        return self

    def next(self):
        """Return next element of the iterator."""
        if self._no_of_moves > 0:
            self._no_of_moves -= 1
            return self._moves[len(self._moves) - self._no_of_moves - 1]
        raise StopIteration

    def set_missiles_over(self):
        """Set moves/missles over flag value."""
        self._missiles_over = True

    def get_missiles_over(self):
        """Get moves/missles over flag value."""
        return self._missiles_over

    def attacked_at(self, position):
        """Implements change if player is attacked.

        Arguments:
          position (str): position at which player is attacked.
        Returns:
          (bool or None): True if attack hits ship and destroyes it else None.
        """
        ship = self._battle_area.get_cell(position)
        if ship:
            isHit = ship.hit(position)
            if isHit:
                return True

    def attacks_on(self, position, player):
        """Implements player attack on opponent and print status.

        Arguments:
          position (str): Position at which player is attacked.
          player (Player()): Instance of player being attacked.
        Returns:
          (bool): True if attack hits ship else False.
        """
        message = '{0} fires a missile with target {1} which got '.format(
            self._player_name, position)
        if player.attacked_at(position):
            print message + 'hit'
            return True
        else:
            print message + 'miss'
            return False

    def is_defeated(self):
        """Returns player defeated status."""
        for ship in self._ships:
            if ship.is_destroyed() is None:
                return False
        return True
