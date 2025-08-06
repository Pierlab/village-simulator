"""Configuration options for the simulator."""

from dataclasses import dataclass


@dataclass
class Config:
    # Dimensions du monde (zone jouable)
    screen_width: int = 1300
    screen_height: int = 760
    # Largeur du panneau latéral d'information
    menu_width: int = 200

    # Durée d'un tick et nombre de villageois
    tick_duration: int = 40  # ms (pour accélérer la journée à 3 minutes)
    num_villagers: int = 25

    # Vitesse de déplacement (5 km/h)
    kmh_to_pixels_per_tick: float = 0.0

    # Facteurs de déplacement
    movement_random_factor: int = 2  # Intensité de l'aléatoire lors des déplacements
    near_destination_radius: int = 25  # Rayon (en px) de déplacement autour de la cible

    # Tailles des personnages
    adult_radius: int = 15
    child_radius: int = 8
    # Répartition du temps de travail (0-1)
    work_time_ratio: float = 0.6

    # Gestion de la fatigue
    fatigue_max: int = 500
    fatigue_work_rate: int = 2
    fatigue_idle_rate: int = 1
    collapse_sleep_ticks: int = 500  # 6h en supposant 2000 ticks par journée

    # Liste optionnelle de modules de plugins à charger au démarrage
    plugins: tuple[str, ...] = ()

    def __post_init__(self):
        self.kmh_to_pixels_per_tick = (5 * 1000 / 60 / 60) * (self.screen_width / 400)


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
FATIGUE_MAX = config.fatigue_max
FATIGUE_WORK_RATE = config.fatigue_work_rate
FATIGUE_IDLE_RATE = config.fatigue_idle_rate
COLLAPSE_SLEEP_TICKS = config.collapse_sleep_ticks
PLUGINS = config.plugins
