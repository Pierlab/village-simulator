import math
import math
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from world import World, Building
from character import Character
from simulation import Simulation
from settings import NEAR_DESTINATION_RADIUS


def test_phase_progression():
    world = World(10, 10)
    char = Character("Test", (0, 0), role="enfant", gender="homme")
    sim = Simulation(world, [char])
    assert sim.day_phase is None
    sim.run_tick()
    assert sim.day_phase == "matin"
    for _ in range(sim.phase_durations[0]):
        sim.run_tick()
    assert sim.day_phase == "midi"


def test_character_stays_near_anchor():
    random.seed(0)
    char = Character("Bob", (0, 0), random_factor=0, role="enfant", gender="homme")
    char.state = "Rester immobile"
    char.anchor = (0, 0)
    char.target = (0, 0)
    for _ in range(200):
        char.move_towards_target()
        ax, ay = char.anchor
        cx, cy = char.position
        assert math.hypot(cx - ax, cy - ay) <= NEAR_DESTINATION_RADIUS + 1e-6


def test_children_go_to_school():
    world = World(100, 100)
    school = Building("École", (10, 10), size=(10, 10), type="école")
    world.add_building(school)
    child = Character("Kid", (0, 0), role="enfant", gender="homme", random_factor=0)
    child.perform_daily_action("matin", world)
    assert child.anchor == school.center
    assert child.state.startswith("Aller vers")


def test_role_goes_to_associated_building():
    world = World(100, 100)
    forge = Building("Forge", (20, 20), size=(10, 10), type="forge")
    world.add_building(forge)
    smith = Character("Smith", (0, 0), role="forgeron", gender="homme", random_factor=0, work_ratio=1.0)
    smith.perform_daily_action("matin", world)
    assert smith.anchor == forge.center
    assert "Forge" in smith.state


def test_adult_goes_to_restaurant_at_lunch():
    world = World(200, 200)
    r1 = Building("R1", (10, 10), size=(10, 10), type="restaurant")
    r2 = Building("R2", (150, 150), size=(10, 10), type="restaurant")
    world.add_building(r1)
    world.add_building(r2)
    adult = Character("Bob", (0, 0), role="forgeron", gender="homme", random_factor=0, work_ratio=1.0)
    adult.perform_daily_action("midi", world)
    assert adult.anchor == r1.center


def test_children_stay_at_school_at_lunch():
    world = World(200, 200)
    school = Building("École", (50, 50), size=(10, 10), type="école")
    world.add_building(school)
    child = Character("Kid", (0, 0), role="enfant", gender="homme", random_factor=0)
    child.perform_daily_action("midi", world)
    assert child.anchor == school.center


def test_building_produces_resources_with_occupants():
    world = World(200, 200)
    farm = Building("Ferme", (0, 0), size=(100, 100), type="ferme", production={"nourriture": 2})
    world.add_building(farm)
    villager = Character("Bob", farm.center, role="fermier", gender="homme", random_factor=0, work_ratio=1.0)
    sim = Simulation(world, [villager])
    sim.run_tick()
    assert farm.inventory["nourriture"] == 2
