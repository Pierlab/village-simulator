"""Simple plugin registry for simulation extensions."""

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
    """
    for mod in module_names:
        __import__(mod)
