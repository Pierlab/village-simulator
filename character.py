import math
import random
from settings import KMH_TO_PIXELS_PER_TICK


class Character:
    def __init__(self, name, position):
        self.name = name
        # positions are stored as floats to permettre des déplacements fluides
        self.position = tuple(map(float, position))  # Position actuelle (x, y)
        self.home_position = self.position  # Domicile
        self.state = "idle"
        self.target = self.position
        self.last_phase = None

    def choose_action(self, day_phase, world):
        """Choisit une action lorsque la phase de la journée change."""
        if day_phase == self.last_phase:
            return

        self.last_phase = day_phase

        if day_phase in ("matin", "midi"):
            if not world.buildings or random.random() < 0.5:
                self.target = self.position
                self.state = "Rester immobile"
            else:
                target_building = random.choice(world.buildings)
                self.target = target_building.position
                self.state = f"Aller vers {target_building.name}"
        elif day_phase == "soir":
            self.target = self.home_position
            self.state = "Retourner à la maison"
        elif day_phase == "nuit":
            self.target = self.home_position
            self.state = "Dormir"

    def move_towards_target(self):
        """Déplace le personnage vers sa cible avec une légère part d'aléatoire."""
        # Aucun mouvement si le personnage dort
        if self.state == "Dormir" and self.position == self.target:
            return

        # Jitter léger lorsque le personnage est immobile (mais réveillé)
        if self.position == self.target:
            jitter = 0.5
            jx = random.uniform(-jitter, jitter)
            jy = random.uniform(-jitter, jitter)
            self.position = (self.position[0] + jx, self.position[1] + jy)
            self.target = self.position
            return

        x, y = self.position
        tx, ty = self.target

        dx = tx - x
        dy = ty - y
        distance = math.hypot(dx, dy)

        # Déplacement avec une petite variation d'angle
        if distance <= KMH_TO_PIXELS_PER_TICK:
            self.position = self.target
            return

        angle = math.atan2(dy, dx) + random.uniform(-0.3, 0.3)
        step = KMH_TO_PIXELS_PER_TICK
        nx = x + math.cos(angle) * step
        ny = y + math.sin(angle) * step

        # Empêche l'éloignement de la cible
        if math.hypot(tx - nx, ty - ny) > distance:
            ratio = step / distance
            nx = x + dx * ratio
            ny = y + dy * ratio

        self.position = (nx, ny)

    def perform_daily_action(self, day_phase, world):
        """Effectue une action en fonction de la phase de la journée."""
        self.choose_action(day_phase, world)
        self.move_towards_target()

