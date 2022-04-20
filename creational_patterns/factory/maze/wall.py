from factory.maze.mapsite import MapSite


class Wall(MapSite):
    def enter(self):
        raise NotImplementedError


class BombedWall(Wall):
    pass
