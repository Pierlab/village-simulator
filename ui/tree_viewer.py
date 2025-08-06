import pygame
from pygame.math import Vector2

NODE_SIZE = (120, 30)
LEVEL_HEIGHT = 80
H_MARGIN = 20
FONT = None

def layout(root, level=0, x=0, positions=None):
    positions = positions or {}
    children = root.children
    if not children:
        positions[root] = Vector2(x, level * LEVEL_HEIGHT)
        return x + NODE_SIZE[0] + H_MARGIN
    start_x = x
    for c in children:
        x = layout(c, level + 1, x, positions)
    mid = (start_x + x - H_MARGIN) / 2
    positions[root] = Vector2(mid, level * LEVEL_HEIGHT)
    return x

def draw_node(screen, node, pos, selected):
    rect = pygame.Rect(pos.x, pos.y, *NODE_SIZE)
    color = (200, 200, 255) if node is selected else (230, 230, 230)
    pygame.draw.rect(screen, color, rect, border_radius=4)
    pygame.draw.rect(screen, (50, 50, 50), rect, 1, border_radius=4)
    text = FONT.render(node.name, True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=rect.center))
    return rect

def run_viewer(root):
    """Affiche l'arbre de nœuds `SimNode` à partir de ``root``."""
    pygame.init()
    global FONT
    FONT = pygame.font.SysFont(None, 18)
    positions = {}
    width = layout(root, positions=positions)
    height = max(p.y for p in positions.values()) + NODE_SIZE[1] + LEVEL_HEIGHT
    screen = pygame.display.set_mode((int(width), int(height)))
    clock = pygame.time.Clock()
    selected = None
    rects = {}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for node, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        selected = node
        screen.fill((255, 255, 255))
        for parent in positions:
            for child in parent.children:
                pygame.draw.line(
                    screen,
                    (150, 150, 150),
                    positions[parent] + Vector2(NODE_SIZE[0] / 2, NODE_SIZE[1]),
                    positions[child] + Vector2(NODE_SIZE[0] / 2, 0),
                    1,
                )
        rects = {}
        for node, pos in positions.items():
            rects[node] = draw_node(screen, node, pos, selected)
        pygame.display.flip()
        clock.tick(30)
