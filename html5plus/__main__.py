import shutil
import sys


from pathlib import Path

from .common.utils import ( parse_arguments, setup_directories, setup_temp )
from .common.logging import ( initialize_logger )                             
from .common.fileoperations import ( copy_files )                             

from .htmlprocessorconductor import ( HTMLProcessorConductor )


class ProjectManager:
    def __init__(self, out_dir, src_dir, res_dir):
        self.out_dir = out_dir
        self.src_dir = src_dir
        self.res_dir = res_dir
        
        self.logger = None
        self.project_root = None 
        self.resources = [] 
        self.skip = None
        self.temp_dir = None
       
    def initialize(self):
        
        self.logger = initialize_logger()
        self.logger.info( self.welcome_message())
        self.temp_dir = setup_temp(self.out_dir, self.logger) 
        self.project_root = Path(__file__).resolve().parent
        self.skip = ["toc.html"] # files to skip over
      
        # Set up resources 
        if (Path(self.res_dir).exists()):
            self.resources.append(self.res_dir)
        elif Path(self.project_root/ self.res_dir).exists():
            self.resources.append(self.project_root/ self.res_dir)
               
       # Store pointers to submodule resources
        for feature_name in ["navigation", "search", "ui"]:
            resource_path = self.project_root / feature_name / "resources"
            if Path(resource_path).exists():
                self.resources.append(resource_path)
            else:
                self.logger.warning(f"Resource path {resource_path} does not exist.")

    
    def post_processing(self):
            
        self.logger.info("Post processing started ")
        self.logger.info(f"Copying files (including resources) to {self.src_dir}")
        
        copy_files(self.temp_dir, self.src_dir)
    
        for resource in self.resources:
            self.logger.info(f"Resource {resource} ")
        
            shutil.copytree(
                resource,
                self.src_dir, 
                dirs_exist_ok=True
            )


    def run(self):
        """Run the entire project flow."""
    
        try:
            self.initialize()
            setup_directories(self.out_dir, self.src_dir,self.logger)

            conductor = HTMLProcessorConductor(self.out_dir,self.logger, self.skip)
            conductor.process()
           
            self.post_processing()
            self.logger.info("Project completed successfully.")
            
        except Exception as e:
            self.logger.error(f"Project failed: {e}")
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

 


def main():
        
    args = parse_arguments()
    out_dir = args.out_dir # DITA OT output
    src_dir = args.src_dir # Processed HTML5 SRC, ready for deployment
    res_dir = args.res_dir # resources

    # Initialize the ProjectManager
    project = ProjectManager(out_dir, src_dir, res_dir)
    
    # Run the project
    project.run()

if __name__ == "__main__":
    main()
