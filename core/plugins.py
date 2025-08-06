"""Simple plugin registry for simulation extensions."""

from importlib import import_module
import logging

_registry = {}


def register_node_type(name, cls):
    """Register a node class under a given name."""
    _registry[name] = cls
    return cls


def get_node_type(name):
    """Retrieve a registered node class by name."""
    return _registry.get(name)


def load_plugins(module_names):
    """Dynamically import a list of plugin modules.

    Each module is expected to call :func:`register_node_type` during import.
    Any import error is logged but does not stop the program.
    """
    for mod in module_names:
        try:
            import_module(mod)
            logging.info("Plugin loaded: %s", mod)
        except Exception as exc:  # pragma: no cover - defensive
            logging.error("Failed to load plugin %s: %s", mod, exc)
