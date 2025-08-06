"""Logical representation of the game world.

This module purposely avoids any rendering code; drawing is delegated to the
``renderer`` module so that the world remains a pure data model.

The module now relies on the :class:`SimNode` infrastructure so that each
element of the simulation can be attached to a tree of nodes."""

from simnode import SimNode


# Classe Building, représentant un bâtiment logique sans rendu
class Building(SimNode):
    def __init__(
        self,
        name,
        position,
        size=(30, 30),
        type="maison",
        production=None,
        color=(100, 100, 100),
    ):
        super().__init__(name)
        self.position = position  # (x, y)
        self.size = size  # (w, h)
        self.type = type  # maison, ferme, forge, taverne, etc.
        self.production = production or {}
        self.inventory = {res: 0 for res in self.production}
        self.money = 0
        self.color = color
        self.occupants = []
        # Centre du bâtiment, utilisé comme point de rassemblement
        self.center = (
            position[0] + size[0] / 2,
            position[1] + size[1] / 2,
        )

    def contains(self, position):
        x, y = position
        bx, by = self.position
        bw, bh = self.size
        return bx <= x <= bx + bw and by <= y <= by + bh

    def produce(self, occupants=0):
        for res, rate in self.production.items():
            self.inventory[res] = self.inventory.get(res, 0) + rate * occupants

    def update(self, *args, **kwargs):  # pragma: no cover - simple passthrough
        self.produce(len(self.occupants))

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

class World(SimNode):
    def __init__(self, width, height, parent=None):
        super().__init__("world", parent)
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]  # Grille de positions
        self.buildings = []  # Liste des bâtiments
        self.characters = []  # Personnages rattachés à ce monde
        self.objects = []   # Objets interactifs
        self.zones = []     # Zones d'intérêt

    def add_building(self, building):
        bx, by = building.position
        bw, bh = building.size
        if bx < 0 or by < 0 or bx + bw > self.width or by + bh > self.height:
            raise ValueError("Building exceeds world boundaries")
        self.buildings.append(building)
        self.add_child(building)
        for x in range(bx, bx + bw):
            for y in range(by, by + bh):
                self.grid[y][x] = building

    def add_character(self, character):
        self.characters.append(character)
        self.add_child(character)

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

    def update(self, day_phase, *args, **kwargs):
        # Réinitialise les occupants de chaque bâtiment
        for b in self.buildings:
            b.occupants = []

        occupied_positions = []
        for char in self.characters:
            char.update(day_phase, self, occupied_positions)

        for b in self.buildings:
            b.update()
