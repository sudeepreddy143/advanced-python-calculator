import os
import importlib

def load_plugins():
    plugins = {}
    plugin_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugin_files:
        module = importlib.import_module(f"app.plugins.{plugin}")
        if hasattr(module, "register"):
            plugins.update(module.register())

    return plugins
