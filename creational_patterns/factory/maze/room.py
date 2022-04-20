from typing import Dict, Any


from factory.maze.mapsite import MapSite


class Room(MapSite):
    def __init__(self, room_number: int):
        self._room_number: int = room_number
        self._sides: Dict[str, Any] = {}

    def set_side(self, direction, side: Any) -> Any:
        self._sides[direction] = side
        return side

    def enter(self):
        raise NotImplementedError


class RoomWithBomb(Room):
    pass
