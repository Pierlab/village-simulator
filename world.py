"""Logical representation of the game world.

This module purposely avoids any rendering code; drawing is delegated to the
``renderer`` module so that the world remains a pure data model."""

# Classe Building, représentant un bâtiment logique sans rendu
class Building:
    def __init__(self, name, position, size=(30, 30), type="maison", production=None):
        self.name = name
        self.position = position  # (x, y)
        self.size = size  # (w, h)
        self.type = type  # maison, ferme, forge, taverne, etc.
        self.production = production or {}
        self.inventory = {res: 0 for res in self.production}
        # Centre du bâtiment, utilisé comme point de rassemblement
        self.center = (
            position[0] + size[0] / 2,
            position[1] + size[1] / 2,
        )

    def produce(self):
        for res, rate in self.production.items():
            self.inventory[res] = self.inventory.get(res, 0) + rate

class InteractiveObject:
    def __init__(self, name, position, type):
        self.name = name
        self.position = position
        self.type = type  # lit, table, four, outil, etc.

class Zone:
    def __init__(self, name, area, type):
        self.name = name
        self.area = area  # (x, y, w, h)
        self.type = type  # travail, repos, public

# Classe World, contenant la carte du village et les bâtiments
# next step: Définir la grille et les bâtiments

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]  # Grille de positions
        self.buildings = []  # Liste des bâtiments
        self.objects = []   # Objets interactifs
        self.zones = []     # Zones d'intérêt

    def add_building(self, building):
        bx, by = building.position
        bw, bh = building.size
        if bx < 0 or by < 0 or bx + bw > self.width or by + bh > self.height:
            raise ValueError("Building exceeds world boundaries")
        self.buildings.append(building)
        for x in range(bx, bx + bw):
            for y in range(by, by + bh):
                self.grid[y][x] = building

    def is_position_free(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] is None

    def find_buildings_by_type(self, btype):
        return [b for b in self.buildings if b.type == btype]

    def find_nearest_building(self, position, btype):
        candidates = self.find_buildings_by_type(btype)
        if not candidates:
            return None
        px, py = position
        return min(candidates, key=lambda b: (b.center[0]-px)**2 + (b.center[1]-py)**2)
