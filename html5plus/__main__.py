from pathlib import Path
from .common.utils import ( parse_arguments )
from .projectmanager import ProjectManager

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