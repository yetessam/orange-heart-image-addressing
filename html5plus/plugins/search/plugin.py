from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup

from .search import modify_navbar_search
from .algolia_operations import apply_algolia_verification_metatag, apply_algolia_scripts


import logging
import sys

class SearchPlugin(Plugin):
    """
        SearchPlugin functionality:
            - Adding import statements to the global CSS 
            - Copying all SearchPlugin/resources/css files over to src/css folder
            
    """
    def __init__(self, logger: logging.Logger, target: str):
        # Call the parent class's __init__
        super().__init__(logger, target)
        
        # Set up paths 
        self.pluginpath = Path(__file__).resolve().parent
        self.resources = self.pluginpath / "resources"
        self.resources_css = self.resources / "css"
        self.resources_js = self.resources / "js"
          
    def apply_algolia_scripts(self, soup: BeautifulSoup):
        return apply_algolia_scripts(soup)
           
    def apply_algolia_verification_metatag(self, soup: BeautifulSoup):
        return apply_algolia_verification_metatag(soup)
           
    def modify_navbar_search(self, soup: BeautifulSoup):
        return modify_navbar_search(soup)
    
    
    def initialize(self) -> None:  
        self.logger.info(f"SearchPlugin initialized")
    
     
    def process(self, html_content: str, HTMLP ) -> str:
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
        # Add verification meta so that the page will be recognized
        soup = apply_algolia_verification_metatag(soup)
        soup = apply_algolia_scripts(soup, HTMLP)
         
        soup = self.modify_navbar_search(soup) # update_html
        return str(soup)
    
    def run(self):
        """Run the entire project flow."""
    
        try:
            self.css_js_resources()
            
                
        except Exception as e:
            self.logger.error(f"SearchPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("SearchPlugin cleanup complete.")        