import abc
from typing import List
from pprint import pprint

from factory.maze.door import Door
from factory.maze.room import Room, RoomWithBomb
from factory.maze.wall import Wall, BombedWall


class AbstractFactory(metaclass=abc.ABCMeta):
    """Abstract Maze Factory"""

    @abc.abstractclassmethod
    def make_maze(self):
        raise NotImplementedError

    def make_wall(self):
        raise NotImplementedError

    def make_room(self, room_number: int):
        raise NotImplementedError

    def make_door(self, r1: Room, r2: Room):
        raise NotImplementedError


class MazeFactory(AbstractFactory):
    """Concrete Maze Factory"""

    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, room_number: int):
        return Room(room_number)

    def make_door(self, r1: Room, r2: Room):
        return Door(r1, r2)


class BombedMazeFactory(MazeFactory):
    def make_wall(self):
        return BombedWall()

    def make_room(self, room_number: int):
        return RoomWithBomb(room_number)


class Maze:
    def __init__(self):
        self._rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        self._rooms.append(room)
        return None


def create_maze(factory: MazeFactory):
    maze = factory.make_maze()
    r1 = factory.make_room(1)
    r2 = factory.make_room(2)
    door = factory.make_door(r1, r2)

    maze.add_room(r1)
    maze.add_room(r2)

    r1.set_side("north", factory.make_wall())
    r1.set_side("east", factory.make_wall())
    r1.set_side("south", factory.make_wall())
    r1.set_side("west", factory.make_wall())

    r2.set_side("north", factory.make_wall())
    r2.set_side("east", factory.make_wall())
    r2.set_side("south", factory.make_wall())
    r2.set_side("west", door)

    pprint(maze)

    return maze


if __name__ == "__main__":
    factory = MazeFactory()
    create_maze(factory)
