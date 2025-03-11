"""
Dynamically loads plugins for the Advanced Python Calculator.
"""
import importlib
import pkgutil
import logging
import app.plugins

logger = logging.getLogger("app")


def load_plugins(invoker):
    """Dynamically load all plugins only once."""
    for _, module_name, _ in pkgutil.iter_modules(app.plugins.__path__):
        try:
            module = importlib.import_module(f"app.plugins.{module_name}")
            if hasattr(module, "COMMAND_NAME") and hasattr(module, "PowerCommand"):
                invoker.register_command(module.COMMAND_NAME, module.PowerCommand())
            elif hasattr(module, "COMMAND_NAME") and hasattr(module, "SquareCommand"):
                invoker.register_command(module.COMMAND_NAME, module.SquareCommand())
            else:
                logger.warning("Skipping unknown plugin: %s", module_name)

            logger.info("Loaded plugin: %s", module.COMMAND_NAME)

        except ImportError as e:
            logger.error("Failed to load plugin %s: %s", module_name, e)
