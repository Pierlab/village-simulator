# Boucle principale, gestion du temps, des agents et de leurs actions
"""Core simulation loop built on top of the SimNode tree."""

import logging
from simnode import SimNode


class Simulation(SimNode):
    def __init__(self, world, characters):
        super().__init__("simulation")
        self.world = world
        self.add_child(world)
        for char in characters:
            world.add_character(char)
        self.characters = self.world.characters
        self.tick = 0
        self.day_phase = None
        self.phases = ["matin", "midi", "apres_midi", "soir", "nuit"]
        self.phase_durations = [500, 250, 250, 500, 500]  # ticks par phase
        self.time_of_day = 0.0  # Heure de la journée en heures

    def update_phase(self):
        tick_in_day = self.tick % sum(self.phase_durations)
        cumulative = 0
        new_phase = self.phases[0]
        for phase, duration in zip(self.phases, self.phase_durations):
            cumulative += duration
            if tick_in_day < cumulative:
                new_phase = phase
                break
        changed = new_phase != self.day_phase
        self.day_phase = new_phase
        return changed

    def run_tick(self):
        """Exécute un tick de la simulation."""
        self.tick += 1
        total_ticks = sum(self.phase_durations)
        # Début d'une nouvelle journée : remise à zéro des compteurs d'occupation
        if (self.tick - 1) % total_ticks == 0:
            for char in self.characters:
                char.reset_daily_counters()
        self.time_of_day = ((self.tick % total_ticks) / total_ticks * 24 + 6) % 24
        phase_changed = self.update_phase()

        self.update(self.day_phase)

        if phase_changed:
            logging.info(f"===== {self.day_phase.upper()} {int(self.time_of_day):02d}h =====")
