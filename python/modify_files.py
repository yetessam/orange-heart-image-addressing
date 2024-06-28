from bs4 import BeautifulSoup
import os
import shutil

# Directory containing the files to modify
out_dir = 'out'
src_dir = 'src'

print(f"Starting script. Source directory: {out_dir}, Destination directory: {src_dir}")

# Define the mapping of HTML elements to Bulma class attributes
bulma_classes = {
    'h1': 'title is-1',
    'h2': 'title is-2',
    'h3': 'title is-3',
    'p': 'content',
    'div': 'box',
    'a': 'button is-primary',
    'button': 'button is-link',
    'ul': 'list is-hoverable',
    'ol': 'list is-hoverable',
    'li': 'list-item'
}

def apply_bulma_classes(soup):
    for tag, class_attr in bulma_classes.items():
        for element in soup.find_all(tag):
            element['class'] = class_attr

    # Specific handling for navigation
    nav = soup.find('nav')
    if nav:
        nav['class'] = 'navbar'
        nav['role'] = 'navigation'
        nav['aria-label'] = 'main navigation'
        
        # Create new navbar menu div
        navbar_menu = soup.new_tag('div', **{'class': 'navbar-menu'})
        navbar_start = soup.new_tag('div', **{'class': 'navbar-start'})
        
        # Move list items to the new structure
        ul = nav.find('ul')
        if ul:
            for li in ul.find_all('li'):
                a = li.find('a')
                a['class'] = 'navbar-item'
                navbar_start.append(a)
        
        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        nav.clear()
        nav.append(navbar_menu)

    return soup

def update_head_and_body(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update the head section
    meta_tag = soup.new_tag('meta')
    meta_tag.attrs['name'] = 'viewport'
    meta_tag.attrs['content'] = 'width=device-width, initial-scale=1.0'
    
    head = soup.head
    
    if head.title:
        head.title.insert_after(meta_tag)
    else:
        charset_meta = head.find('meta', attrs={'charset': True})
        if charset_meta:
            charset_meta.insert_after(meta_tag)
        else:
            head.insert(0, meta_tag)
     
    print(f"Adding viewport meta tag to HTML file: {filepath}")
    # Certain content has to be inserted before script tags
    #first_script = head.find('script')
    #if first_script:
    #    first_script.insert_before(link_tag)
    #else:
    #    head.append(link_tag)
    
    # Update the body section
    soup = apply_bulma_classes(soup)
    
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
        
        # Parse and modify the HTML content with BeautifulSoup
        modified_content = update_head_and_body(content)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Modified and saved HTML file: {filepath}")

# Copy the file
def copy_files(src, dst):
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_files(s, d)
            else:
                shutil.copy2(s, d)
    else:
        shutil.copy2(src, dst)

# Define the paths to the source and destination files
source_file = os.path.join(out_dir, 'landing-page.html')
destination_file = os.path.join(out_dir, 'index.html')

# Problem with the landing page, clobber index.html with landing-page.html
# Check if the landing-page file exists
if os.path.exists(source_file):
    # Copy the file
    shutil.copy(source_file, destination_file)
    print(f"Copied {source_file} to {destination_file}")
else:
    print(f"Source file {source_file} does not exist.")


# Copy all files and directories to src
copy_files(out_dir, src_dir)
