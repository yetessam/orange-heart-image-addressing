from bs4 import BeautifulSoup

from ..common.logging import logger
from ..common.headoperations import  apply_meta_tag 



"""
    Following series of functions add metadata and script to the HTML document
"""

def apply_viewport_metatag(soup):
    return apply_meta_tag(soup, 'viewport', 'width=device-width, initial-scale=1.0')

    
def update_head(soup):
    """
    Updates the head section of an HTML document using specified update functions.
    
    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    - filepath (str): The path to the HTML file (for logging purposes).
    
    Returns:
    - soup (BeautifulSoup): The updated BeautifulSoup object.
    """
    
    add_metatags = [apply_viewport_metatag]

    for update_function in add_metatags:
        soup = update_function(soup)
        
    return soup

