from bs4 import BeautifulSoup
import os
import shutil

# Directory containing the files to modify
out_dir = 'out'
src_dir = 'src'

print(f"Starting script. Source directory: {out_dir}, Destination directory: {src_dir}")

def update_head(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Create new meta tag
    meta_tag = soup.new_tag('meta')
    meta_tag.attrs['name'] = 'viewport'
    meta_tag.attrs['content'] = 'width=device-width, initial-scale=1.0'
    
    # Create new link tag
    link_tag = soup.new_tag('link')
    link_tag.attrs['rel'] = 'stylesheet'
    link_tag.attrs['href'] = 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css'
    
    # Find the head element
    head = soup.head
    
    # Insert meta tag right after the first title or meta charset if present
    if head.title:
        head.title.insert_after(meta_tag)
    else:
        charset_meta = head.find('meta', attrs={'charset': True})
        if charset_meta:
            charset_meta.insert_after(meta_tag)
        else:
            head.insert(0, meta_tag)
    
    # Append link tag before any existing script tags, or at the end of head if no scripts are present
    first_script = head.find('script')
    if first_script:
        first_script.insert_before(link_tag)
    else:
        head.append(link_tag)
    
    return str(soup)


# Create the src directory if it doesn't exist
if not os.path.exists(src_dir):
    os.makedirs(src_dir)
    

# Iterate over all files in the out directory
for filename in os.listdir(out_dir):
    filepath = os.path.join(out_dir, filename)
    
    if os.path.isfile(filepath) and filename.endswith('.html'):
        print(f"Processing HTML file: {filepath}")
        
        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the HTML content with BeautifulSoup
        modified_content = update_head(content)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Modified and saved HTML file: {filepath}")

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

# Copy all files and directories except *.css to src
copy_files(out_dir, src_dir)

