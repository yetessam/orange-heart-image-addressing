from update_html.bulma_classes import bulma_classes
from update_html.apply_bulma import apply_bulma_classes
from update_html.modify_navbar import modify_navbar

from update_html.file_operations import read_html_file, write_html_file, copy_files
from update_html.update_head import update_head
from update_html.create_pictures import create_picture_tags

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

def find_html_files(out_dir):
    html_files = []
    for root, dirs, files in os.walk(out_dir):
        for fname in files:
            if fname.endswith('.html'):
                html_files.append(os.path.join(root, fname))
    return html_files

def process_html_files():
    print(f"Starting script. Source directory: {out_dir}, Destination directory: {src_dir}")

    # Create the out directory if it doesn't exist
    if not os.path.exists(out_dir):
        raise FileNotFoundError(f"Could not find the html 5 out directory: {out_dir}. Exiting.")

    # Create the src directory if it doesn't exist
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print(f"Created destination directory: {src_dir}")


    # Check if any .html files exist in the directory and its subdirectories
    # Find all .html files
    html_files = find_html_files(out_dir)

    if not html_files:
        raise FileNotFoundError(f"No HTML files found in the {out_dir}. Exiting.")
    else:
        print(f"Found {len(html_files)} HTML files:")

        for filepath in html_files:
            print(" ")
            print(filepath)

            # Read the HTML content from the file
            content = read_html_file(filepath)

            # Parse and modify the HTML content with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            # Pretty print fron the start to make debugging easier
            soup.prettify()

            soup = update_head(soup, filepath)
            soup = create_picture_tags(soup, filepath)
            soup = apply_bulma_classes(soup)
            soup = modify_navbar(soup)
            
            
            # Write the modified content back to the file
            write_html_file(filepath, soup.prettify())

            print(f"Modified and saved HTML file: {filepath}")
        
            
        # Problem with the landing page, clobber index.html with landing-page.html
        # Check if the landing-page file exists
        # Define the paths to the source and destination files
        #source_file = os.path.join(out_dir, 'en/topics/landing-page.html')
        #destination_file = os.path.join(out_dir, 'en/topics/index.html')

        #if os.path.exists(source_file):
            # Copy the file
        #    copy_files(source_file, destination_file)
        #    print(f"Copied {source_file} to {destination_file}")
        #else:
        #    print(f"Could not find a landing page to copy over to index.html {source_file} does not exist.")

        # Copy all files and directories to src
        copy_files(out_dir, src_dir)
        print(f"Copied all files from {out_dir} to {src_dir}")

if __name__ == "__main__":
    try:
        process_html_files()
    except Exception as e:
        print(e)
        sys.exit(1)
    

