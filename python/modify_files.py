# modify_files.py, written by ChatGPT
from bs4 import BeautifulSoup
import os
import shutil

# Directory containing the files to modify
out_dir = 'out'
src_dir = '../src'

# Create the src directory if it doesn't exist
if not os.path.exists(src_dir):
    os.makedirs(src_dir)

# Iterate over all files in the out directory
for filename in os.listdir(out_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(out_dir, filename)
        
        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the HTML content with Beautiful Soup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Make modifications to the HTML content
        # For example, adding a new paragraph
        new_paragraph = soup.new_tag('p')
        new_paragraph.string = "This is an awesome new paragraph added by Beautiful Soup."
        soup.body.append(new_paragraph)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

# Copy all files except *.css to ../src
for filename in os.listdir(out_dir):
    if not filename.endswith('.css'):
        source_path = os.path.join(out_dir, filename)
        destination_path = os.path.join(src_dir, filename)
        shutil.copy2(source_path, destination_path)
