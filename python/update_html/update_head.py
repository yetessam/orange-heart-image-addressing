from bs4 import BeautifulSoup
from update_html.logging_ohp import logger

def apply_viewport_metatag(soup):
    """
    Applies the viewport meta tag to the soup object.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object.
    """
    viewport_meta = soup.find('meta', attrs={'name': 'viewport'})
    if viewport_meta:
        # Update the existing viewport meta tag
        viewport_meta['content'] = 'width=device-width, initial-scale=1.0'
    else:
        # Create a new viewport meta tag if it doesn't exist
        meta_tag = soup.new_tag('meta', attrs={
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        })
        
        head = soup.head
        if head:
            # Find all meta tags in the head
            meta_tags = head.find_all('meta')
            if meta_tags:
                # Append the new meta tag after the last existing meta tag
                last_meta = meta_tags[-1]
                last_meta.insert_after(meta_tag)
            else:
                # Append the new meta tag to the head if no other meta tags exist
                head.append(meta_tag)
    
    return soup
    
def update_head(soup, filepath):
    """
    Updates the head section of an HTML document using specified update functions.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    - filepath (str): The path to the HTML file (for logging purposes).
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object.
    """
    
    # List of update functions
    update_functions = [apply_viewport_metatag]

    for update_function in update_functions:
        soup = update_function(soup)
        logger.info(f"Applied {update_function.__name__} to {filepath}")
    
    return soup

