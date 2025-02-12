from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup


import logging
import sys

class FamilyLinksPlugin(Plugin):
    """
        FamilyLinksPlugin functionality:
            - Minimize collection-type labels on each HTML file 
            - Apply Bulma and responsive styling to prev/next links
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
        return self.modify_familylinks(html_content)
          
 
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
        
    

    def create_level_html(self, prevlink, nextlink):
        """
        Creates a new HTML string with the previous and next links in a new layout.
        
        Args:
            prevlink (str): The previous link as a string.
            nextlink (str): The next link as a string.
        
        Returns:
            str: The new HTML string.
        """
        level_html = f"""
        <div class="level is-mobile pt-3 is-flex is-justify-content-space-between">
            <div class="level-left">
                {prevlink}
            </div>
            <div class="level-right">
                {nextlink}
            </div>
        </div>
        """
        return level_html

    def extract_links(self, familylinks):
        """
        Extracts the previous and next links from the familylinks div element and injects span elements for arrows.
        
        Args:
            familylinks (bs4.element.Tag): The familylinks div element.
        
        Returns:
            tuple: A tuple containing the previous and next links as strings.
        """
        prevlink = ""
        nextlink = ""
        
        pnode = familylinks.find('div', class_='previouslink')
        if pnode:
            alink = pnode.find('a')
            if alink:
                prevlink = alink
                prevlink.insert(0, BeautifulSoup('<span class="mr-2 translate-y-px">←</span>', 'html.parser'))
                prevlink = str(prevlink)
            pnode.decompose()
        
        nnode = familylinks.find('div', class_='nextlink')
        if nnode:
            alink = nnode.find('a')
            if alink:
                nextlink = alink
                nextlink.append(BeautifulSoup('<span class="ml-2 translate-y-px">→</span>', 'html.parser'))
                nextlink = str(nextlink)
            nnode.decompose()
        
        return prevlink, nextlink




    def modify_familylinks(self,html_content):
        """
        Modifies the familylinks div element in the provided HTML content.
        
        Args:
            html_content (str): The HTML content as a string.
        
        Returns:
            str: The modified HTML content as a string.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        familylinks = soup.find('div', class_='familylinks')
        
        if familylinks:
            prevlink, nextlink = self.extract_links(familylinks)
            level_html = self.create_level_html(prevlink, nextlink)
            familylinks.append(BeautifulSoup(level_html, 'html.parser'))
        
        return str(soup)
        
        
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