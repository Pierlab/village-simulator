"""Configuration options for the simulator."""

# Paramètres globaux
# next step: Définir résolution écran, tick duration, nombre de villageois

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TICK_DURATION = 50  # ms (pour accélérer la journée à 3 minutes)
NUM_VILLAGERS = 30

# Vitesse de déplacement des villageois (en pixels par tick, calculée pour 5 km/h)
KMH_TO_PIXELS_PER_TICK = (5 * 1000 / 60 / 60) * (SCREEN_WIDTH / 500)

# Facteurs de déplacement
MOVEMENT_RANDOM_FACTOR = 10  # Intensité de l'aléatoire lors des déplacements
NEAR_DESTINATION_RADIUS = 30  # Rayon (en px) de déplacement autour de la cible

# Tailles des personnages selon l'âge
ADULT_RADIUS = 15
CHILD_RADIUS = 6
