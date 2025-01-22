from bs4 import BeautifulSoup
from update_html.logging_ohp import logger

# Adding attribution 
def update_attribute(element, att_name, att_value):
    att = element.get(att_name, [])
    if att_value not in att:
        element[att_name] = att + [att_value]


# Function to recursively set classes for nested menu items in a depth-first manner
def set_navbar_classes(soup, list_element):
    for li in list_element.find_all('li', recursive=True):
        a = li.find('a')
        if a:
            update_attribute(a, 'class', 'navbar-item')

    for ul in list_element.find_all('ul', recursive=True):
        if ul:
            update_attribute(ul, 'class', 'navbar-dropdown')
            update_attribute(ul.find_parent('li'), 'class', 'has-dropdown')
            # rename nested menu items to div
            new_tag = soup.new_tag("div")
            new_tag.attrs = ul.attrs
            new_tag.contents = ul.contents
            ul.replace_with(new_tag)


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
            set_navbar_classes(soup, ul);
            # remove the li element, Bulma CSS only needs div/a 
            for tag in ul.find_all('li'):
                tag.unwrap()

            
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
