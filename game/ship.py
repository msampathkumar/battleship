##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import abc

import player
import utils
import validations


class ShipCell(object):
    """This is abstract ShipCell class."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, cell_name):
        """Cell constuctor.

        Arguments:
          cell_name (str): position (cell_name) in case of ship.
          is_battle_area (bool): True if area created for battle ground else
            False.
        """
        self._cell_name = cell_name
        self._power = 0
        super(ShipCell, self).__init__()

    def set_name(self, _name):
        """Set cell name."""
        self._cell_name = _name

    def get_name(self):
        """Get cell name."""
        return self._cell_name

    def get_power(self):
        """Get cell name."""
        return self._power

    def hit(self):
        """Implements a hit to the cell.

        Returns:
          (bool): True if cell was still alive.
        """
        if self._power == 0 :
            return False
        self._power -= 1
        return True

    def is_destroyed(self):
        """Returns if cell still has any power(alive)."""
        if self._power == 0:
            return True
        return False


class PShipCell(ShipCell):
    """This is abstract PShipCell class for P type cells."""

    def __init__(self, cell_name):
        """Constructor."""
        super(PShipCell, self).__init__(cell_name)
        self._power = 1


class QShipCell(ShipCell):
    """This is abstract QShipCell class for P type cells."""

    def __init__(self, cell_name):
        """Constructor."""
        super(QShipCell, self).__init__(cell_name)
        self._power = 2


class Ship(object):
    """This is abstract Ship class."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, width=1, height=1, starts_at='A1',
                 for_player=player.Player()):
        """Ship constuctor.

        Arguments:
          width (int): width of the battle area.
          height (str, int): height of the battle area.
          starts_at (str): position (cell_name) in case of ship.
          battle_area (battleArea.BattleArea()): Instance of BattleArea.
        """
        self._width = width
        self._height = height
        self._cells = list()
        self._starts_at = starts_at
        self._battle_area = for_player.get_battle_area()
        self._power = 0
        if self.check_movability() is False:
            raise 'Error: Cannot add ship as area already occupies.'
        for_player.add_ship(self)
        super(Ship, self).__init__()

    @abc.abstractmethod
    def create_position(self):
        """Creates position of ship and adds mappings to battle_area."""
        raise NotImplementedError


    def _update_battle_position(self, new_cells=[], previous_cells=[]):
        """Update position of ship on the """
        if previous_cells:
            for previous_cell in previous_cells:
                self._battle_area.set_cell(previous_cell.get_name(), False)
        if new_cells:
            for new_cell in new_cells:
                self._battle_area.set_cell(new_cell.get_name(), self)

    def get_cell_by_name(self, cell_name):
        """Returns cell by its name."""
        for cell in self._cells:
            if cell.get_name() == cell_name:
                return cell

    def is_destroyed(self):
        """Returns if ship still has any power(alive)."""
        if self._power == 0:
            return True

    def check_movability(self):
        return validations.Validations().validate_area_availability(
            self._width, self._height, self._starts_at, self._battle_area)

    def hit(self, cell_name):
        """Implements a hit to the ship.

        Arguments:
          cell_name (str): name of the target cell which was hit.
        Returns:
          (bool): True if ship was still alive.
        """
        cell = self.get_cell_by_name(cell_name)
        if cell.get_power():
            cell.hit()
            self._power -= 1
            return True


class PShip(Ship):

    def __init__(self, width=1, height=1, starts_at='A1',
                 for_player=player.Player()):
        """PShip constuctor.

        Arguments:
          width (int): width of the battle area.
          height (str, int): height of the battle area.
          starts_at (str): position (cell_name) in case of ship.
          battle_area (battleArea.BattleArea()): Instance of BattleArea.
        """
        super(PShip, self).__init__(width, height, starts_at, for_player)
        self._power = self._width * self._height * 1
        self.create_position()

    def create_position(self):
        """Creates position of ship and adds mappings to battle_area."""
        area = utils.AreaCreator(
            self._width, self._height, starts_at=self._starts_at,
            is_battle_area=False)
        for coordinate in area.get_coordinates():
            position = coordinate.get_position()
            self._cells.append(PShipCell(position))
        self._update_battle_position(self._cells)


class QShip(Ship):

    def __init__(self, width=1, height=1, starts_at='A1',
                 for_player=player.Player()):
        """QShip constuctor.

        Arguments:
          width (int): width of the battle area.
          height (str, int): height of the battle area.
          starts_at (str): position (cell_name) in case of ship.
          battle_area (battleArea.BattleArea()): Instance of BattleArea.
        """
        super(QShip, self).__init__(width, height, starts_at, for_player)
        self._power = self._width * self._height * 2
        self.create_position()

    def create_position(self):
        """Creates position of ship and adds mappings to battle_area."""
        area = utils.AreaCreator(
            self._width, self._height, starts_at=self._starts_at,
            is_battle_area=False)
        for coordinate in area.get_coordinates():
            position = coordinate.get_position()
            self._cells.append(QShipCell(position))
        self._update_battle_position(self._cells)
