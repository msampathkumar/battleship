from setuptools import setup

setup(
    name='game',
    version='0.0.1',
    author='Pawan Singh Pal',
    author_email='pawansingh126@gmail.com',
    packages=['game'],
    url='https://github.com/pawansingh126/battleship',
    description='Creates a mini Battlezone Game.',
    license='Apache 2.0',
    long_description="""
    This module lets you create and play a battleship game:
      - There are two players in the game.
      - Players have their own battle area with similar dimentions, each
        coordinate typically refferred as a cell.
      - Players have same number of ships with similar dimentions which are
        places on their respective battle area.
      - Ships can be of two types, P(weak) and Q(strong).
      - P type Ship takes a sigle hit on its cell to get cell destroyed
        whereas Q takes 2.
      - Players have moves which target a certain cell of a battle area ().
      - Player 1 starts the game, and they alternatively takes turn.
      - if attaking players' move hits the other player, attacker
        gets another chance to make a move.
      - As soon as all the ships with other player gets destroyed, attacker
        wins.
      - If both players exhausts their moves and none gets destroyed, then
        they call Peace.
    """,
    entry_points={
        'console_scripts': [
            'game=game.game:main',
        ]
    }
)