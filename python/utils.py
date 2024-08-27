import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pass through the DITA OT output folder, the target src folder and the Python resources folder')
    parser.add_argument('--out_dir', type=str, required=True, help="DITA OT folder where the HTML files are build, normally called 'out'")
    parser.add_argument('--src_dir', type=str, required=True, help='After processing, this folder contains the Bulma-ready HTML.')
    parser.add_argument('--res_dir', type=str, required=True, help='This folder contains additional resource files such as css or icons.')
    return parser.parse_args()

def find_html_files(directory):
    """Find all HTML files in the given directory."""
    return [os.path.join(root, file) 
            for root, _, files in os.walk(directory) 
            for file in files if file.endswith('.html')]

def setup_directories(origin_dir, destination_dir):
    if not os.path.exists(origin_dir):
        raise FileNotFoundError(f"Could not find the directory: {origin_dir}. Exiting.")
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created destination directory: {destination_dir}")


