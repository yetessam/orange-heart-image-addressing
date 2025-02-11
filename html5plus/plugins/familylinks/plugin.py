from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup


import logging
import sys

class FamilyLinksPlugin(Plugin):
    """
        FamilyLinksPlugin functionality:
            - Minimize collection-type labels on each HTML file 
            - Apply Bulma styling
    """
    def __init__(self, logger: logging.Logger, target: str):
        # Call the parent class's __init__
        super().__init__(logger, target)
        
        # Set up paths 
        
        self.pluginpath = Path(__file__).resolve().parent
           
     
            
    def initialize(self) -> None:  
        self.logger.info(f"FamilyLinksPlugin initialized")
    
      
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
        # Keep the a tags and add more divs to family links
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the parent topic
        familylink = soup.find('div', class_='familylinks')
        prev_uri = "test"
        prev_text = "test"
        next_uri = "test"
        next_text = "test"
        banner_text = self.getBanner(prev_uri, prev_text, next_uri, next_text)
        return str(soup)     
    
    def run(self):
        """This code once during the projects entire project flow."""
    
        try:
            #self.logger.info("FamilyLinksPlugin project level execution ")     
            pass
                
        except Exception as e:
            self.logger.error(f"FamilyLinksPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("FamilyLinksPlugin cleanup complete.")        
        
        
        
    def getBanner(self, prev_uri, prev_text, next_uri, next_text):
        
        return f"""
                <div class="is-fixed-bottom has-background-light py-4">
                    <div class="container is-flex is-justify-content-space-between">
                        <!-- Previous Link -->
                        <div class="has-text-left">
                            <a href="{prev_uri}" class="has-text-weight-bold">
                               {prev_text}
                            </a>
                            <div class="is-size-7 has-text-grey">
                                Previous
                            </div>
                        </div>

                       
                        <div class="has-text-right">
                            <a href="{next_uri}" class="has-text-weight-bold">
                               {next_text}
                            </a>
                            <div class="is-size-7 has-text-grey">
                                Next
                            </div>
                        </div>
                    </div>
                </div>
        """            