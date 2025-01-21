from bs4 import BeautifulSoup
from update_html.logging_ohp import logger


# Function to recursively set classes for nested menu items in a depth-first manner
def set_navbar_classes(list_element, max_depth, counter=0):
    if counter < max_depth:
        for li in list_element.find_all('li', recursive=False):
            # Check for nested ul or ol
            nested_list = li.find(['ul', 'ol'], recursive=False)
            if nested_list:
                set_navbar_classes(nested_list,  max_depth, counter + 1)
            a = li.find('a')
            if a:
                a['class'] = 'navbar-item'

# Rename elements
def rename_elements(node, tags_to_rename, new_tag_name):
    for tag in node.find_all(tags_to_rename):
        new_tag = node.new_tag(new_tag_name)
        new_tag.attrs = tag.attrs
        new_tag.extend(tag.contents)
        tag.replace_with(new_tag)
 # Handle navigation and update the navbar for Bulma Responsive CSS
def modify_navbar(soup):
   
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
            max_depth = 2 # Bulma navbar is up to 2 deep, only keep nodes at level 0 and level 1
            set_navbar_classes(ul, max_depth, 0 )
            # Rename the elements to divs 
            rename_elements(ul, ['ul', 'ol', 'li'], 'div')  
            navbar_start.append(ul);
            logger.debug("Reorganized <nav> structure with Bulma classes.")
            
             
        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        navbar_menu.append(navbar_end)
        nav.clear()
        nav.append(navbar_brand)
        nav.append(navbar_menu)
        
        # Add javascript for Bulma
        script_tag = soup.new_tag('script', src='js/navbar.js', type='text/javascript')
        nav.insert_after(script_tag)

        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")

    return soup
