# Classe Building, représentant un bâtiment
class Building:
    def __init__(self, name, position, size=(30, 30), type="maison"):
        self.name = name
        self.position = position  # (x, y)
        self.size = size  # (w, h)
        self.type = type  # maison, ferme, forge, taverne, etc.

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
        self.buildings.append(building)
        bx, by = building.position
        bw, bh = building.size
        for x in range(bx, bx + bw):
            for y in range(by, by + bh):
                self.grid[y][x] = building

    def is_position_free(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] is None
