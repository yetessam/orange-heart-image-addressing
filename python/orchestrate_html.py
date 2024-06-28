from apply_bulma import apply_bulma_classes
from update_head import update_head
from file_operations import read_html_file, write_html_file, copy_files
import os
import sys
from bs4 import BeautifulSoup

# Directory containing the files to modify
out_dir = 'out'
src_dir = 'src'

def process_html_files():
    print(f"Starting script. Source directory: {out_dir}, Destination directory: {src_dir}")

    # Create the src directory if it doesn't exist
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print(f"Created destination directory: {src_dir}")

    # Create the out directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print(f"Created source directory: {out_dir}")

    # Check if there are HTML files to process
    if not any(fname.endswith('.html') for fname in os.listdir(out_dir)):
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
#            soup = apply_bulma_classes(soup)
            
            # Write the modified content back to the file
            write_html_file(filepath, soup.prettify())

            print(f"Modified and saved HTML file: {filepath}")

    # Define the paths to the source and destination files
    source_file = os.path.join(out_dir, 'landing-page.html')
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
    

