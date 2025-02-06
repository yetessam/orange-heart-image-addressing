from bs4 import BeautifulSoup

# Add the search box to the navbar
def modify_navbar_search(soup):
    nav = soup.find('nav')
    if nav:
        nav_id = nav.get('id')
        if nav_id == 'navbar-bulma':
            
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
 
            nav.append(navbar_end_soup)

            # Define and parse the navbar-end HTML
            dropdown_html = """
                <div id="dropdown-container" class="columns is-paddingless is-hidden test_color is-full">
                    <div id="dropdown-content" class="column  is-paddingless is-half-desktop is-half-widescreen is-pulled-right ml-auto">
                    <!-- Search results will be injected here by InstantSearch.js -->
                    <div id="hits" class="notification">
                        <!-- Close Button -->
                        <button id="close-results" class="delete is-small"></button>
                        <div id="hits"></div> <!-- Fixed the closing tag here -->
                    </div>
                    </div>
                    <div id="dropdown-footer">
                    <!-- Placeholder for footer, for refining search results or pagination-->
                    </div>
                </div>

"""
            dropdown_soup = BeautifulSoup(dropdown_html, 'html.parser')
            nav.insert_after(dropdown_soup)
            
    return soup
