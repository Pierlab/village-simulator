"""Point d'entrée de la simulation et configuration initiale."""

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
from renderer import Renderer
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
    appearance = {}
    with open("map.json", "r", encoding="utf-8") as f:
        map_data = json.load(f)
        for item in map_data:
            cfg = building_configs.get(item["type"], {})
            color = tuple(item.get("color", cfg.get("color", (100, 100, 100))))
            size = tuple(item.get("size", cfg.get("size", (40, 40))))
            building = Building(
                item["name"],
                tuple(item["position"]),
                size,
                type=item["type"],
            )
            world.add_building(building)
            appearance[building] = color

    # Vérification du nombre de bâtiments
    if len(world.buildings) != len(map_data):
        logging.warning("Le nombre de bâtiments affichés ne correspond pas à ceux définis dans map.json.")

    # Chargement des données de personnalisation
    with open("names.json", "r", encoding="utf-8") as f:
        names = json.load(f)
    with open("genders.json", "r", encoding="utf-8") as f:
        genders = [g["name"] for g in json.load(f)]
    with open("professions.json", "r", encoding="utf-8") as f:
        roles = [r["name"] for r in json.load(f)]

    # Initialisation des personnages : chacun commence dans une maison
    houses = [b for b in world.buildings if b.type == "maison"]
    if houses:
        home_buildings = [random.choice(houses) for _ in range(NUM_VILLAGERS)]
    else:
        home_buildings = [None] * NUM_VILLAGERS

    villagers = []
    for home in home_buildings:
        position = home.center if home else (0, 0)
        villagers.append(
            Character(
                name=random.choice(names),
                position=position,
                random_factor=MOVEMENT_RANDOM_FACTOR,
                role=random.choice(roles),
                gender=random.choice(genders),
            )
        )

    # Initialisation de la simulation et du rendu
    simulation = Simulation(world, villagers)
    renderer = Renderer(screen, world, appearance)

    # Simulation loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.run_tick()
        renderer.draw(villagers, simulation.time_of_day)
        clock.tick(1000 // TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()
