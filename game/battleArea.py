##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import utils


class BattleArea(object):
    """This is BattleArea class. It sets up a battle area."""

    def __init__(self, width=1, height='A'):
        """Constructor for Battle Area.

        Arguments:
          width (int): width of the battle area.
          height (str): height of the battle area.
        """
        self._width = width
        self._height = height
        self._cells = {}
        self.create_area()

    def get_width(self):
        """Returns battle area width."""
        return self._width

    def get_height(self):
        """Returns battle area height."""
        return self._height

    def create_area(self):
        """Creates all the cells for battle area."""
        area = utils.AreaCreator(self._width, self._height)
        for coordinate in area.get_coordinates():
            position = coordinate.get_position()
            self._cells[position] = False

    def set_cell(self, cell_name, ship):
        """Set ship on a cell.

        Arguments:
          cell_name (str): cell at which ship needs to be placed.
          ship (ship.Ship()): instance of ship which needs to be places.
        """
        if self.get_cell(cell_name) is not None:
            self._cells[cell_name] = ship

    def get_cell(self, cell_name):
        """Returns ship at a cell."""
        return self._cells.get(cell_name, None)

    def get_cells(self):
        """Returns cells dict. """
        return self._cells
