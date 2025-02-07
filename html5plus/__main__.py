from pathlib import Path
from .common.utils import ( parse_arguments )
from .projectmanager import ProjectManager
from .ui.plugin import UIPlugin  

def main():
        
    args = parse_arguments()
    out_dir = args.out_dir # DITA OT output
    src_dir = args.src_dir # Processed HTML5 SRC, ready for deployment
    res_dir = args.res_dir # resources

    # Instantiate and initialize the ProjectManager
    project = ProjectManager(out_dir, src_dir, res_dir)
    project.initialize() # Project init creates temp directory 
    
    # Instatiate and initialize UIPlugin and pass through the logger
    ui_plugin = UIPlugin(project.logger, project.temp_dir)
    ui_plugin.initialize() # Code that runs once
     
 
    # Run the projects main code first
    project.run()
    
    # Run project-level plugin code       
    ui_plugin.run()
    
    # Now run post-processing after the plugins
    project.post_processing() # Move
    

if __name__ == "__main__":
    main()