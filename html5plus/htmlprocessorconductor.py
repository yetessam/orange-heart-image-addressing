# html_processor_conductor.py
import os
from .htmlprocessor import HTMLProcessor

from .common.fileoperations import get_relative_path

class HTMLProcessorConductor:
    """Responsible for managing and processing all HTML files in a directory."""

    def __init__(self, directory, logger, plugins):
        self.directory = directory
        self.logger = logger
        self.plugins = plugins
        
    
    def initialize(self):
        
        self.logger.info( self.welcome_message())
        self.skip = ["toc.html"] # files to skip over during processing
        
    def find_html_files(self):
        """Find all HTML files in the given directory."""
        return [
            os.path.join(root, file)
            for root, _, files in os.walk(self.directory)
            for file in files if file.endswith('.html')
        ]

    def process(self):
        """Process all HTML files in directory."""
        try:
            # Find all HTML files in the output directory
            html_files = self.find_html_files()
            if not html_files:
                raise FileNotFoundError(f"No HTML files found to process.")

            # Process each HTML file
            counter = 1 
            for filepath in html_files:
                try:
                    # Skip files that are in the array
                    if os.path.basename(filepath) in self.skip:
                        self.logger.debug(f"Skipping file: {filepath}")
                        continue
                    
                    # root_relative is the path to base dir for the current file
                    root_relative = get_relative_path(filepath, self.directory)
                    self.logger.debug(f"Filepath: {filepath}")
                    self.logger.debug(f"Base: {self.directory}")
                    self.logger.debug(f"Relative path: {root_relative}")
                     
                    # Process the HTML file
                    processor = HTMLProcessor(filepath,  root_relative, self.logger, self.plugins)
                    processor.process()
                    counter = counter + 1 

                except Exception as e:
                    self.logger.info(f"Error processing file {filepath}: {e}")
                    #raise # Reraise the exception
                    self.logger.info(f"Continuing HTML processing on the remaining files.")
                    continue  # Continue processing other files even if one fails
            self.logger.info(f"Completed processing {counter} html files")
   
        except FileNotFoundError as e:
            self.logger.error(e)
            raise  # Re-raise the exception to stop further execution
        except Exception as e:
            self.logger.error(f"Unexpected error during HTML processing: {e}")
            raise  # Re-raise the exception to stop further execution
        
    def welcome_message(self):
        return "Conductor started processing all the files"