# Game: Adapt, Evolve, Segfault.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
from joueur.base_game import BaseGame

# import game objects
from games.galapagos.creature import Creature
from games.galapagos.game_object import GameObject
from games.galapagos.plant import Plant
from games.galapagos.player import Player
from games.galapagos.tile import Tile



class Game(BaseGame):
    """The class representing the Game in the Galapagos game.

    Adapt, Evolve, Segfault.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._base_health = 0
        self._creatures = []
        self._current_player = None
        self._current_turn = 0
        self._damage_multiplier = 0
        self._game_objects = {}
        self._health_per_breed = 0
        self._health_per_carnivorism = 0
        self._health_per_endurance = 0
        self._health_per_herbivorism = 0
        self._health_per_move = 0
        self._health_per_turn = 0
        self._map_height = 0
        self._map_width = 0
        self._max_plant_size = 0
        self._max_starting_creatures = 0
        self._max_starting_plants = 0
        self._max_stat_value = 0
        self._max_turns = 100
        self._min_starting_creatures = 0
        self._min_starting_plants = 0
        self._plants = []
        self._players = []
        self._session = ""
        self._tiles = []
        self._time_added_per_turn = 0

        self.name = "Galapagos"

        self._game_object_classes = {
            'Creature': Creature,
            'GameObject': GameObject,
            'Plant': Plant,
            'Player': Player,
            'Tile': Tile
        }

    @property
    def base_health(self) -> int:
        """int: The amount of health that a creature with a 0 endurance stat starts with.
        """
        return self._base_health

    @property
    def creatures(self) -> List['games.galapagos.creature.Creature']:
        """list[games.galapagos.creature.Creature]: Every Creature in the game.
        """
        return self._creatures

    @property
    def current_player(self) -> 'games.galapagos.player.Player':
        """games.galapagos.player.Player: The player whose turn it is currently. That player can send commands. Other players cannot.
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """int: The current turn number, starting at 0 for the first player's turn.
        """
        return self._current_turn

    @property
    def damage_multiplier(self) -> int:
        """int: How much to damage an opponent per difference of carnivorism and defense.
        """
        return self._damage_multiplier

    @property
    def game_objects(self) -> Dict[str, 'games.galapagos.game_object.GameObject']:
        """dict[str, games.galapagos.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def health_per_breed(self) -> int:
        """int: The amount of extra health from both breeding creatures required if you have more total health than your opponent.
        """
        return self._health_per_breed

    @property
    def health_per_carnivorism(self) -> int:
        """int: Multiplied by carnivorism to determine health gained from eating creatures.
        """
        return self._health_per_carnivorism

    @property
    def health_per_endurance(self) -> int:
        """int: The amount of extra health for each point of endurance.
        """
        return self._health_per_endurance

    @property
    def health_per_herbivorism(self) -> int:
        """int: Multiplied by herbivorism to determine health gained from biting plants.
        """
        return self._health_per_herbivorism

    @property
    def health_per_move(self) -> int:
        """int: The amount of health required to move.
        """
        return self._health_per_move

    @property
    def health_per_turn(self) -> int:
        """int: The amount of health lost after each of your turns.
        """
        return self._health_per_turn

    @property
    def map_height(self) -> int:
        """int: The number of Tiles in the map along the y (vertical) axis.
        """
        return self._map_height

    @property
    def map_width(self) -> int:
        """int: The number of Tiles in the map along the x (horizontal) axis.
        """
        return self._map_width

    @property
    def max_plant_size(self) -> int:
        """int: The maximum size a plant to grow to.
        """
        return self._max_plant_size

    @property
    def max_starting_creatures(self) -> int:
        """int: The maximum number of creatures that each player will start with.
        """
        return self._max_starting_creatures

    @property
    def max_starting_plants(self) -> int:
        """int: The maximum number of plants that the map will start with.
        """
        return self._max_starting_plants

    @property
    def max_stat_value(self) -> int:
        """int: The maxmimum value that a stat (carnivorism, herbivorism, defense, endurance, speed) can have.
        """
        return self._max_stat_value

    @property
    def max_turns(self) -> int:
        """int: The maximum number of turns before the game will automatically end.
        """
        return self._max_turns

    @property
    def min_starting_creatures(self) -> int:
        """int: The minimum number of creatures that each player will start with.
        """
        return self._min_starting_creatures

    @property
    def min_starting_plants(self) -> int:
        """int: The minimum number of plants that the map will start with.
        """
        return self._min_starting_plants

    @property
    def plants(self) -> List['games.galapagos.plant.Plant']:
        """list[games.galapagos.plant.Plant]: Every Plant in the game.
        """
        return self._plants

    @property
    def players(self) -> List['games.galapagos.player.Player']:
        """list[games.galapagos.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    @property
    def tiles(self) -> List['games.galapagos.tile.Tile']:
        """list[games.galapagos.tile.Tile]: All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.
        """
        return self._tiles

    @property
    def time_added_per_turn(self) -> int:
        """int: The amount of time (in nano-seconds) added after each player performs a turn.
        """
        return self._time_added_per_turn

    def get_tile_at(self, x: int, y: int) -> Optional['games.galapagos.tile.Tile']:
        """Gets the Tile at a specified (x, y) position.

        Args:
            x (int): An integer between 0 and the map_width.
            y (int): An integer between 0 and the map_height.

        Returns:
            games.galapagos.tile.Tile or None: The Tile at (x, y) or None if out of bounds.
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]
