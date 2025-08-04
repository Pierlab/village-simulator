"""Rendering helpers for the village simulator.

The :class:`Renderer` draws the world and characters using Pygame.
Static elements like buildings are pre-rendered on a background surface to
minimise per-frame work."""

import pygame
from settings import SCREEN_WIDTH, MENU_WIDTH


class Renderer:
    """Draws the logical world state to a Pygame screen."""

    def __init__(self, screen, world):
        self.screen = screen
        self.world = world
        self.font = pygame.font.SysFont(None, 20)
        self.background = pygame.Surface((world.width, world.height))
        self._draw_static_world()

    def _draw_static_world(self):
        self.background.fill((50, 150, 50))
        for building in self.world.buildings:
            bx, by = building.position
            bw, bh = building.size
            pygame.draw.rect(self.background, building.color, (bx, by, bw, bh))
            name_text = self.font.render(building.name, True, (0, 0, 0))
            text_rect = name_text.get_rect(center=(bx + bw / 2, by + bh / 2))
            self.background.blit(name_text, text_rect)

    def draw(self, villagers, time_of_day, selected=None, paused=False):
        """Render villagers and UI on top of the static background."""
        self.screen.blit(self.background, (0, 0))
        for villager in villagers:
            vx, vy = villager.position
            radius = villager.radius
            # Couleur centrale représentant le genre
            pygame.draw.circle(self.screen, villager.gender_color, (int(vx), int(vy)), radius)
            # Anneau extérieur représentant l'occupation courante
            pygame.draw.circle(
                self.screen, villager.occupation_color, (int(vx), int(vy)), radius, 3
            )
            # Lettres du rôle au centre
            role_text = self.font.render(villager.role_label, True, (0, 0, 0))
            role_rect = role_text.get_rect(center=(int(vx), int(vy)))
            self.screen.blit(role_text, role_rect)
            # Nom au-dessus du personnage
            name_text = self.font.render(villager.name, True, (255, 255, 255))
            text_rect = name_text.get_rect(center=(int(vx), int(vy) - radius - 5))
            self.screen.blit(name_text, text_rect)

        sidebar_rect = (SCREEN_WIDTH, 0, MENU_WIDTH, self.world.height)
        pygame.draw.rect(self.screen, (230, 230, 230), sidebar_rect)

        hours = int(time_of_day)
        minutes = int((time_of_day - hours) * 60)
        clock_text = self.font.render(f"{hours:02d}:{minutes:02d}", True, (0, 0, 0))
        self.screen.blit(clock_text, (SCREEN_WIDTH + 10, 10))

        info_y = 40
        for villager in villagers:
            activity = f"{villager.name}: {villager.current_occupation or villager.state}";
            activity_text = self.font.render(activity, True, (0, 0, 0))
            self.screen.blit(activity_text, (SCREEN_WIDTH + 10, info_y))
            info_y += 15

        info_y += 10
        for building in self.world.buildings:
            if building.inventory:
                inv_str = ", ".join(
                    f"{res}:{qty}" for res, qty in building.inventory.items()
                )
                text = f"{building.name}: {inv_str}"
                inv_text = self.font.render(text, True, (0, 0, 0))
                self.screen.blit(inv_text, (SCREEN_WIDTH + 10, info_y))
                info_y += 15

        if selected:
            info_y += 20
            sel_lines = [
                f"Nom: {selected.name}",
                f"Genre: {selected.gender}",
                f"Rôle: {selected.role}",
                f"Argent: {selected.money}",
            ]
            if selected.inventory:
                inv = ", ".join(f"{k}:{v}" for k, v in selected.inventory.items())
                sel_lines.append(f"Inventaire: {inv}")
            if selected.current_occupation:
                sel_lines.append(f"Occupation: {selected.current_occupation}")
            else:
                sel_lines.append(f"Destination: {selected.state}")
            for line in sel_lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (SCREEN_WIDTH + 10, info_y))
                info_y += 15

        if paused:
            pause_text = self.font.render("PAUSE", True, (200, 0, 0))
            self.screen.blit(pause_text, (SCREEN_WIDTH + 10, self.world.height - 30))

        pygame.display.flip()
