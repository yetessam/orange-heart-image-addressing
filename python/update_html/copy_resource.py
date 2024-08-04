import os
import shutil

from update_html.logging_ohp import logger

def copy_resource(source_dir, dest_dir, filename):
   source_file_path = os.path.join(source_dir, filename)
   destination_file_path = os.path.join(dest_dir, filename)

    if not os.path.exists(source_file_path):
        logger.info(f"File not found in resource directory: {source_file_path}")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        logger.info(f"Created directory: {dest_dir}")

    shutil.copy2(source_file_path, destination_file_path)
    logger.info(f"Copied {source_file_path} to {destination_file_path}")
