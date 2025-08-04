# Boucle principale, gestion du temps, des agents et de leurs actions
# next step: Implémenter la boucle de simulation

class Simulation:
    def __init__(self, world, characters):
        self.world = world
        self.characters = characters
        self.tick = 0
        self.day_phase = "matin"
        self.phases = ["matin", "midi", "soir", "nuit"]
        self.phase_duration = 500  # ticks par phase
        self.time = self.tick * 0.1  # Exemple : chaque tick représente 0.1 unité de temps

    def update_phase(self):
        phase_index = (self.tick // self.phase_duration) % len(self.phases)
        self.day_phase = self.phases[phase_index]

    def run_tick(self):
        """Exécute un tick de la simulation."""
        self.tick += 1
        self.time = self.tick * 0.1  # Met à jour l'heure de la simulation
        self.update_phase()
        for char in self.characters:
            char.choose_action(self.day_phase, self.world)
            char.move_towards_target(self.world)
