from bs4 import BeautifulSoup
from update_html.bulma_classes import bulma_classes

def apply_bulma_classes(soup):
    
    for tag, class_attr in bulma_classes.items():
        for element in soup.find_all(tag):
            if 'class' not in element.attrs:
                # If the element does not have a class attribute, add one
                element['class'] = [class_attr]
                print(f"Applied Bulma class '{class_attr}' to <{tag}> tag without existing classes.")
            elif class_attr not in element['class']:
                # If the element has a class attribute but does not contain the class_attr, add it
                element['class'].append(class_attr)
                print(f"Added Bulma class '{class_attr}' to existing classes of <{tag}> tag.")
            else:
                # If the element already has the class_attr, skip
                print(f"Skipped <{tag}> tag as it already contains the Bulma class '{class_attr}'.")

            
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

    
        # Add inline script after navbar
        script_content = """
        document.addEventListener('DOMContentLoaded', () => {
            const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
        
            if ($navbarBurgers.length > 0) {
                $navbarBurgers.forEach(el => {
                    el.addEventListener('click', () => {
                        const target = el.dataset.target;
                        const $target = document.getElementById(target);
        
                        el.classList.toggle('is-active');
                        $target.classList.toggle('is-active');
                    });
                });
            }
        });
        """
        script_tag = soup.new_tag('script', type='text/javascript')
        script_tag.string = script_content
        nav.insert_after(script_tag)
        print("Added Bulma inline script after <nav> tag.")


    return soup

