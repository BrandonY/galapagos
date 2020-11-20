# This is where you build your AI for the Galapagos game.

import sys

from typing import List
from joueur.base_ai import BaseAI
import itertools


class AI(BaseAI):
    """ The AI you add and improve code inside to play Galapagos. """

    @property
    def game(self) -> 'games.galapagos.game.Game':
        """games.galapagos.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.galapagos.player.Player':
        """games.galapagos.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        return "The Beagles"

    def find_nearest_prey(self, my_creature):
        my_creatures = self.player.creatures
        opponent_creatures = []
        for c in self.game.creatures:
            if c not in my_creatures and c and c.tile and not c.is_egg:
                opponent_creatures.append(c)

        possible_prey = {} # {prey : (dist, health)}
        # find the nearest creature to bite
        min_dist = 922337203685477580
        for opp_creature in opponent_creatures:
            d = self.dist(my_creature.tile, opp_creature.tile)
            possible_prey[opp_creature] = (d, opp_creature.current_health)
            if d < min_dist:
                min_dist = d
                best_prey = opp_creature

        best_dist = 922337203685477580
        best_health = 922337203685477580
        best_prey = None

        for prey in possible_prey:
            curr_dist = possible_prey[prey][0]
            curr_health = possible_prey[prey][1]
            is_prey_better = (curr_dist < best_dist or (curr_dist == best_dist and curr_health < best_health))
            if is_prey_better:
                best_dist = curr_dist
                best_health = curr_health
                best_prey = prey

        return best_prey

    def bite_prey(self, my_creature) -> None:
        # go bite the creatures
        prey = self.find_nearest_prey(my_creature)
        if not prey:
          return
        if not prey.tile:
          print("Found dead prey")
        path = self.find_path(my_creature.tile, prey.tile)
        if not path:
          return
        while my_creature.movement_left and len(path) >1:
          my_creature.move(path.pop(0))
          path = self.find_path(my_creature.tile, prey.tile)

        if prey and len(path) == 1 and my_creature.can_bite:
          my_creature.bite(path.pop())

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # replace with your start logic

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # replace with your game updated logic

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # replace with your end logic

    def dist(self, tile1, tile2):
      return abs(tile1.x - tile2.x) + abs(tile1.y - tile2.y)

    def find_nearest_plant(self, tile):
      all_plants = [p for p in self.game.plants if p.tile]
      best_plant = None
      best_dist = 9999
      for plant in all_plants:
        # A plant needs to be close, but it's also nice if it's big.
        plant_dist = self.dist(tile, plant.tile)*2 - plant.size
        if plant_dist < best_dist:
          best_dist = plant_dist
          best_plant = plant
      return best_plant

    def seek_plant(self, creature):
      nearest_plant = self.find_nearest_plant(creature.tile)
      path_to_plant = self.find_path(creature.tile, nearest_plant.tile)
      while creature.movement_left and len(path_to_plant) > 1:
        creature.move(path_to_plant.pop(0))

      if nearest_plant and len(path_to_plant) == 1 and creature.can_bite:
        # Would eating be helpful?
        room_in_stomach = creature.max_health - creature.current_health
        benefit_to_eating = creature.herbivorism*5
        eating_kills_plant = nearest_plant.size == 1

        if room_in_stomach and not eating_kills_plant:
          creature.bite(path_to_plant.pop())

    def walk_towards_each_other(self, creature1, creature2):
      while self.dist(creature1.tile, creature2.tile) > 1:
        path = self.find_path(creature1.tile, creature2.tile)[:-1]
        if not path:  # Could happen if dino is surrounded
          break
        if creature1.movement_left:
          creature1.move(path.pop(0))
        elif creature2.movement_left:
          creature2.move(path.pop())
        else:
          break

    def my_creatures(self):
        return [c for c in self.player.creatures if c.tile]

    def eligible_to_breed(self, creature):
      """Heuristic for which dinosaur should breed."""

      # Maybe also don't breed if there are baddies nearby.
      return creature.can_breed and creature.current_health/creature.max_health > 0.8

    def all_possible_pairings(self, dinos):
      # Stolen from https://stackoverflow.com/questions/18172810/optimal-strategy-for-choosing-pairs-from-a-list-of-combinations
      dinos = dinos.copy()
      n = len(dinos)
      if n % 2:
        dinos.append('_')
        n += 1
      cycles = []
      for _ in range(n-1):
        c = list(zip(dinos[:n//2], reversed(dinos[n//2:])))
        cycles.append(c)
        dinos.insert(1, dinos.pop())

      cycles = [c for c in [
             [(p1, p2) for p1, p2 in c if p1 != '_' and p2 != '_']]]

      return cycles

    def try_to_breed(self):
      eligible_dinos = [c for c in self.my_creatures() if self.eligible_to_breed(c)]
      if len(eligible_dinos) < 2:
        print("Not enough healthy dinos to breed")
        return
      possible_pairings = self.all_possible_pairings(eligible_dinos)

      # TODO: some heurisitic for best pairings -- maybe distance, or health.

      for dino1, dino2 in possible_pairings[0]:
        self.walk_towards_each_other(dino1, dino2)
        if self.dist(dino1.tile, dino2.tile) == 1:
          dino1.breed(dino2)

    def would_win_in_a_fight(self):
      """Heuristic for whether we're pretty clearly healthier than the other team."""
      our_health


    def run_turn(self) -> bool:
        """This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        if self.game.current_turn < 75:
          for creature in self.my_creatures():
            self.seek_plant(creature)
          self.try_to_breed()
        else:
          for creature in self.my_creatures():
            self.bite_prey(creature)

        # Put your game logic here for runTurn
        return True


    def find_path(self, start: 'games.galapagos.tile.Tile', goal: 'games.galapagos.tile.Tile') -> List['games.galapagos.tile.Tile']:
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.galapagos.tile.Tile): The starting Tile to find a path from.
            goal (games.galapagos.tile.Tile): The goal (destination) Tile to find a path to.

        Returns:
            list[games.galapagos.tile.Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
        """

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and (
                    neighbor.is_pathable()
                ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where
        # you want to go; in that case, we'll just return an empty path.
        return []
