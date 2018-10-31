##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


class Coordinate(object):
    """This is Coordinate class. It sets up a coordinate."""

    def __init__(self, x, y):
        """Coordinate constructor."""
        self._x = x
        self._y = y

    def set_x(self, x):
        """set x coordinate."""
        self._x = x

    def get_x(self):
        """Returns y coordinate."""
        return self._x

    def set_y(self, y):
        """set y coordinate."""
        self._x = y

    def get_y(self):
        """Returns y coordinate."""
        return self._y

    def get_position(self):
        """Returns position."""
        return self._y + str(self._x)

class AreaCreator(object):

    def __init__(self, width=1, height='A', starts_at='A1',
                 is_battle_area=True):
        """Area constuctor.

        Arguments:
          width (int): width of the battle area.
          height (str, int): height of the battle area.
          starts_at (str): position (cell_name) in case of ship.
          is_battle_area (bool): True if area created for battle ground else
            False.
        """
        self._is_battle_area = is_battle_area
        self._x_coordinates = []
        self._y_coordinates = []
        self._width = width
        self._height = height
        self._starts_at = starts_at
        self._coordinates = []
        self.setup()

    def _set_width(self):
        """Set width coordinates."""
        if self._is_battle_area:
            self._x_coordinates = range(1, self._width + 1)
        else:
            starts_at = int(self._starts_at[1])
            self._x_coordinates = range(
                starts_at, (starts_at + self._width))

    def _set_height(self):
        """Set height coordinates."""
        if self._is_battle_area:
            self._y_coordinates = [chr(x) for x in range(
                65, ord(self._height) + 1)]
        else:
            starts_at = ord(self._starts_at[0])
            self._y_coordinates = map(
                chr, range(starts_at, (starts_at + self._height)))

    def _fix_coordinates(self):
        """Fix coordinates to area."""
        for yCoordinate in self._y_coordinates:
            for xCoordinate in self._x_coordinates:
                self._coordinates.append(
                    Coordinate(xCoordinate, yCoordinate))

    def setup(self):
        """Setup for area."""
        self._set_width()
        self._set_height()
        self._fix_coordinates()

    def get_coordinates(self):
        """Get all area coordiantes."""
        return self._coordinates
