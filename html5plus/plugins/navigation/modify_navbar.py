import os 
from bs4 import BeautifulSoup

def add_bulma_script(soup, nav, relative_path, logger):
    """Add the Bulma JavaScript file to the HTML."""
    jspath = "js/navbar.js"
        # Calculate the relative path to the JavaScript file
    if relative_path:
        jspath = os.path.join(relative_path, 'js', 'navbar.js')

    script = {
        "src": jspath,
        "type": "text/javascript",
    }



    # Create and append the script tag
    script_tag = soup.new_tag('script', **script)
    nav.insert_after(script_tag)
    logger.debug(f"Added Bulma script: {script['src']}")


def apply_navbar_classes(nav, logger):
    """Apply Bulma classes to the <nav> tag."""
    nav['class'] = 'navbar'
    nav['role'] = 'navigation'
    nav['aria-label'] = 'main navigation'
    logger.debug("Applied Bulma classes to <nav> tag.")


def create_navbar_brand(soup):
     
    """Create the navbar brand div with the hamburger menu."""
    navbar_brand = soup.new_tag('div', **{'class': 'navbar-brand'})



    # Define and parse the hamburger menu HTML
    hamburger_menu_html = """
    <a role="button" class="navbar-burger is-boxed" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
        <span aria-hidden="true"></span>
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
    navbar_menu = soup.new_tag('div', **{'class': 'navbar-menu', 'id': 'navbarMenu'})

    # Move list items to the new structure
    navbar_start = nav.find('ul')
    if navbar_start:
        navbar_start.name = 'div'
        navbar_start['class'] = 'navbar-start'
        navbar_start = set_navbar_classes(soup, navbar_start)
        logger.debug("Reorganized <nav> structure with Bulma classes.")

    # Assemble the navbar menu structure
    navbar_menu.append(navbar_start)

    return navbar_menu


def modify_navbar( html_content, HTMLP):
    
    filepath = HTMLP.filepath, 
    root_dir = HTMLP.root_relative

    logger = HTMLP.logger
    
    soup = BeautifulSoup(html_content, "html.parser")
    
    nav = soup.find('nav')
    
    if nav is None:
        logger.info(f"Expected an HTML <nav> element in {filepath}")
        logger.debug("Navbar not found. ")
        raise ValueError(f"Expected an HTML <nav> element in {filepath}.")
    
    if nav and nav.get('id') == 'navbar-bulma':
        logger.debug("Navbar already modified. Skipping.")
        return html_content

    try: 
          
        # Apply Bulma classes to the <nav> tag
        apply_navbar_classes(nav, logger)
        navbar_brand = create_navbar_brand(soup)
        nav.append(navbar_brand)

        # Create and append the navbar menu structure
        navbar_menu = create_navbar_menu(soup, nav, logger)
        nav.append(navbar_menu)

        
        navbar_brand = create_navbar_brand(soup)
        
        # Add JavaScript for Bulma
        add_bulma_script(soup, nav, root_dir, logger)

        # Mark the navbar as modified and avoid reprocessing
        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")
        
    except Exception as e:
        logger.error(f"Failed to modify navbar in {filepath}: {e}")
        raise ValueError(f"Failed to modify navbar in {filepath}: {e}") from e

    return str(soup)


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
        list_element 
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
            
    return list_element

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