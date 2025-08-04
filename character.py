import random

class Character:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # (x, y)
        self.state = "idle"  # travail ou repos
        self.target = None

    def choose_action(self, day_phase, world):
        """Choisit une action selon la phase de la journée."""
        if day_phase == "matin" or day_phase == "midi":
            if random.random() < 0.5:  # 50% de chance de rester immobile
                self.target = self.position
                self.state = "Rester immobile"
            else:
                if world.buildings:
                    target_building = random.choice(world.buildings)
                    self.target = target_building.position
                    self.state = f"Aller vers {target_building.name}"
                else:
                    self.target = self.position
                    self.state = "Rester immobile"

    def move_towards_target(self):
        """Déplace le personnage directement vers la cible en ligne droite."""
        if self.position == self.target:
            return

        x, y = self.position
        tx, ty = self.target

        # Calculer le déplacement en ligne droite
        dx = 1 if tx > x else -1 if tx < x else 0
        dy = 1 if ty > y else -1 if ty < y else 0

        # Mettre à jour la position directement
        self.position = (x + dx, y + dy)

    def perform_daily_action(self, day_phase, world):
        """Effectue une action en fonction de la phase de la journée."""
        self.choose_action(day_phase, world)
        if self.position != self.target:
            self.move_towards_target()
