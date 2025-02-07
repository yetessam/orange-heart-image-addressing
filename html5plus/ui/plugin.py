
from ..plugins.plugin import Plugin 
from pathlib import Path

import logging
import sys

class UIPlugin(Plugin):
    """
        UIPlugin functionality:
            - Adding import bulma.css statements to the custom.css
            - Copying all UIPlugin/resources/css files over to src/css folder
            
    """
    def __init__(self, logger: logging.Logger, target: str):
        # Call the parent class's __init__
        super().__init__(logger, target)
        
        # Set up paths 
        self.pluginpath = Path(__file__).resolve().parent
        self.resources = self.pluginpath / "resources"
        self.resources_css = self.resources / "css"
          
    def initialize(self) -> None:  
        self.logger.info(f"UIPlugin initialized with global stylesheet: {self.global_stylesheet}")
    
    
    def run(self):
        """Run the entire project flow."""
    
        try:
            
            self.update_global_stylesheet() 
            self.copy_resources(self.target)
            self.cleanup()
                
        except Exception as e:
            self.logger.error(f"UIPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("UIPlugin cleanup complete.")
        
        