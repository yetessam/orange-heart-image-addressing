# Written by Deep Seek and a human

from abc import ABC, abstractmethod
from typing import Any, Dict
from pathlib import Path
import logging
import shutil

class Plugin(ABC):
    """Base class for all plugins."""

    def __init__(self, logger: logging.Logger, target: str):
        self.logger = logger
        self.pluginpath = None 
        self.target = target 
        self.global_stylesheet =  f"{self.target}/css/styles.css"  # default DITA OT path
        self.resources = None
        self.resources_css = None
        
        

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the plugin with the given configuration.
        
        Args:
            config: A dictionary containing configuration parameters for the plugin.
        """
        pass
    
    def copy_resources(self, target):
        # resource is a folder inside the plugin 
        shutil.copytree(
            self.resources,
            target, 
            dirs_exist_ok=True
        )
            
           
     
    def process(self, html_content, parent ):
        """
        Process the HTML content.  
        HTMLProcessor Object level plugin code. 
        
        Args:
            html_content: The HTML content to process.
            # removed the context param for now.. it was a dictionary containing shared resources or state.
        
        Returns:
            The processed HTML content.
        """
        return html_content
   
   
    def css_js_resources(self):
        """Prep and copy plugin resources."""
        self.copy_resources(self.target)
        self.update_global_stylesheet()  
         
     
    @abstractmethod
    def run(self):
        """Run the project-level flow."""
    
        pass 
    
    def add_cdn_stylesheet(self, URI):
        """
        Update the global stylesheet by adding an import statements for a CDN CSS
         
        """
        
        logger = self.logger 
        
        try:
            
            if not Path(self.global_stylesheet).exists():
                raise FileNotFoundError(f"Global stylesheet not found: {self.global_stylesheet}")
            
            with open(self.global_stylesheet, "r") as file:
                content = file.read()
           
                import_string = f'@import url("{URI}"); /* Imported by {type(self)} */\n'
                if import_string not in content:
                    with open(self.global_stylesheet, "w") as file:
                        file.write(import_string + content)
                    logger.info(f"Updated global stylesheet with reference to CDN: {URI}")
                else:
                    logger.info(f"Global stylesheet already contains reference to CDN: {URI}")

        except Exception as e:
            logger.error(f"Failed to update global stylesheet with CDN: {e}")
             
    def update_global_stylesheet(self) -> None:
        """
        Update the global stylesheet by adding import statements for 
        each css file found in resources/css
         
        """
        
        logger = self.logger 
        
        try:
            
            if not Path(self.resources_css).exists():
                return
            
            if not Path(self.global_stylesheet).exists():
                raise FileNotFoundError(f"Global stylesheet not found: {self.global_stylesheet}")
           
            with open(self.global_stylesheet, "r") as file:
                content = file.read()
            
            # Scan the resources/css directory for stylesheets
            stylesheets = [f.name for f in self.resources_css.iterdir() if f.is_file() and f.suffix == ".css"]

            for stylesheet in stylesheets:              

                import_string = f'@import url("{stylesheet}"); /* Imported by {type(self)} */\n'
                if import_string not in content:
                    with open(self.global_stylesheet, "w") as file:
                        file.write(import_string + content)
                    logger.info(f"Updated global stylesheet with import: {stylesheet}")
                else:
                    logger.info(f"Global stylesheet already contains import: {stylesheet}")

        except Exception as e:
            logger.error(f"Failed to update global stylesheet: {e}")
            
            
    @abstractmethod
    def cleanup(self) -> None:
        """
        Clean up resources used by the plugin.
        """
        pass
    
    
    
    