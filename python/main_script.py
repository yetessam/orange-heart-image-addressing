from update_html.bulma_classes import bulma_classes
from update_html.apply_bulma import apply_bulma_classes
from update_html.file_operations import read_html_file, write_html_file, copy_files
from update_html.update_head import update_head

import argparse
import os
import sys

from bs4 import BeautifulSoup




parser = argparse.ArgumentParser(description='Pass through the DITA OT output folder and the target src folder')

parser.add_argument('--out_dir', type=str, required=True, help="DITA OT folder where the HTML files are build, normally called 'out'")
parser.add_argument('--src_dir', type=str, required=True, help='After processing, this folder contains the Bulma-ready HTML.')

args = parser.parse_args()

out_dir = args.out_dir
src_dir = args.src_dir

print(f"Output directory: {out_dir}")
print(f"Web site source directory: {src_dir}")

def process_html_files():
    print(f"Starting script. Source directory: {out_dir}, Destination directory: {src_dir}")

    # Create the out directory if it doesn't exist
    if not os.path.exists(out_dir):
        raise FileNotFoundError(f"Could not find the html 5 out directory: {out_dir}. Exiting.")

    # Create the src directory if it doesn't exist
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print(f"Created destination directory: {src_dir}")

    
    # Check if there are HTML files to process
    # Recursive
    if not any(fname.endswith('.html') for fname in os.walk(out_dir)):
        raise FileNotFoundError(f"No HTML files found in the {out_dir}. Exiting.")

    # Iterate over all files in the out directory
    for filename in os.listdir(out_dir):
        filepath = os.path.join(out_dir, filename)
        
        if os.path.isfile(filepath) and filename.endswith('.html'):
            print(f"Processing HTML file: {filepath}")
            
            # Read the file content
            content = read_html_file(filepath)
            
            # Parse and modify the HTML content with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            soup = update_head(soup, filepath)
            soup = apply_bulma_classes(soup)
            
            # Write the modified content back to the file
            write_html_file(filepath, soup.prettify())

            print(f"Modified and saved HTML file: {filepath}")

    # Define the paths to the source and destination files
    source_file = os.path.join(out_dir, 'en/topics/landing-page.html=OFF')
    destination_file = os.path.join(out_dir, 'index.html')

    # Problem with the landing page, clobber index.html with landing-page.html
    # Check if the landing-page file exists
    if os.path.exists(source_file):
        # Copy the file
        copy_files(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")
    else:
        print(f"Source file {source_file} does not exist.")

    # Copy all files and directories to src
    copy_files(out_dir, src_dir)
    print(f"Copied all files from {out_dir} to {src_dir}")

if __name__ == "__main__":
    try:
        process_html_files()
    except Exception as e:
        print(e)
        sys.exit(1)
    

