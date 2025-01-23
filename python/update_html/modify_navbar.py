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
    # Run through this routine twice, once just to set all of the navbar-item classes
    # and a second time to set the has-dropdown classes
    for li in list_element.find_all('li', recursive=True):
        a = li.find('a')
        if a:
            update_attribute(a, 'class', 'navbar-item')
            remove_attribute_value(a, 'class', 'is-link')
            # We know that the <a> tag is a navbar item, so we can remove the <li> tag
            if (len(list(li.children)) == 1):
                li.unwrap() # Remove the <li> tag if it contains a single menu item

    
    for li in list_element.find_all('li', recursive=True):
        # Check if the list item contains a nested list
        has_dropdown = False
        for submenu in li.find_all('ul', recursive=True):
            if submenu:
                has_dropdown = True
                update_attribute(li, 'class', 'has-dropdown')
                update_attribute(submenu, 'class', 'navbar-dropdown')
                remove_attribute_value(submenu, 'class', 'list')
                

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
        navbar_start = soup.new_tag('div', **{'class': 'navbar-start'})
        navbar_end = soup.new_tag('div', **{'class': 'navbar-end'})

        # Move list items to the new structure
        ul = nav.find('ul')
        if ul:
            set_navbar_classes(soup, ul)
            navbar_start.append(ul)
            logger.debug("Reorganized <nav> structure with Bulma classes.")

        
        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        navbar_menu.append(navbar_end)
        nav.clear()
        nav.append(navbar_brand)
        nav.append(navbar_menu)
        
        # Add javascript for Bulma
         # Calculate relative path to root
        if filepath and root_dir:
            from pathlib import Path
            current_dir = Path(filepath).parent
            relative_path = Path(os.path.relpath(root_dir, current_dir))
            js_path = relative_path / 'js' / 'navbar.js'
            logger.debug(f"JS path relative to {filepath}: {js_path}")
        else:
            js_path = '/js/navbar.js'

        script_tag = soup.new_tag('script', src='/js/navbar.js', type='text/javascript')
        nav.insert_after(script_tag)

        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")

    return soup
