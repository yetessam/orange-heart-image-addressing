from bs4 import BeautifulSoup
from update_html.logging_ohp import logger


# Function to recursively set classes for nested menu items in a depth-first manner
def set_navbar_classes(list_element):
    for li in list_element.find_all('li', recursive=False):
        # Check for nested ul or ol
        nested_list = li.find(['ul', 'ol'], recursive=False)
        if nested_list:
            set_navbar_classes(nested_list)
        a = li.find('a')
        if a:
            a['class'] = 'navbar-item'

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
            set_navbar_classes(ul);
        
            navbar_start.append(ul);
            logger.debug("Reorganized <nav> structure with Bulma classes.")

        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        navbar_menu.append(navbar_end)
        nav.clear()
        nav.append(navbar_brand)
        nav.append(navbar_menu)

        # Add inline script for Bulma navbar functionality
        script_content = """

      document.addEventListener('DOMContentLoaded', () => {
            const navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
            const targetMenu = document.getElementById('navbarBasicExample');

            const isDesktop = () => window.innerWidth >= 1024; // Adjust this breakpoint as needed

            const setInitialMenuState = () => {
                if (isDesktop() && localStorage.getItem('navbar-menu-state') === 'active') {
                    targetMenu.classList.add('is-active');
                    navbarBurgers.forEach(el => el.classList.add('is-active'));
                } else {
                    targetMenu.classList.remove('is-active');
                    navbarBurgers.forEach(el => el.classList.remove('is-active'));
                }
            };

            setInitialMenuState();

            // Add click event to toggle state
            navbarBurgers.forEach(el => {
                el.addEventListener('click', () => {
                    el.classList.toggle('is-active');
                    targetMenu.classList.toggle('is-active');

                    // Save the state to localStorage if on desktop
                    if (isDesktop()) {
                        if (targetMenu.classList.contains('is-active')) {
                            localStorage.setItem('navbar-menu-state', 'active');
                        } else {
                            localStorage.removeItem('navbar-menu-state');
                        }
                    }
                });
            });

            // Recheck the menu state on window resize
            window.addEventListener('resize', () => {
                setInitialMenuState();
            });
        });
  
        
        """
        script_tag = soup.new_tag('script', type='text/javascript')
        script_tag.string = script_content
        nav.insert_after(script_tag)

        nav['id'] = 'navbar-bulma'
        logger.info("Added Bulma inline script after <nav> with id='navbar-bulma'.")

    return soup
