##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import unittest

import utils


class TestCoordinate(unittest.TestCase):

    def test_get_position(self):
        coordinate = utils.Coordinate(1, 'D')
        self.assertEqual(coordinate.get_position(), 'D1')


class TestAreaCreator(unittest.TestCase):

    def test_setup_battle_area(self):
        area = utils.AreaCreator(3, 'B')
        self.assertEqual(len(area.get_coordinates()), 6)

    def test_setup_battle_area_cell_names(self):
        area = utils.AreaCreator(3, 'B')
        coordinates = [c.get_position() for c in area.get_coordinates()]
        self.assertEqual(len(coordinates), 6)
        self.assertEqual(coordinates, ['A1', 'A2', 'A3',
                                       'B1', 'B2', 'B3'])

    def test_setup_ship_area(self):
        area = utils.AreaCreator(3, 3, 'C2', False)
        self.assertEqual(len(area.get_coordinates()), 9)

    def test_setup_ship_area_cell_names(self):
        area = utils.AreaCreator(3, 3, 'C2', False)
        coordinates = [c.get_position() for c in area.get_coordinates()]
        self.assertEqual(len(coordinates), 9)
        self.assertEqual(coordinates, ['C2', 'C3', 'C4',
                                       'D2', 'D3', 'D4',
                                       'E2', 'E3', 'E4'])
