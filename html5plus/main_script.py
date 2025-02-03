import shutil
import sys
import os
import tempfile


from bs4 import BeautifulSoup


from .common.utils import ( copy_resources, copy_specific_resources, find_html_files, parse_arguments, setup_directories
)

from .common.logging_ohp import ( setup_logger, set_log_temp)                              
from .search.algolia_operations import ( 
    apply_algolia_verification_metatag, apply_algolia_scripts
)

from .update_html import (
    apply_bulma_classes, bulma_classes, create_picture_tags, create_responsive,
    copy_files, read_html_file, write_html_file, modify_navbar, update_head
)

def setup_temp(input_dir, logger):
    temp_dir = tempfile.mkdtemp()
    logger.info(f"Created temp directory: {temp_dir}\n\n")
    set_log_temp(temp_dir)  # Strip temp_dir from log messages
    
    try:
        # Copy entire directory structure
        shutil.copytree(input_dir, temp_dir, dirs_exist_ok=True)
        logger.debug(f"Copied contents from {input_dir} to {temp_dir}")
        return temp_dir
    
    except Exception as e:
        logger.error(f"Failed to copy files to temp directory: {e}")
        shutil.rmtree(temp_dir)
        raise   


def process_html_file(filepath, out_dir, logger):
    # Switch back to default format
    logger.info(f"\n\n Processing HTML file: {filepath}")
    
    content = read_html_file(filepath)
    soup = BeautifulSoup(content, 'html.parser')
    soup.prettify()
   
    # Passing through the filepath to improve error messages
    soup = update_head(soup)
    soup = create_picture_tags(soup, filepath,logger)
    soup = create_responsive(soup, filepath)

    soup = apply_bulma_classes(soup, logger)
    soup = modify_navbar(soup, filepath, out_dir, logger)
    
    # Yas:  we are using a temp directory for processing
    write_html_file(filepath, soup.prettify())
    


def process_html_files(out_dir, src_dir, res_dir, logger):
    logger.info(f"process_html_files to copy from out directory: {out_dir}, to src directory: {src_dir} with resources from {res_dir}")

    setup_directories(out_dir, src_dir,logger)

    html_files = find_html_files(out_dir)
    if not html_files:
        raise FileNotFoundError(f"No HTML files found in the {out_dir}. Exiting.")
    
    logger.debug(f"Found {len(html_files)} HTML files:")
    for filepath in html_files:
        print(filepath)
        if 'toc.html' in filepath:
            print(f"Leave toc.html alone: {filepath}")
            continue 
        process_html_file(filepath, out_dir, logger )

    copy_files(out_dir, src_dir)
    logger.info(f"Copied all files from {out_dir} to {src_dir}\n\n")
    
    # Copy resources directory that includes css and js folders

    shutil.copytree(res_dir, src_dir, dirs_exist_ok=True)
    # Need to calculate the path to the search's modules resources
    # Copy over the search's modules resources
    # shutil.copytree(res_dir, src_dir, dirs_exist_ok=True)


def main():
    args = parse_arguments()
    out_dir = args.out_dir
    src_dir = args.src_dir
    res_dir = args.res_dir
  
 
   
    # Global logger initialization
    logger = setup_logger(debug_mode=False)
 
 
    logger.info(f"PARAMETERS\n\n")
     
    logger.info(f"DOT html5 output   {out_dir}")
    logger.info(f"Python processed   {src_dir}")
    logger.info(f"Python resources   {res_dir}\n\n")
    
    try:
        temp_dir = setup_temp(out_dir, logger)
        process_html_files(temp_dir, src_dir, res_dir, logger)
        
    except Exception as e:
        logger.error(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
