import os
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
import pygame

from ui.renderer import Renderer
from nodes.world import World
from nodes.character import Character


def test_selected_info_includes_fatigue():
    pygame.init()
    try:
        screen = pygame.Surface((100, 100))
        world = World(100, 100)
        renderer = Renderer(screen, world)
        char = Character("Bob", (10, 10), role="forgeron", gender="homme")
        char.fatigue = 42
        lines = renderer._selected_info_lines(char)
        assert any("Fatigue" in line and "42" in line for line in lines)
    finally:
        pygame.quit()
