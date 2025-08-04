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
    for _ in range(sim.phase_duration):
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
    smith = Character("Smith", (0, 0), role="forgeron", gender="homme", random_factor=0)
    smith.perform_daily_action("matin", world)
    assert smith.anchor == forge.center
    assert "Forge" in smith.state
