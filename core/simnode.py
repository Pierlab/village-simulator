class SimNode:
    """Basic building block for the simulation tree with extensible hooks."""

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = None
        self.children = []
        if parent is not None:
            parent.add_child(self)

    # --- tree utilities -------------------------------------------------
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def get_root(self):
        node = self
        while node.parent is not None:
            node = node.parent
        return node

    def path(self):
        node = self
        parts = []
        while node is not None:
            parts.append(node.name)
            node = node.parent
        return list(reversed(parts))

    def find(self, predicate):
        if predicate(self):
            return self
        for child in self.children:
            result = child.find(predicate)
            if result is not None:
                return result
        return None

    # --- hooks -----------------------------------------------------------
    def on_tick(self, *args, **kwargs):
        pass

    def on_enter_phase(self, phase):
        pass

    def on_leave_phase(self, phase):
        pass

    def update(self, *args, **kwargs):
        self.on_tick(*args, **kwargs)
        for child in list(self.children):
            child.update(*args, **kwargs)

    # phase propagation
    def propagate_enter_phase(self, phase):
        self.on_enter_phase(phase)
        for child in self.children:
            child.propagate_enter_phase(phase)

    def propagate_leave_phase(self, phase):
        self.on_leave_phase(phase)
        for child in self.children:
            child.propagate_leave_phase(phase)

    # --- serialization ---------------------------------------------------
    def serialize(self):
        return {
            "name": self.name,
            "path": self.path(),
            "children": [child.serialize() for child in self.children],
        }
