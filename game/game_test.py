##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import unittest

import game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = game.Game(5, 'E')
        self.p1 = self.game.get_player_1()
        self.p2 = self.game.get_player_2()
        self.game.add_ship(self.p1, 1, 1, 'B2', 'Q')
        self.game.add_ship(self.p2, 1, 1, 'E4', 'Q')
        self.game.set_moves(self.p1, ['B1', 'B2'])
        self.game.set_moves(self.p2, ['D3', 'B2'])

    def test_add_ship(self):
        total_ships = len(self.p1.get_ships())
        self.game.add_ship(self.p1, 2, 2, 'D4', 'P')
        self.assertEqual(len(self.p1.get_ships()), total_ships + 1)

        total_ships = len(self.p2.get_ships())
        self.game.add_ship(self.p2, 2, 2, 'B4', 'P')
        self.assertEqual(len(self.p2.get_ships()), total_ships + 1)

    def test_set_moves(self):
        moves = ['B1', 'B2', 'B3']
        self.game.set_moves(self.p1, moves)
        i = 0
        for move in self.p1:
            self.assertEqual(move, moves[i])
            i += 1
        self.game.set_moves(self.p2, moves)
        i = 0
        for move in self.p2:
            self.assertEqual(move, moves[i])
            i += 1
