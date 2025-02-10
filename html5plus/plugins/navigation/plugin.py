from ..plugin import Plugin 
from pathlib import Path

from .modify_navbar import  modify_navbar

import logging
import sys

class NavPlugin(Plugin):
    """
        NavPlugin functionality:
            - Adding script tag to each HTML file 
            - Copying all NavPlugin/resources/js files over to src/js folder
            
    """
    def __init__(self, logger: logging.Logger, target: str):
        # Call the parent class's __init__
        super().__init__(logger, target)
        
        # Set up paths 
        
        self.pluginpath = Path(__file__).resolve().parent
        self.resources = self.pluginpath / "resources"
        self.resources_css = self.resources / "css"
          
     
            
    def initialize(self) -> None:  
        self.logger.info(f"NavPlugin initialized")
    
    
    def modify_navbar(self, html_content, HTMLP) -> str:
        # Call the imported function and pass the logger
        return modify_navbar(html_content, HTMLP)      
    
    def process(self, html_content: str, HTMLP ) -> str:
        """
        Process the HTML content.  
        HTMLProcessor Object level plugin code. 
        
        Args:
            html_content: The HTML content to process.
            HTMLP is the HTMLProcessor 
        Returns:
            The processed HTML content.
        """
        modified_string = self.modify_navbar(html_content, HTMLP)      
        return modified_string      
    
    def run(self):
        """This code once during the projects entire project flow."""
    
        try:
            # self.logger.info("NavPlugin project level execution ")     
            self.css_js_resources()
                
        except Exception as e:
            self.logger.error(f"NavPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("NavPlugin cleanup complete.")        