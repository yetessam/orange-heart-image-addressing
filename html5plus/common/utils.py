import argparse
import os
import shutil
import tempfile

from .logging import set_log_temp 

def setup_temp(input_dir, logger):
    
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
    parser = argparse.ArgumentParser(description='Pass through the DITA OT output folder, the target src folder and the Python resources folder')
    parser.add_argument('--out_dir', type=str, required=True, help="DITA OT folder where the HTML files are build, normally called 'out'")
    parser.add_argument('--src_dir', type=str, required=True, help='After processing, this folder contains the Bulma-ready HTML.')
    parser.add_argument('--res_dir', type=str, required=True, help='This folder contains additional resource files such as css or icons.')
    return parser.parse_args()


def setup_directories(origin_dir, destination_dir,logger):
    if not os.path.exists(origin_dir):
        raise FileNotFoundError(f"Could not find the directory: {origin_dir}. Exiting.")
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        logger.info(f"Created destination directory: {destination_dir}")


