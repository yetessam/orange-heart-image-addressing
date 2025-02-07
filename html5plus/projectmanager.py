import os 
import shutil
import sys

from pathlib import Path
from .common.utils import  setup_temp 
from .common.logging import  initialize_logger                              
from .common.fileoperations import copy_dir                              
from .htmlprocessorconductor import HTMLProcessorConductor 


class ProjectManager:
    def __init__(self, out_dir, src_dir, res_dir):
        
        self.out_dir = out_dir
        self.src_dir = src_dir
        self.res_dir = res_dir
        
        self.features = []
        self.logger = None
        self.html5pluspath = None 
        self.resources = [] 
        self.temp_dir = None
        self.global_custom_css = None 
         
        
    def initialize(self):
        # The following section sets up the processing for success 
        
        try: 
            # Output log welcome message to user
            self.logger = initialize_logger()
            self.logger.info( self.welcome_message())
        
        except Exception as e:
            print(f"Project initialization failed at logging: {e}")
            sys.exit(1)
        
        try:   
            # project path
            self.html5pluspath = Path(__file__).resolve().parent
        
            # Create target directory when it does not exist
            if not os.path.exists(self.src_dir):
                os.makedirs(self.src_dir)
            
         
            # Copy the output from the DITA OT to a temp folder 
            self.temp_dir = setup_temp(self.out_dir, self.logger) 
        
        except Exception as e:
            self.logger.error(f"Project Manager exception: {e}")
            sys.exit(1)
                   
    def post_processing(self):
        self.logger.info("Post processing started ")
        self.logger.info(f"Copying files (including resources) to {self.src_dir}")
        # Copy processed directory over to src
        copy_dir(self.temp_dir, self.src_dir)
    

    def run(self):
        """Run the entire project flow."""
    
        try:
            
            conductor = HTMLProcessorConductor(self.temp_dir, self.logger)
            conductor.process()
           
        except Exception as e:
            self.logger.error(f"ProjectManager run exception: {e}")
            sys.exit(1)


    def welcome_message(self):
        strMessage = f"""
        ########################################################
        
        Developer Log - html5plus project        
        
        ########################################################
        
        Project initialization started with the following parameters:
        
        DOT HTML5 Output Directory:        {self.out_dir}
        Processed HTML5 Source Directory:  {self.src_dir}
        Resource Directory:                {self.res_dir}
    """
        return strMessage

 

