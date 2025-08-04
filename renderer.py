"""Rendering helpers for the village simulator.

The :class:`Renderer` draws the world and characters using Pygame.
Static elements like buildings are pre-rendered on a background surface to
minimise per-frame work."""

import pygame


class Renderer:
    """Draws the logical world state to a Pygame screen."""

    def __init__(self, screen, world, appearance):
        self.screen = screen
        self.world = world
        self.appearance = appearance  # mapping building -> colour
        self.font = pygame.font.SysFont(None, 20)
        # Pre-render static background with buildings
        self.background = pygame.Surface(screen.get_size())
        self._draw_static_world()

    def _draw_static_world(self):
        self.background.fill((50, 150, 50))
        for building in self.world.buildings:
            bx, by = building.position
            bw, bh = building.size
            color = self.appearance.get(building, (100, 100, 100))
            pygame.draw.rect(self.background, color, (bx, by, bw, bh))
            name_text = self.font.render(building.name, True, (0, 0, 0))
            text_rect = name_text.get_rect(center=(bx + bw / 2, by + bh / 2))
            self.background.blit(name_text, text_rect)

    def draw(self, villagers, time_of_day):
        """Render villagers and UI on top of the static background."""
        self.screen.blit(self.background, (0, 0))
        for villager in villagers:
            vx, vy = villager.position
            radius = villager.radius
            pygame.draw.circle(self.screen, villager.role_color, (int(vx), int(vy)), radius)
            inner_radius = max(1, radius - 3)
            pygame.draw.circle(
                self.screen, villager.gender_color, (int(vx), int(vy)), inner_radius
            )
            name_text = self.font.render(villager.name, True, (255, 255, 255))
            text_rect = name_text.get_rect(center=(int(vx), int(vy) - radius - 5))
            self.screen.blit(name_text, text_rect)

        hours = int(time_of_day)
        minutes = int((time_of_day - hours) * 60)
        clock_text = self.font.render(f"{hours:02d}:{minutes:02d}", True, (0, 0, 0))
        self.screen.blit(clock_text, (10, 10))

        pygame.display.flip()
