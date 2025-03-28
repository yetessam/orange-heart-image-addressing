from ..plugin import Plugin 
from pathlib import Path
from bs4 import BeautifulSoup

from ...common.headoperations import add_script_tag 

import logging
import os
import sys


class ModalPlugin(Plugin):
    """
        ModalPlugin functionality:
            - Search for modal parent element and apply JS to child elements
            - Load JS for on-click behaviour
    """
    def __init__(self, logger: logging.Logger, target: str):
        # Call the parent class's __init__
        super().__init__(logger, target)
        
        # Set up paths 
        
        self.pluginpath = Path(__file__).resolve().parent
        self.resources = self.pluginpath / "resources"
        self.resources_css = self.resources / "css"
          
            
    def initialize(self) -> None:  
        self.logger.info(f"ModalPlugin initialized")
        
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
        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, "html.parser")
        comment = "Modal for Gallery"
        js_path = os.path.join(HTMLP.root_relative, 'js', 'modal.js') 
        script =  {"src": f"{js_path}"}
        
        soup =  add_script_tag(soup, script, comment)
        soup = self.modify_Modal(str(soup))
        
        return str(soup)      
 
    def run(self):
        """This code once during the projects entire project flow."""
    
        try:
            self.css_js_resources()
                
        except Exception as e:
            self.logger.error(f"ModalPlugin runtime exception: {e}")
            sys.exit(1)


    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        self.logger.info("ModalPlugin cleanup complete.")        
        
    

    def update_html(self, str_html):
        """
        Updates HTML
        
        Args:
            prevlink (str): The previous link as a string.
            nextlink (str): The next link as a string.
        
        Returns:
            str: The new HTML string.
        """
        return str_html 

    def make_modal(self, Gallery):
        """
        Extracts the figures from the  Gallery element
        - Set on-click behaviors on figures 
        
        Args:
            Gallery (bs4.element.Tag): The Gallery element
        
        
        """
        
        fnodes = Gallery.find('fig')
        for fnode in fnodes:
            if fnode:
                print ("found fig ")
                # Set on-click behavior     
                #fnode['onclick'] = "document.getElementById('modal').style.display='block';"
                fnode['id'] = "whatever"


    def modify_Modal(self,html_content):
        """
        Modifies the Modal div element in the provided HTML content.
        
        Args:
            html_content (str): The HTML content as a string.
        
        Returns:
            str: The modified HTML content as a string.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        Gallery = soup.find( "*", class_='gallery')
        
        if Gallery:
            pass 
            #self.make_modal(Gallery)  
            #level_html = self.create_level_html(prevlink, nextlink)
            #Modal.append(BeautifulSoup(level_html, 'html.parser'))
        
        return soup
        
        
    def getHTMLSnippet(self, prev_uri, prev_text, next_uri, next_text):
        
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