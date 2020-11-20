# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.galapagos.game_object import GameObject



class Tile(GameObject):
    """The class representing the Tile in the Galapagos game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._creature = None
        self._egg = None
        self._plant = None
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._x = 0
        self._y = 0

    @property
    def creature(self) -> Optional['games.galapagos.creature.Creature']:
        """games.galapagos.creature.Creature or None: The Creature on this Tile or None.
        """
        return self._creature

    @property
    def egg(self) -> Optional['games.galapagos.creature.Creature']:
        """games.galapagos.creature.Creature or None: The unhatched Creature on this Tile or None.
        """
        return self._egg

    @property
    def plant(self) -> Optional['games.galapagos.plant.Plant']:
        """games.galapagos.plant.Plant or None: The Plant on this Tile or None.
        """
        return self._plant

    @property
    def tile_east(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.
        """
        return self._tile_west

    @property
    def x(self) -> int:
        """int: The x (horizontal) position of this Tile.
        """
        return self._x

    @property
    def y(self) -> int:
        """int: The y (vertical) position of this Tile.
        """
        return self._y

    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self) -> List['games.galapagos.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.galapagos.tile.Tile]: The list of neighboring Tiles of this Tile.
        """
        neighbors = []

        for direction in Tile.directions:
            neighbor = getattr(self, "tile_" + direction.lower())
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

    def is_pathable(self) -> bool:
        """Checks if a Tile is pathable to units

        Returns:
            bool: True if pathable, False otherwise.
        """
        return not self.creature and not self.plant

    def has_neighbor(self, tile: 'games.galapagos.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.galapagos.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())
