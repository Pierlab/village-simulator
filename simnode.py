class SimNode:
    """Basic building block for the simulation tree."""

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = None
        self.children = []
        if parent is not None:
            parent.add_child(self)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def update(self, *args, **kwargs):
        for child in list(self.children):
            child.update(*args, **kwargs)

    def serialize(self):
        return {
            "name": self.name,
            "children": [child.serialize() for child in self.children],
        }
