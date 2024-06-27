# modify_files.py, written by Chat GPT
from bs4 import BeautifulSoup
import os

# Directory containing the files to modify
out_dir = 'out'

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
        new_paragraph.string = "This is a new paragraph added by Beautiful Soup."
        soup.body.append(new_paragraph)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
