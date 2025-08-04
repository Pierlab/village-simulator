# Point d'entrée de la simulation

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, NUM_VILLAGERS, TICK_DURATION
from character import Character
from world import World, Building
from simulation import Simulation
import json
import logging
import random  # Importation de random pour le choix aléatoire

# Configuration du logging
logging.basicConfig(
    filename='simulation.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
logging.info("Simulation démarrée.")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Village Simulator")

    # Initialisation du monde et des bâtiments
    world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Chargement des données de la carte depuis le fichier JSON
    with open("map.json", "r", encoding="utf-8") as f:
        map_data = json.load(f)
        for item in map_data:
            world.add_building(
                Building(item["name"], tuple(item["position"]), tuple(item["size"]), type=item["type"])
            )

    # Vérification du nombre de bâtiments
    if len(world.buildings) != len(map_data):
        logging.warning("Le nombre de bâtiments affichés ne correspond pas à ceux définis dans map.json.")

    # Chargement des noms depuis names.json
    with open("names.json", "r", encoding="utf-8") as f:
        names = json.load(f)

    # Initialisation des personnages : chacun commence dans un bâtiment existant
    if world.buildings:
        # Assigne un bâtiment unique à chaque villageois si possible
        home_buildings = (
            random.sample(world.buildings, NUM_VILLAGERS)
            if len(world.buildings) >= NUM_VILLAGERS
            else [random.choice(world.buildings) for _ in range(NUM_VILLAGERS)]
        )
    else:
        home_buildings = [None] * NUM_VILLAGERS

    villagers = []
    for home in home_buildings:
        position = home.position if home else (0, 0)
        villagers.append(
            Character(
                name=random.choice(names),
                position=position
            )
        )

    # Initialisation de la simulation
    simulation = Simulation(world, villagers)

    # Affichage des bâtiments avec leurs noms
    font = pygame.font.SysFont(None, 32)
    for b in world.buildings:
        bx, by = b.position
        bw, bh = b.size
        color = (100, 100, 100)
        pygame.draw.rect(screen, color, (bx, by, bw, bh))
        name_text = font.render(b.name, True, (0, 0, 0))
        screen.blit(name_text, (bx, by - 20))

    # Simulation loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.run_tick()

        # Affichage
        screen.fill((50, 150, 50))
        for b in world.buildings:
            bx, by = b.position
            bw, bh = b.size
            pygame.draw.rect(screen, (100, 100, 100), (bx, by, bw, bh))
            name_text = font.render(b.name, True, (0, 0, 0))
            screen.blit(name_text, (bx, by - 20))

        # Affichage des personnages
        for villager in villagers:
            vx, vy = villager.position
            pygame.draw.circle(screen, (0, 0, 255), (int(vx), int(vy)), 10)  # Cercle bleu pour représenter les personnages
            name_text = font.render(villager.name, True, (255, 255, 255))
            screen.blit(name_text, (int(vx) - 20, int(vy) - 20))

        pygame.display.flip()
        clock.tick(1000 // TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()
