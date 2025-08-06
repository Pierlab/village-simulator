import pygame
from nodes.world import World, Building
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import json

# Charger les bâtiments depuis le fichier buildings.json et générer les occurrences
with open("data/buildings.json", "r", encoding="utf-8") as f:
    _configs = json.load(f)

BUILDINGS = []
for cfg in _configs:
    count = cfg.get("count", 1)
    for i in range(1, count + 1):
        entry = cfg.copy()
        if count > 1:
            entry["name"] = f"{cfg['name']} {i}"
        BUILDINGS.append(entry)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Éditeur de carte - Village Simulator")
    font = pygame.font.SysFont(None, 20)
    world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
    building_idx = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and building_idx < len(BUILDINGS):
                mx, my = pygame.mouse.get_pos()
                building = BUILDINGS[building_idx]
                name = building["name"]
                size = tuple(building.get("size", (40, 40)))
                b_type = building.get("type", name.lower())
                color = tuple(building.get("color", (100, 100, 100)))
                world.add_building(Building(name, (mx, my), size, type=b_type, color=color))
                building_idx += 1
        screen.fill((220, 220, 220))
        # Affichage des bâtiments déjà placés
        for b in world.buildings:
            bx, by = b.position
            bw, bh = b.size
            pygame.draw.rect(screen, b.color, (bx, by, bw, bh))
        # Indication du prochain bâtiment à placer
        if building_idx < len(BUILDINGS):
            txt = font.render(f"Cliquez pour placer: {BUILDINGS[building_idx]['name']}", True, (0,0,0))
            screen.blit(txt, (20, 20))
        else:
            if len(world.buildings) != len(BUILDINGS):
                error_txt = font.render("Erreur: Nombre de bâtiments incorrect!", True, (255, 0, 0))
                screen.blit(error_txt, (20, 60))
            else:
                txt = font.render("Tous les bâtiments sont placés !", True, (0,100,0))
                screen.blit(txt, (20, 20))
                # Sauvegarde de la carte
                with open("data/map.json", "w", encoding="utf-8") as f:
                    json.dump([
                        {
                            "name": b.name,
                            "position": list(b.position),
                            "size": list(b.size),
                            "type": b.type,
                            "color": list(b.color)
                        }
                        for b in world.buildings
                    ], f, ensure_ascii=False)
        # Afficher les noms des bâtiments
        for b in world.buildings:
            bx, by = b.position
            bw, bh = b.size
            name_txt = font.render(b.name, True, (0, 0, 0))
            text_rect = name_txt.get_rect(center=(bx + bw / 2, by + bh / 2))
            screen.blit(name_txt, text_rect)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
