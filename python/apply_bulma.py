from bs4 import BeautifulSoup
from bulma_classes import bulma_classes

def apply_bulma_classes(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for tag, class_attr in bulma_classes.items():
        for element in soup.find_all(tag):
            element['class'] = class_attr
            print(f"Applied Bulma class '{class_attr}' to <{tag}> tag.")

    # Specific handling for navigation
    nav = soup.find('nav')
    if nav:
        nav['class'] = 'navbar'
        nav['role'] = 'navigation'
        nav['aria-label'] = 'main navigation'
        print("Applied Bulma classes to <nav> tag.")

        # Create new navbar brand div for logo or brand name (if needed)
        navbar_brand = soup.new_tag('div', **{'class': 'navbar-brand'})
        nav.insert(0, navbar_brand)

        # Create and add the hamburger menu
        navbar_burger = soup.new_tag('a', **{
            'role': 'button',
            'class': 'navbar-burger',
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
            for li in ul.find_all('li'):
                a = li.find('a')
                a['class'] = 'navbar-item'
                navbar_start.append(a)
                print("Reorganized <nav> structure with Bulma classes.")

        # Assemble the new navbar structure
        navbar_menu.append(navbar_start)
        navbar_menu.append(navbar_end)
        nav.clear()
        nav.append(navbar_menu)

    return str(soup)

