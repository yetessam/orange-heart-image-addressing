import os
import shutil

def copy_resource(resource_dir, src_dir, filename):
    source_file_path = os.path.join(resource_dir, filename)
    destination_dir = os.path.join(src_dir, "css")
    destination_file_path = os.path.join(destination_dir, filename)

    if not os.path.exists(source_file_path):
        print(f"File not found in resource directory: {source_file_path}")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created directory: {destination_dir}")

    shutil.copy2(source_file_path, destination_file_path)
    print(f"Copied {source_file_path} to {destination_file_path}")
