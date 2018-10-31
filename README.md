# Info

This module contains a simple Battle Ship game, which can be described as folows:
- There are two players in the game.
- Players have their own battle area with similar dimentions, each coordinate typically refferred as a cell.
- Players have same number of ships with similar dimentions which are places on their respective battle area.
- Ships can be of two types, P(weak) and Q(strong).
- P type Ship takes a sigle hit on its cell to get cell destroyed whereas Q takes 2.
- Players have moves which target a certain cell of a battle area ().
- Player 1 starts the game, and they alternatively takes turn.
- if attaking players' move hits the other player, attacker
    gets another chance to make a move.
- As soon as all the ships with other player gets destroyed, attacker wins.
- If both players exhausts their moves and none gets destroyed, then they call Peace.

# Installation
```
make install
# or
pip install .
```

# Usage
```
game test.txt
```

# Run unitests
```
make unittests
```

# Create a new Game with Python interpreter
```
import game
g = game.Game()

# Get Player 1 and 2
p1 = g.get_player_1()
p2 = g.get_player_2()

# add a new Q type ship for p1 and p2
g.add_ship(p1, width=1, height=2, starts_at='B2', ship_type='Q')
g.add_ship(p2, width=1, height=2, starts_at='C1', ship_type='Q')

# add moves for each player
g.add_moves(p1, ['C1', 'B1', 'C1', 'C2', 'D1', 'E1'])
g.add_moves(p2, ['C1', 'B1', 'B1', 'B2', 'B3', 'D1'])

# start the game
g.start()

```

# Contributors

@pawansingh126
