# html_file_processor.py
from bs4 import BeautifulSoup
from .common.fileoperations import read_html_file, write_html_file


from .update_html import (
    create_picture_tags, create_responsive, update_head
)
     
class HTMLProcessor:
    """Responsible for processing a single HTML file."""

    def __init__(self, filepath, root_relative, logger, plugins):
        self.filepath = filepath
        self.logger = logger
        self.plugins = plugins 
        self.root_relative = root_relative 
        self.relativepath = None 
        
    def initialize(self):
        
         self.logger.info( self.welcome_message())
    

    def process(self):
        """Process the HTML file."""
        
        filepath = self.filepath
        logger = self.logger 

        try:
            # Read the HTML file
            content = read_html_file(filepath, logger)
            soup = BeautifulSoup(content, 'html.parser')
            soup.prettify()

            # Apply updates to the HTML
            
            soup = update_head(soup) # update_html
            soup = create_picture_tags(soup, filepath, logger)
            soup = create_responsive(soup, filepath, logger)
            
            content = str(soup)
            for plugin in self.plugins:  
                content = plugin.process(content, self)     # runs on each html instance
            
            soup = BeautifulSoup(content, 'html.parser')
          
            # Write the updated HTML back to the file
            write_html_file(self.filepath, soup.prettify())
           
        except Exception as e:
            self.logger.error(f"Error processing file {filepath}: {str(e)}")
            raise  # Re-raise the exception to handle it in the conductor 
        
    def post_processing(self):
        pass 
        
    def welcome_message(self):
        return f"Processing HTML file: {self.filepath}"
