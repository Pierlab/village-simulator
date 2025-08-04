# Paramètres globaux
# next step: Définir résolution écran, tick duration, nombre de villageois

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TICK_DURATION = 20  # ms (pour accélérer la journée à 3 minutes)
NUM_VILLAGERS = 10

# Vitesse de déplacement des villageois (en pixels par tick, calculée pour 5 km/h)
KMH_TO_PIXELS_PER_TICK = (5 * 1000 / 60 / 60) * (SCREEN_WIDTH / 60000)
