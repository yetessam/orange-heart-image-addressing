from pathlib import Path
from .common.utils import ( parse_arguments )
from .projectmanager import ProjectManager

import pkgutil, importlib
# Dynamically import all plugins 
plugins = {name: importlib.import_module(f".plugins.{name}", __package__).Plugin for _, name, _ in pkgutil.iter_modules(["./plugins"]) if name != "plugin"}


def main():
        
    args = parse_arguments()
    out_dir = args.out_dir # DITA OT output
    src_dir = args.src_dir # Processed HTML5 SRC, ready for deployment
    res_dir = args.res_dir # resources
    debug_mode = False      # 
        

    # Instantiate and initialize the ProjectManager
    project = ProjectManager(out_dir, src_dir, res_dir, debug_mode)
    project.initialize() # Project init creates temp directory 
    
    # Add plugins after project has been initialized since that's what sets up 
    # the logging and temp folders. 
    # Now, add as many plugs in as you want and pass through project level properties
    # Instatiate and initialize UIPlugin and pass through the logger and temp 
    
    # Order is significant as you need to build the navbar before addig the search box to it
    
    PLUGIN_MAPPING = {
       
        "ui": ("ui", "UIPlugin"),
        "navigation": ("navigation", "NavPlugin"),
         "search": ("search", "SearchPlugin"),
    }
    
    plugins = project.import_plugins(PLUGIN_MAPPING)
    
    for plugin in plugins:  # Initialize
        plugin.initialize()     # runs once on each plugin
    
    project.run()
    project.post_processing() 
    project.cleanup()
    

if __name__ == "__main__":
    
    main()