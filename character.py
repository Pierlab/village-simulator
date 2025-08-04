import math
import random
import logging
from settings import KMH_TO_PIXELS_PER_TICK, NEAR_DESTINATION_RADIUS


class Character:
    def __init__(self, name, position, random_factor=1.0):
        self.name = name
        self.position = tuple(map(float, position))
        self.home_position = self.position
        self.state = "idle"
        self.target = self.position
        self.last_phase = None
        self.random_factor = random_factor

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

        logging.info(f"{self.name} -> {self.state} ({day_phase})")

    def move_towards_target(self):
        """Déplace le personnage vers sa cible avec une part d'aléatoire."""
        # Aucun mouvement si le personnage dort déjà chez lui
        if self.state == "Dormir" and self.position == self.target:
            return

        x, y = self.position
        tx, ty = self.target

        dx = tx - x
        dy = ty - y
        distance = math.hypot(dx, dy)

        if distance <= NEAR_DESTINATION_RADIUS:
            if self.state == "Dormir":
                self.position = self.target
            else:
                self.target = (
                    tx + random.uniform(-NEAR_DESTINATION_RADIUS, NEAR_DESTINATION_RADIUS),
                    ty + random.uniform(-NEAR_DESTINATION_RADIUS, NEAR_DESTINATION_RADIUS),
                )
            return

        angle = math.atan2(dy, dx) + random.uniform(-0.3, 0.3) * self.random_factor
        step = KMH_TO_PIXELS_PER_TICK
        nx = x + math.cos(angle) * step
        ny = y + math.sin(angle) * step

        if math.hypot(tx - nx, ty - ny) > distance:
            ratio = step / distance
            nx = x + dx * ratio
            ny = y + dy * ratio

        self.position = (nx, ny)

    def perform_daily_action(self, day_phase, world):
        """Effectue une action en fonction de la phase de la journée."""
        self.choose_action(day_phase, world)
        self.move_towards_target()

