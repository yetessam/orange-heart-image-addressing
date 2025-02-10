from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup

from .apply_bulma import apply_bulma_classes

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
          
    
    def apply_bulma_classes(self, soup: BeautifulSoup, logger: logging) -> BeautifulSoup:
        # Call the imported function and pass the logger
        return apply_bulma_classes(soup, self.logger)      
    
    def initialize(self) -> None:  
        self.logger.info(f"UIPlugin initialized")
    
     
    def process(self, html_content: str , HTMLP) -> str:
        """
        Process the HTML content.  
        HTMLProcessor Object level plugin code. 
        
        Args:
            html_content: The HTML content to process.
            # removed the context param for now.. it was a dictionary containing shared resources or state.
        
        Returns:
            The processed HTML content.
        """
        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, "html.parser")
        soup = self.apply_bulma_classes(soup, HTMLP.logger) # update_html
        return str(soup)
    
    def run(self):
        """Run the entire project flow."""
    
        try:
            self.logger.info("UIPlugin is running")  
            self.css_js_resources()
                
        except Exception as e:
            self.logger.error(f"UIPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("UIPlugin cleanup complete.")        