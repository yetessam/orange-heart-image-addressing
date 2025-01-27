from bs4 import BeautifulSoup
from update_html.logging_ohp import logger

def apply_meta_tag(soup, name, content):
    """
    Applies a meta tag with a specified name and content to the soup object.
    If the meta tag already exists, it updates the content attribute. If not, it creates and inserts it.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    - name (str): The name attribute of the meta tag.
    - content (str): The content attribute of the meta tag.
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object with the applied meta tag.
    """
    # Look for an existing meta tag with the specified name
    meta_tag = soup.find('meta', attrs={'name': name})
    
    if meta_tag:
        # If the meta tag exists, update its content
        meta_tag['content'] = content
    else:
        # If the meta tag doesn't exist, create a new one
        meta_tag = soup.new_tag('meta', attrs={'name': name, 'content': content})
        
        # Find the <head> section
        head = soup.head
        if head:
            # Find all existing meta tags in the head
            meta_tags = head.find_all('meta')
            if meta_tags:
                # Insert the new meta tag after the last existing meta tag
                last_meta = meta_tags[-1]
                last_meta.insert_after(meta_tag)
            else:
                # If no meta tags exist, just append the new meta tag
                head.append(meta_tag)
    
    return soup


def add_script_tag(soup, script_attrs):
    """
    Adds a script tag with a specified src attribute to the soup object.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    - script_attrs (dict): A dictionary of attributes for the script tag.
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object with the added script tag.
    """
    # Create a new script tag
   
    script_tag = soup.new_tag('script', **script_attrs)
       
    
    # Find the <head> section
    head = soup.head
    if head:
        # Append the new script tag to the head
        head.append(script_tag)
    
    return soup