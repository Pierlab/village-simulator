"""Character logic without any rendering concerns."""

import json
import math
import random
import logging
from pathlib import Path
from settings import (
    KMH_TO_PIXELS_PER_TICK,
    NEAR_DESTINATION_RADIUS,
    ADULT_RADIUS,
    CHILD_RADIUS,
)

BASE_PATH = Path(__file__).resolve().parent

with open(BASE_PATH / "genders.json", "r", encoding="utf-8") as f:
    _GENDERS = {g["name"]: g for g in json.load(f)}

with open(BASE_PATH / "professions.json", "r", encoding="utf-8") as f:
    _ROLES = {r["name"]: r for r in json.load(f)}


class Character:
    """Représente un villageois logique avec un genre et un rôle."""

    genders = _GENDERS
    roles = _ROLES

    def __init__(self, name, position, random_factor=1.0, role=None, gender=None):
        self.name = name
        self.position = tuple(map(float, position))
        # Position de référence du foyer (centre de la maison)
        self.home_position = self.position
        self.state = "idle"
        self.target = self.position
        # Point autour duquel le personnage gravite lorsqu'il est immobile
        self.anchor = self.position
        self.last_phase = None
        self.random_factor = random_factor
        # Temps d'arrêt restant lors des mouvements saccadés
        self.idle_timer = 0

        # Attribution du genre
        if gender is None:
            gender = random.choice(list(self.genders))
        g_info = self.genders[gender]
        self.gender = gender
        self.gender_color = tuple(g_info["color"])

        # Attribution du rôle/profession
        if role is None:
            role = random.choice(list(self.roles))
        r_info = self.roles[role]
        self.role = role
        self.role_color = tuple(r_info["color"])
        self.role_building = r_info.get("building")

        # Taille différente selon l'âge (enfant/adulte)
        self.radius = CHILD_RADIUS if role == "enfant" else ADULT_RADIUS

    def choose_action(self, day_phase, world):
        """Choisit une action lorsque la phase de la journée change."""
        if day_phase == self.last_phase:
            return

        self.last_phase = day_phase

        if day_phase in ("matin", "midi"):
            target_building = None
            if self.role_building:
                for b in world.buildings:
                    if b.type == self.role_building:
                        target_building = b
                        break
            if target_building:
                self.anchor = target_building.center
                self.target = self.anchor
                self.state = f"Aller vers {target_building.name}"
            else:
                self.anchor = self.position
                self.target = self.position
                self.state = "Rester immobile"
        elif day_phase == "soir":
            self.anchor = self.home_position
            self.target = self.home_position
            self.state = "Retourner à la maison"
        elif day_phase == "nuit":
            self.anchor = self.home_position
            self.target = self.home_position
            self.state = "Dormir"

        logging.info(f"{self.name} -> {self.state} ({day_phase})")

    def move_towards_target(self):
        """Déplace le personnage vers sa cible avec une part d'aléatoire."""
        # Gestion des pauses lors des mouvements saccadés
        if self.idle_timer > 0:
            self.idle_timer -= 1
            return

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
                self.position = self.anchor
            else:
                # Choisit une nouvelle petite destination autour de l'ancre dans un rayon circulaire
                angle = random.uniform(0, 2 * math.pi)
                radius = random.uniform(0, NEAR_DESTINATION_RADIUS)
                self.target = (
                    self.anchor[0] + math.cos(angle) * radius,
                    self.anchor[1] + math.sin(angle) * radius,
                )
                self.idle_timer = random.randint(5, 20)
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

