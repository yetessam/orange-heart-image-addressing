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

            # Determine which features are loaded and get pointers to each
            # Order is significant as you must define the features prior to
            # copying over the resources
            self.features = ["navigation", "search", "ui"] 
            self.resources = self.setup_resources_array() 
            
            for resource in self.resources:
                self.logger.info(f"Resource {resource} ")
        
                shutil.copytree(
                    resource,
                    self.src_dir, 
                    dirs_exist_ok=True
                )
                
           
            # Copy the output from the DITA OT to a temp folder 
            self.temp_dir = setup_temp(self.out_dir, self.logger) 
        
        except Exception as e:
            self.logger.error(f"Project failed: {e}")
            sys.exit(1)
                   
    def post_processing(self):
        self.logger.info("Post processing started ")
        self.logger.info(f"Copying files (including resources) to {self.src_dir}")
        # Copy processed directory over to src
        copy_dir(self.temp_dir, self.src_dir)
    

    def run(self):
        """Run the entire project flow."""
    
        try:
            self.initialize()
            
            conductor = HTMLProcessorConductor(self.temp_dir, self.logger)
            conductor.process()
           
            self.post_processing()
            self.logger.info("Project completed successfully.")
            
        except Exception as e:
            self.logger.error(f"Project failed: {e}")
            sys.exit(1)


    def setup_resources_array(self):
        # Resources such as .js or images for the modified html5 output
        # 
        # Project level resources folder and each feature level resource folder need to be 
        # captured in the ProjectManager.that are global as well as feature
        # level resources, set these resources up in an array
        
        resources = []
        
        if (Path(self.res_dir).exists()):
            resources.append(self.res_dir)
        elif Path(self.html5pluspath/ self.res_dir).exists():
            resources.append(self.html5pluspath/ self.res_dir) 
                
        # Store pointers to submodule resources
        for feature in self.features:
            resource_path = self.html5pluspath / feature / "resources"
        if Path(resource_path).exists():
            resources.append(resource_path)
        else:
                self.logger.warning(f"Feature path {resource_path} does not exist.")

        return resources 
            
    
 
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

 

