##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import utils


class Validations(object):
    """This is Validation class. It defines all the validation methods."""

    def validate_battle_area_width(self, width):
        """Validate width of battle area.

        Arguments:
          width (int): width of battle area.
        """
        if width >= 1 and width <= 9:
            return True
        return False

    def validate_battle_area_height(self, height):
        """Validate height of battle area.

        Arguments:
          height (str): height of battle area.
        """
        if len(height) == 1 and ord(height) >= 65 and ord(height) <= 90:
            return True
        return False

    def validate_ship_position(self, area_width, area_height, width, height,
                              starts_at):
        """Validate posion of ship on battle area.

        Arguments:
          area_width (int): width of battle area.
          area_height (str): height of battle area.
          width (int): width of ship.
          height (int): height of ship.
          starts_at (str): stsrting position of ship.
        """
        if (int(starts_at[1]) + width - 1) <= area_width and (
            ord(starts_at[0]) + height - 1) <= ord(area_height):
            return True
        return False

    def validate_area_availability(self, width, height, starts_at,
                                   battle_area):
        area = utils.AreaCreator(width, height, starts_at,
                                 is_battle_area=False)
        for coordinate in area.get_coordinates():
            cell = battle_area.get_cell(coordinate.get_position())
            if cell or cell is None :
                return False
        return True

    def validate_moves(self, moves, battle_area):
        """Validate posion of ship on battle area.

        Arguments:
          moves (list): list of moves / missiles target.
          battle_area (battleArea.BattleArea()): battle are on which taget
            position are marked.
        """
        for move in moves:
            if battle_area.get_cell(move) is None:
                return False
        return True
