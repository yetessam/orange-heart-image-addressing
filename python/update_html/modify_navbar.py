# Description: This script modifies the navigation bar to be compatible with Bulma CSS.
from bs4 import BeautifulSoup
import os

from update_html.logging_ohp import logger

# Adding attribution 
def update_attribute(element, att_name, att_value):
    att = element.get(att_name, [])
    if att_value not in att:
        element[att_name] = att + [att_value]


def remove_attribute_value(element, att_name, att_value):
    att = element.get(att_name, [])
    if att_value in att:
        att.remove(att_value)
        element[att_name] = att

# Function to recursively set classes for nested menu items in a depth-first manner
def set_navbar_classes(soup, list_element):
    """
    Updates the classes of navbar items and dropdowns in the given list element.
    This function performs the following tasks:
    1. Iterates through all <li> elements within the list_element to:
       - Add the 'navbar-item' class to <a> tags.
       - Remove the 'is-link' class from <a> tags.
       - Unwrap <li> tags that contain a single <a> tag.
    2. Iterates through all <li> elements within the list_element again to:
       - Check if the <li> contains a nested <ul> (submenu).
       - If a submenu is found, update its class to 'navbar-dropdown' and change its tag to <div>.
       - Update the parent <li> to a <div> with the class 'navbar-item has-dropdown is-hoverable'.
    Args:
        soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
        list_element (Tag): The parent list element containing the navbar items.
    Returns:
        None
    """
    # Set all the nav-bar items first 
    for li in list_element.find_all('li', recursive=True):
        a = li.find('a')
        if a:
            update_attribute(a, 'class', 'navbar-item')
            remove_attribute_value(a, 'class', 'is-link')
            # Bulma doesn't expect the list item, so remove it if its a simple menu item
            # without any submenus
            if (len(list(li.children)) == 1):
                li.unwrap() 

    
    for li in list_element.find_all('li', recursive=True):
        # Check if the list item contains a nested list
        has_dropdown = False
        for submenu in li.find_all('ul', recursive=False):
            if submenu:
                has_dropdown = True
                dropdown_a = li.find('a')       
                if (dropdown_a):
                    submenu.name = 'div'
                    submenu['class'] = 'navbar-dropdown is-hoverable'
                    
        if (has_dropdown):
             li.name = 'div'
             update_attribute(li, 'class', 'navbar-item has-dropdown is-hoverable')
             remove_attribute_value(li, 'class', 'list-item')
                
                         
                
                
 # Handle navigation and update the navbar for Bulma Responsive CSS
def modify_navbar(soup,  filepath=None, root_dir=None):
   
    nav = soup.find('nav')
    if nav:

        # Check if the nav has already been modified
        if nav.get('id') == 'navbar-bulma':
            logger.debug("Navbar already modified. Skipping.")
            return soup
        
        nav['class'] = 'navbar is-spaced'
        nav['role'] = 'navigation'
        nav['aria-label'] = 'main navigation'
        print("Applied Bulma classes to <nav> tag.")

        # Create new navbar brand div for logo or brand name (if needed)
        navbar_brand = soup.new_tag('div', **{'class': 'navbar-brand'})
       
        # Create and add the hamburger menu
        navbar_burger = soup.new_tag('a', **{
            'role': 'button',
            'class': 'navbar-burger is-boxed',
            'aria-label': 'menu',
            'aria-expanded': 'false',
            'data-target': 'navbarBasicExample'
        })
        for _ in range(3):
            navbar_burger.append(soup.new_tag('span', **{'aria-hidden': 'true'}))
        navbar_brand.append(navbar_burger)

        # Create new navbar menu div
        navbar_menu = soup.new_tag('div', **{'class': 'navbar-menu', 'id': 'navbarBasicExample'})
        #navbar_start = soup.new_tag('div', **{'class': 'navbar-start'})
        navbar_end = soup.new_tag('div', **{'class': 'navbar-end'})

        # Move list items to the new structure
        navbar_start = nav.find('ul')
        if navbar_start:
            navbar_start.name = 'div'
            navbar_start['class'] = 'navbar-start'
            set_navbar_classes(soup, navbar_start)
            logger.debug("Reorganized <nav> structure with Bulma classes.")

        
        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        navbar_menu.append(navbar_end)
        nav.clear()
        nav.append(navbar_brand)
        nav.append(navbar_menu)
        
        # Add javascript for Bulma
         # Calculate relative path to root
        js_path = 'Missing JS path'
        if filepath and root_dir:
            from pathlib import Path
            current_dir = Path(filepath).parent
            relative_path = Path(os.path.relpath(root_dir, current_dir))
            js_path = relative_path / 'js' / 'navbar.js'
            logger.debug(f"JS path relative to {filepath}: {js_path}")

        script_tag = soup.new_tag('script', src=str(js_path), type='text/javascript')
        nav.insert_after(script_tag)

        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")

    return soup
