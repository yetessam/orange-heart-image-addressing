from bs4 import BeautifulSoup

from ..common.logging_ohp import logger
from ..common.head_operations import  apply_meta_tag, add_script_tag

from ..search.algolia_operations import apply_algolia_verification_metatag, apply_algolia_scripts

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
    
    add_metatags = [apply_viewport_metatag, apply_algolia_verification_metatag]

    for update_function in add_metatags:
        soup = update_function(soup)
        
    add_scripts = [apply_algolia_scripts]

    for update_function in add_scripts:
        soup = update_function(soup)
        
    return soup

