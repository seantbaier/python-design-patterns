from typing import Any


from factory.maze.mapsite import MapSite


class Door(MapSite):
    def __init__(self, room1: Any, room2: Any):
        self._rooms = room1, room2
        self._is_open = False

    def enter(self):
        return

    @property
    def is_open(self) -> bool:
        return self._is_open

    @is_open.setter
    def is_open(self) -> None:
        self._is_open = not self._is_open
        return None

    def door(self, room_one: int, room_two: int):
        self._room_one = room_one
        self._room_two = room_two
