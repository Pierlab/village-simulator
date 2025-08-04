# Boucle principale, gestion du temps, des agents et de leurs actions
# next step: Implémenter la boucle de simulation

import logging


class Simulation:
    def __init__(self, world, characters):
        self.world = world
        self.characters = characters
        self.tick = 0
        self.day_phase = None
        self.phases = ["matin", "midi", "soir", "nuit"]
        self.phase_duration = 500  # ticks par phase
        self.time_of_day = 0.0  # Heure de la journée en heures

    def update_phase(self):
        phase_index = (self.tick // self.phase_duration) % len(self.phases)
        new_phase = self.phases[phase_index]
        changed = new_phase != self.day_phase
        self.day_phase = new_phase
        return changed

    def run_tick(self):
        """Exécute un tick de la simulation."""
        self.tick += 1
        total_ticks = self.phase_duration * len(self.phases)
        self.time_of_day = ((self.tick % total_ticks) / total_ticks * 24 + 6) % 24
        phase_changed = self.update_phase()
        occupied_positions = []
        for char in self.characters:
            previous_position = char.position
            char.perform_daily_action(self.day_phase, self.world)

            for occupied in occupied_positions:
                dx = char.position[0] - occupied[0]
                dy = char.position[1] - occupied[1]
                if dx * dx + dy * dy < 1:
                    char.position = previous_position
                    break

            occupied_positions.append(char.position)

        if phase_changed:
            logging.info(f"===== {self.day_phase.upper()} {int(self.time_of_day):02d}h =====")
