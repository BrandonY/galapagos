# Creature: A Creature in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.galapagos.game_object import GameObject



class Creature(GameObject):
    """The class representing the Creature in the Galapagos game.

    A Creature in the game.
    """

    def __init__(self):
        """Initializes a Creature with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._can_bite = False
        self._can_breed = False
        self._carnivorism = 0
        self._current_health = 0
        self._defense = 0
        self._endurance = 0
        self._herbivorism = 0
        self._is_egg = False
        self._max_health = 0
        self._movement_left = 0
        self._owner = None
        self._parents = []
        self._speed = 0
        self._tile = None

    @property
    def can_bite(self) -> bool:
        """bool: Indicates whether or not this creature can bite this turn.
        """
        return self._can_bite

    @property
    def can_breed(self) -> bool:
        """bool: Indicates whether or not this creature can breed this turn.
        """
        return self._can_breed

    @property
    def carnivorism(self) -> int:
        """int: The carnivore level of the creature. This increases damage to other other creatures and health restored on kill.
        """
        return self._carnivorism

    @property
    def current_health(self) -> int:
        """int: The current amount of health that this creature has.
        """
        return self._current_health

    @property
    def defense(self) -> int:
        """int: The defense of the creature. This reduces the amount of damage this creature takes from being eaten.
        """
        return self._defense

    @property
    def endurance(self) -> int:
        """int: The endurance level of the creature. This increases the max health a creature can have.
        """
        return self._endurance

    @property
    def herbivorism(self) -> int:
        """int: The herbivore level of the creature. This increases health restored from eating plants.
        """
        return self._herbivorism

    @property
    def is_egg(self) -> bool:
        """bool: Indicates whether or not this creature is still in an egg and cannot bite, breed, or be bitten.
        """
        return self._is_egg

    @property
    def max_health(self) -> int:
        """int: The maximum amount of health this creature can have.
        """
        return self._max_health

    @property
    def movement_left(self) -> int:
        """int: The amount of moves this creature has left this turn.
        """
        return self._movement_left

    @property
    def owner(self) -> Optional['games.galapagos.player.Player']:
        """games.galapagos.player.Player or None: The owner of the creature.
        """
        return self._owner

    @property
    def parents(self) -> List['games.galapagos.creature.Creature']:
        """list[games.galapagos.creature.Creature]: The creatures that gave birth to this one.
        """
        return self._parents

    @property
    def speed(self) -> int:
        """int: The speed of the creature. This determines how many times a creature can move in one turn.
        """
        return self._speed

    @property
    def tile(self) -> Optional['games.galapagos.tile.Tile']:
        """games.galapagos.tile.Tile or None: The Tile this Creature occupies.
        """
        return self._tile

    def bite(self, tile: 'games.galapagos.tile.Tile') -> bool:
        """Command a creature to bite a plant or creature on the specified tile.

        Args:
            tile (games.galapagos.tile.Tile): The Tile with a plant or creature to bite.

        Returns:
            bool: True if successfully bit, False otherwise.
        """
        return self._run_on_server('bite', {
            'tile': tile
        })

    def breed(self, mate: 'games.galapagos.creature.Creature') -> Optional['games.galapagos.creature.Creature']:
        """Command a creature to breed with an adjacent creature.

        Args:
            mate (games.galapagos.creature.Creature): The Creature to breed with.

        Returns:
            games.galapagos.creature.Creature or None: The baby creature if successful, None otherwise.
        """
        return self._run_on_server('breed', {
            'mate': mate
        })

    def move(self, tile: 'games.galapagos.tile.Tile') -> bool:
        """Command a creature to move to a specified adjacent tile.

        Args:
            tile (games.galapagos.tile.Tile): The Tile to move to.

        Returns:
            bool: True if successfully moved, False otherwise.
        """
        return self._run_on_server('move', {
            'tile': tile
        })
