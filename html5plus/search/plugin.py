
from ..plugins.plugin import Plugin 
from pathlib import Path

import logging
import sys

class SearchPlugin(Plugin):
    
    """
        SearchPlugin functionality:
        1. Copying all SearchPlugin/resources/css files over to src/css folder 
        2. Creating import url statements for all the css files
            
    """
    
        
    def initialize(self) -> None:
        
        self.logger.info(f"SearchPlugin initialized with global stylesheet: {self.global_stylesheet}")

       
        
            
    def process(self, html_content: str, context: Dict[str, Any]) -> str:
        return html_content
    
    
    def run(self):
        """Run the entire project flow."""
    
        try:
            
            self.update_global_stylesheet() # add to custom.css
            self.copy_resources(self.target)
            self.cleanup()
         
        except Exception as e:
            self.logger.error(f"SearchPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("SearchPlugin cleanup complete.")
        
        