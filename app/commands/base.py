class BaseCommand:
    """Base class for all calculator commands."""
    name = None  # Must be overridden by subclasses

    def execute(self, *args):
        """Execute the command. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement 'execute' method")
