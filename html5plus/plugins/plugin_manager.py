# Written by Deep Seek -- no changes
class PluginManager:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.plugins = {}

    def register(self, name: str, plugin_class: Type[Plugin]) -> None:
        """Register a plugin class by name."""
        if name in self.plugins:
            raise ValueError(f"Plugin '{name}' is already registered.")
        self.plugins[name] = plugin_class

    def load_plugins_from_directory(self, directory: str) -> None:
        """Load plugins from a local directory."""
        plugin_dir = Path(directory)
        for module_path in plugin_dir.glob("*/plugin.py"):
            module_name = module_path.parent.name
            try:
                module = importlib.import_module(f"{module_name}.plugin")
                self.register(module_name, module.Plugin)
                self.logger.info(f"Loaded plugin: {module_name}")
            except Exception as e:
                self.logger.error(f"Failed to load plugin {module_name}: {e}")

    def initialize_plugin(self, name: str, config: Dict[str, Any]) -> Plugin:
        """Initialize a plugin by name."""
        if name not in self.plugins:
            raise ValueError(f"Plugin '{name}' not found.")
        plugin = self.plugins[name](self.logger)
        try:
            plugin.initialize(config)
            self.logger.info(f"Initialized plugin: {name}")
        except Exception as e:
            self.logger.error(f"Failed to initialize plugin {name}: {e}")
        return plugin

    def process_with_plugin(self, plugin: Plugin, html_content: str, context: Dict[str, Any]) -> str:
        """Process HTML content using a plugin."""
        try:
            return plugin.process(html_content, context)
        except Exception as e:
            self.logger.error(f"Plugin {plugin.__class__.__name__} failed: {e}")
            return html_content  # Continue with unmodified content

    def cleanup_plugin(self, plugin: Plugin) -> None:
        """Clean up a plugin."""
        try:
            plugin.cleanup()
            self.logger.info(f"Cleaned up plugin: {plugin.__class__.__name__}")
        except Exception as e:
            self.logger.error(f"Failed to clean up plugin {plugin.__class__.__name__}: {e}")