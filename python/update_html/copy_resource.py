import os
import shutil

from update_html.logging_ohp import logger

def copy_resource(source_dir, dest_dir, filename):
   source = os.path.join(source_dir, filename)
   destination = os.path.join(dest_dir, filename)

   if not os.path.exists(source):
      logger.error(f"File not found in resource directory: {source}")
      return

   if not os.path.exists(dest_dir):
      os.makedirs(dest_dir)
      logger.info(f"Created directory: {dest_dir}")

   shutil.copy2(source, destination)
   logger.info(f"Copied {source} to {destination}")
