# Plant: A Plant in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.galapagos.game_object import GameObject



class Plant(GameObject):
    """The class representing the Plant in the Galapagos game.

    A Plant in the game.
    """

    def __init__(self):
        """Initializes a Plant with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._growth_rate = 0
        self._size = 0
        self._tile = None
        self._turns_until_growth = 0

    @property
    def growth_rate(self) -> int:
        """int: The total number of turns it takes this plant to grow in size.
        """
        return self._growth_rate

    @property
    def size(self) -> int:
        """int: The size of the plant.
        """
        return self._size

    @property
    def tile(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile this Plant occupies.
        """
        return self._tile

    @property
    def turns_until_growth(self) -> int:
        """int: The number of turns left until this plant will grow again.
        """
        return self._turns_until_growth
