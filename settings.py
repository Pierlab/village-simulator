"""Configuration options for the simulator."""

# Paramètres globaux
# next step: Définir résolution écran, tick duration, nombre de villageois

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TICK_DURATION = 20  # ms (pour accélérer la journée à 3 minutes)
NUM_VILLAGERS = 10

# Vitesse de déplacement des villageois (en pixels par tick, calculée pour 5 km/h)
KMH_TO_PIXELS_PER_TICK = (500 * 1000 / 60 / 60) * (SCREEN_WIDTH / 40000)

# Facteurs de déplacement
MOVEMENT_RANDOM_FACTOR = 0.1  # Intensité de l'aléatoire lors des déplacements
NEAR_DESTINATION_RADIUS = 3  # Rayon (en px) de déplacement autour de la cible

# Tailles des personnages selon l'âge
ADULT_RADIUS = 12
CHILD_RADIUS = 8
