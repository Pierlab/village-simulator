import pygame
from world import World, Building
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import json

# Charger les bâtiments depuis le fichier buildings.json
with open("buildings.json", "r") as f:
    BUILDINGS = [(b["name"], (40, 40)) for b in json.load(f)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Éditeur de carte - Village Simulator")
    font = pygame.font.SysFont(None, 32)
    world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
    building_idx = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and building_idx < len(BUILDINGS):
                mx, my = pygame.mouse.get_pos()
                name, size = BUILDINGS[building_idx]
                world.add_building(Building(name, (mx, my), size, type=name.lower()))
                building_idx += 1
        screen.fill((220, 220, 220))
        # Affichage des bâtiments déjà placés
        for b in world.buildings:
            bx, by = b.position
            bw, bh = b.size
            color = (100, 100, 100)
            pygame.draw.rect(screen, color, (bx, by, bw, bh))
        # Indication du prochain bâtiment à placer
        if building_idx < len(BUILDINGS):
            txt = font.render(f"Cliquez pour placer: {BUILDINGS[building_idx][0]}", True, (0,0,0))
            screen.blit(txt, (20, 20))
        else:
            if len(world.buildings) != len(BUILDINGS):
                error_txt = font.render("Erreur: Nombre de bâtiments incorrect!", True, (255, 0, 0))
                screen.blit(error_txt, (20, 60))
            else:
                txt = font.render("Tous les bâtiments sont placés !", True, (0,100,0))
                screen.blit(txt, (20, 20))
                # Sauvegarde de la carte
                import json
                with open("map.json", "w") as f:
                    json.dump([{"name": b.name, "position": b.position, "size": b.size, "type": b.type} for b in world.buildings], f)
        # Afficher les noms des bâtiments
        for b in world.buildings:
            bx, by = b.position
            name_txt = font.render(b.name, True, (0, 0, 0))
            screen.blit(name_txt, (bx, by - 20))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
