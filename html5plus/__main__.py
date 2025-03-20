from pathlib import Path
from typing import Dict, Tuple
import pkgutil
import importlib
import logging
from .common.utils import parse_arguments
from .projectmanager import ProjectManager


# Dynamically import all plugins
plugins = {
    name: importlib.import_module(f".plugins.{name}", __package__).Plugin
    for _, name, _ in pkgutil.iter_modules(["./plugins"])
    if name != "plugin"
}

def main():
    # Parse command-line arguments
    args = parse_arguments()
    out_dir = args.out_dir  # DITA OT output
    src_dir = args.src_dir  # Processed HTML5 SRC, ready for deployment
    res_dir = args.res_dir  # Resources
    debug_mode = getattr(args, "debug_mode", False)  # Default to False if not provided

    # Configure logging
    logging.basicConfig(level=logging.DEBUG if debug_mode else logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Instantiate and initialize the ProjectManager
        project = ProjectManager(out_dir, src_dir, res_dir, debug_mode)
        project.initialize()  # Project init creates temp directory

        # Plugin configuration
        PLUGIN_MAPPING: Dict[str, Tuple[str, str]] = {
            "ui": ("ui", "UIPlugin"),
            "navigation": ("navigation", "NavPlugin"),
            "familylinks": ("familylinks", "FamilyLinksPlugin"),
            "search": ("search", "SearchPlugin"),
            "modal": ("modal", "ModalPlugin"),
        }

        # Import and initialize plugins
        plugins = project.import_plugins(PLUGIN_MAPPING)
        for plugin in plugins:
            try:
                plugin.initialize()  # Initialize each plugin
            except Exception as e:
                logger.error(f"Failed to initialize plugin {plugin.__class__.__name__}: {e}")
                raise

        # Run the project
        project.run()
        project.post_processing()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
    finally:
        # Ensure cleanup runs even if an error occurs
        project.cleanup()

if __name__ == "__main__":
    main()