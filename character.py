import random


class Character:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # Position actuelle (x, y)
        self.home_position = position  # Domicile
        self.state = "idle"
        self.target = position
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
        """Déplace le personnage directement vers la cible en ligne droite."""
        if self.position == self.target:
            return

        x, y = self.position
        tx, ty = self.target

        dx = 1 if tx > x else -1 if tx < x else 0
        dy = 1 if ty > y else -1 if ty < y else 0

        self.position = (x + dx, y + dy)

    def perform_daily_action(self, day_phase, world):
        """Effectue une action en fonction de la phase de la journée."""
        self.choose_action(day_phase, world)
        self.move_towards_target()

