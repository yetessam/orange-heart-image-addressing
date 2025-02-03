from bs4 import BeautifulSoup
import os
from pathlib import Path

def modify_navbar(soup, filepath, root_dir, logger):
    nav = soup.find('nav')
    if nav:
        if nav.get('id') == 'navbar-bulma':
            logger.debug("Navbar already modified. Skipping.")
            return soup

        # Apply Bulma classes to the <nav> tag
        apply_navbar_classes(nav, logger)

        # Create and append the navbar brand with the hamburger menu
        navbar_brand = create_navbar_brand(soup)
        nav.append(navbar_brand)

        # Create and append the navbar menu structure
        navbar_menu = create_navbar_menu(soup, nav, logger)
        nav.append(navbar_menu)

        # Add JavaScript for Bulma
        add_bulma_script(soup, nav, filepath, root_dir, logger)

        # Mark the navbar as modified
        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")

    return soup


def apply_navbar_classes(nav, logger):
    """Apply Bulma classes to the <nav> tag."""
    nav['class'] = 'navbar is-spaced'
    nav['role'] = 'navigation'
    nav['aria-label'] = 'main navigation'
    logger.debug("Applied Bulma classes to <nav> tag.")


def create_navbar_brand(soup):
    """Create the navbar brand div with the hamburger menu."""
    navbar_brand = soup.new_tag('div', **{'class': 'navbar-brand'})

    # Define and parse the hamburger menu HTML
    hamburger_menu_html = """
    <a role="button" class="navbar-burger is-boxed" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
    </a>
    """
    hamburger_menu_soup = BeautifulSoup(hamburger_menu_html, 'html.parser')
    navbar_brand.append(hamburger_menu_soup)

    return navbar_brand


def create_navbar_menu(soup, nav, logger):
    """Create the navbar menu structure."""
    navbar_menu = soup.new_tag('div', **{'class': 'navbar-menu', 'id': 'navbarBasicExample'})

    # Move list items to the new structure
    navbar_start = nav.find('ul')
    if navbar_start:
        navbar_start.name = 'div'
        navbar_start['class'] = 'navbar-start'
        set_navbar_classes(soup, navbar_start)
        logger.debug("Reorganized <nav> structure with Bulma classes.")

    # Define and parse the navbar-end HTML
    navbar_end_html = """
    <div class="navbar-end">
        <!-- Search Box aligned to the right -->
        <div class="navbar-item">
            <!-- Search Box Widget -->
            <div id="search-box"></div>
        </div>
    </div>
    """
    navbar_end_soup = BeautifulSoup(navbar_end_html, 'html.parser')

    # Assemble the navbar menu structure
    navbar_menu.append(navbar_start)
    navbar_menu.append(navbar_end_soup)

    return navbar_menu


def add_bulma_script(soup, nav, filepath, root_dir, logger):
    """Add the Bulma JavaScript file to the HTML."""
    script = {
        "src": "js/navbar.js",
        "type": "text/javascript",
    }

    # Calculate the relative path to the JavaScript file
    if filepath and root_dir:
        current_dir = Path(filepath).parent
        relative_path = Path(os.path.relpath(root_dir, current_dir))
        script['src'] = str(relative_path / 'js' / 'navbar.js')

    # Create and append the script tag
    script_tag = soup.new_tag('script', **script)
    nav.insert_after(script_tag)
    logger.debug(f"Added Bulma script: {script['src']}")


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
            if len(list(li.children)) == 1:
                li.unwrap()

    for li in list_element.find_all('li', recursive=True):
        # Check if the list item contains a nested list
        has_dropdown = False
        for submenu in li.find_all('ul', recursive=False):
            if submenu:
                has_dropdown = True
                dropdown_a = li.find('a')
                if dropdown_a:
                    submenu.name = 'div'
                    submenu['class'] = 'navbar-dropdown is-hoverable'

        if has_dropdown:
            li.name = 'div'
            update_attribute(li, 'class', 'navbar-item has-dropdown is-hoverable')
            remove_attribute_value(li, 'class', 'list-item')


def update_attribute(element, att_name, att_value):
    """Update an attribute of an element."""
    att = element.get(att_name, [])
    if att_value not in att:
        element[att_name] = att + [att_value]


def remove_attribute_value(element, att_name, att_value):
    """Remove a specific value from an attribute of an element."""
    att = element.get(att_name, [])
    if att_value in att:
        att.remove(att_value)
        element[att_name] = att