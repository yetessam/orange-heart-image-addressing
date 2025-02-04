# html_processor_conductor.py
import os
from .htmlprocessor import HTMLFileProcessor


class HTMLProcessorConductor:
    """Responsible for managing and processing all HTML files in a directory."""

    def __init__(self, out_dir, logger, skip):
        self.out_dir = out_dir
        self.logger = logger
        self.skip = skip
    
    def initialize(self):
        
        self.logger.info( self.welcome_message())
     
        
    def find_html_files(self):
        """Find all HTML files in the given directory."""
        return [
            os.path.join(root, file)
            for root, _, files in os.walk(self.out_dir)
            for file in files if file.endswith('.html')
        ]

    def process(self):
        """Process all HTML files in the output directory."""
        self.initialize()
        
        try:
            # Find all HTML files in the output directory
            html_files = self.find_html_files()
            if not html_files:
                raise FileNotFoundError(f"No HTML files found to process.")

            # Process each HTML file
            for filepath in html_files:
                try:
                    # Skip files that are in the array
                    if os.path.basename(filepath) in self.skip:
                        self.logger.debug(f"Skipping file: {filepath}")
                        continue
                    # TO DO:  Calculate relative path to website root  
                    # compare filepath and self.out_dir and that will provide relative path
                    
                    # Process the HTML file
                    processor = HTMLFileProcessor(filepath, self.out_dir, self.logger)
                    processor.process()

                except Exception as e:
                    self.logger.error(f"Error processing file {filepath}: {e}")
                    raise # Reraise the exception
                    #continue  # Continue processing other files even if one fails

   
        except FileNotFoundError as e:
            self.logger.error(e)
            raise  # Re-raise the exception to stop further execution
        except Exception as e:
            self.logger.error(f"Unexpected error during HTML processing: {e}")
            raise  # Re-raise the exception to stop further execution
        
    def welcome_message(self):
        return "Conductor started processing all the files"