"""Configuration options for the simulator."""

from dataclasses import dataclass


@dataclass
class Config:
    # Dimensions du monde (zone jouable)
    screen_width: int = 1200
    screen_height: int = 720
    # Largeur du panneau latéral d'information
    menu_width: int = 200

    # Durée d'un tick et nombre de villageois
    tick_duration: int = 50  # ms (pour accélérer la journée à 3 minutes)
    num_villagers: int = 30

    # Vitesse de déplacement (5 km/h)
    kmh_to_pixels_per_tick: float = 0.0

    # Facteurs de déplacement
    movement_random_factor: int = 10  # Intensité de l'aléatoire lors des déplacements
    near_destination_radius: int = 30  # Rayon (en px) de déplacement autour de la cible

    # Tailles des personnages
    adult_radius: int = 15
    child_radius: int = 6
    # Répartition du temps de travail (0-1)
    work_time_ratio: float = 0.6

    def __post_init__(self):
        self.kmh_to_pixels_per_tick = (5 * 1000 / 60 / 60) * (self.screen_width / 500)


config = Config()

# Compatibilité ascendante : export des constantes
SCREEN_WIDTH = config.screen_width
SCREEN_HEIGHT = config.screen_height
MENU_WIDTH = config.menu_width
TICK_DURATION = config.tick_duration
NUM_VILLAGERS = config.num_villagers
KMH_TO_PIXELS_PER_TICK = config.kmh_to_pixels_per_tick
MOVEMENT_RANDOM_FACTOR = config.movement_random_factor
NEAR_DESTINATION_RADIUS = config.near_destination_radius
ADULT_RADIUS = config.adult_radius
CHILD_RADIUS = config.child_radius
WORK_TIME_RATIO = config.work_time_ratio
