import argparse
import os
import shutil
import tempfile

from .logging import set_log_temp 

def setup_temp(input_dir, logger):
   
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Could not find the directory: {input_dir}. Exiting.")
    
   
    temp_dir = tempfile.mkdtemp()
    logger.info(f"Created temp directory: {temp_dir}")
    set_log_temp(temp_dir)  # Strip temp_dir from log messages
    
    try:
        # Copy entire directory structure
        shutil.copytree(input_dir, temp_dir, dirs_exist_ok=True)
        logger.debug(f"Copied contents from {input_dir} to temp directory")
        return temp_dir
    
    except Exception as e:
        logger.error(f"Failed to copy files to temp directory: {e}")
        shutil.rmtree(temp_dir)
        raise   


def copy_specific_resources(source_dir, resource_type, target_dir):
    """
    Copy specific type of resources (e.g., css, js) from the source directory to the target directory.
    """
    resource_dir = os.path.join(source_dir, resource_type)

    # Check if the resource directory exists before copying
    if os.path.exists(resource_dir):
        shutil.copytree(resource_dir, os.path.join(target_dir, resource_type), dirs_exist_ok=True)


def copy_resources(source_dir, target_dir):
    """
    Copies resources from `source_dir` to `target_dir`. Ensures directories exist and files are copied.
    """
    # Ensure the destination directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy over the resources from the source directory (source_dir) to the target directory (target_dir)
    shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process HTML5 output to update with additional UI/responsive/linking features.")
    parser.add_argument("--out-dir", type=str, required=True, help="DITA OT output directory")
    parser.add_argument("--src-dir", type=str, required=True, help="Processed HTML5 source directory")
    parser.add_argument("--res-dir", type=str, required=False, help="Resources directory such as css or icons.")
    parser.add_argument("-d", "--debug-mode", action="store_true", default=False, help="Enable debug mode")
    return parser.parse_args()
