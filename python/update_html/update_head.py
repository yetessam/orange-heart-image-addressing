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


def apply_viewport_metatag(soup):
    """
    Applies the viewport meta tag to the soup object using the apply_meta_tag helper function.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object with the viewport meta tag.
    """
    return apply_meta_tag(soup, 'viewport', 'width=device-width, initial-scale=1.0')


def apply_algolia_verification_metatag(soup):
    """
    Applies the Algolia site verification meta tag to the soup object using the apply_meta_tag helper function.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object with the Algolia verification meta tag.
    """
    return apply_meta_tag(soup, 'algolia-site-verification', '204AB1DCEC8BAEEF')


def update_head(soup, filepath):
    """
    Updates the head section of an HTML document using specified update functions.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    - filepath (str): The path to the HTML file (for logging purposes).
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object.
    """
    
    # Always apply the viewport meta tag
    update_functions = [apply_viewport_metatag]

    # Conditionally add the Algolia verification meta tag if the file is 'index.html'
    if 'index.html' in filepath:
        update_functions.append(apply_algolia_verification_metatag)


    for update_function in update_functions:
        logger.info(f"Calling {update_function.__name__} to {filepath}")
        soup = update_function(soup)
        
    return soup

