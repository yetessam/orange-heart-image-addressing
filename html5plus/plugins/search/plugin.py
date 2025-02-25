from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup

from .search import insert_search_hits
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
        self.search_anchor = "navbarEnd" 
        
          
    def apply_algolia_scripts(self, soup: BeautifulSoup):
        return apply_algolia_scripts(soup)
           
    def apply_algolia_verification_metatag(self, soup: BeautifulSoup):
        return apply_algolia_verification_metatag(soup)
           
    def insert_search_hits(self, soup: BeautifulSoup, str_search_div):
        return insert_search_hits(soup, self.logger, str_search_div)
    
    
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
        soup = self.insert_search_hits(soup, self.search_anchor) 
        
        # Instant Search 
        self.add_cdn_stylesheet("https://cdn.jsdelivr.net/npm/instantsearch.css@8.5.1/themes/reset-min.css")
           
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