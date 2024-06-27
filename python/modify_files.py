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
    filepath = os.path.join(out_dir, filename)
    
    if os.path.isfile(filepath) and filename.endswith('.html'):
        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the HTML content with Beautiful Soup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Make modifications to the HTML content
        # For example, adding a new paragraph
        new_paragraph = soup.new_tag('p')
        new_paragraph.string = "This is a new paragraph added by Beautiful Soup."
        soup.body.append(new_paragraph)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

# Function to copy files and directories excluding .css files
def copy_files(src, dst):
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_files(s, d)
            elif not s.endswith('.css'):
                shutil.copy2(s, d)
    elif not src.endswith('.css'):
        shutil.copy2(src, dst)

# Copy all files and directories except *.css to ../src
copy_files(out_dir, src_dir)
