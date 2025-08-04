# Point d'entrée de la simulation

import pygame
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    NUM_VILLAGERS,
    TICK_DURATION,
    MOVEMENT_RANDOM_FACTOR,
)
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

    # Chargement des configurations de bâtiments (couleurs, tailles)
    with open("buildings.json", "r", encoding="utf-8") as f:
        building_configs = {b["type"]: b for b in json.load(f)}

    # Chargement des données de la carte depuis le fichier JSON
    with open("map.json", "r", encoding="utf-8") as f:
        map_data = json.load(f)
        for item in map_data:
            cfg = building_configs.get(item["type"], {})
            color = tuple(item.get("color", cfg.get("color", (100, 100, 100))))
            size = tuple(item.get("size", cfg.get("size", (40, 40))))
            world.add_building(
                Building(
                    item["name"],
                    tuple(item["position"]),
                    size,
                    type=item["type"],
                    color=color,
                )
            )

    # Vérification du nombre de bâtiments
    if len(world.buildings) != len(map_data):
        logging.warning("Le nombre de bâtiments affichés ne correspond pas à ceux définis dans map.json.")

    # Chargement des noms depuis names.json
    with open("names.json", "r", encoding="utf-8") as f:
        names = json.load(f)

    # Initialisation des personnages : chacun commence dans une maison
    houses = [b for b in world.buildings if b.type == "maison"]
    if houses:
        home_buildings = [random.choice(houses) for _ in range(NUM_VILLAGERS)]
    else:
        home_buildings = [None] * NUM_VILLAGERS

    villagers = []
    for home in home_buildings:
        position = home.position if home else (0, 0)
        villagers.append(
            Character(
                name=random.choice(names),
                position=position,
                random_factor=MOVEMENT_RANDOM_FACTOR,
            )
        )

    # Initialisation de la simulation
    simulation = Simulation(world, villagers)

    # Affichage initial des bâtiments avec leurs noms
    font = pygame.font.SysFont(None, 20)
    for b in world.buildings:
        bx, by = b.position
        bw, bh = b.size
        pygame.draw.rect(screen, b.color, (bx, by, bw, bh))
        name_text = font.render(b.name, True, (0, 0, 0))
        text_rect = name_text.get_rect(center=(bx + bw / 2, by + bh / 2))
        screen.blit(name_text, text_rect)

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
            pygame.draw.rect(screen, b.color, (bx, by, bw, bh))
            name_text = font.render(b.name, True, (0, 0, 0))
            text_rect = name_text.get_rect(center=(bx + bw / 2, by + bh / 2))
            screen.blit(name_text, text_rect)

        # Affichage des personnages
        for villager in villagers:
            vx, vy = villager.position
            pygame.draw.circle(screen, (0, 0, 255), (int(vx), int(vy)), 10)
            name_text = font.render(villager.name, True, (255, 255, 255))
            text_rect = name_text.get_rect(center=(int(vx), int(vy) - 15))
            screen.blit(name_text, text_rect)

        # Affichage de l'horloge
        hours = int(simulation.time_of_day)
        minutes = int((simulation.time_of_day - hours) * 60)
        clock_text = font.render(f"{hours:02d}:{minutes:02d}", True, (0, 0, 0))
        screen.blit(clock_text, (10, 10))

        pygame.display.flip()
        clock.tick(1000 // TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()
