from bs4 import BeautifulSoup

# Add the search box to the navbar
def insert_search_hits(soup, logger, str_search_div ):
    
    # parent tag for search box 
    if not str_search_div.startswith('#'):
        str_search_div = '#' + str_search_div 
    
    searchparent = soup.select_one(str_search_div)
    if searchparent:   
        searchbox =  soup.new_tag('div', **{'id': 'search-box'})   
        searchparent.append(searchbox)
        # define div for results
        dropdown_html = """
                <div id="dropdown-container" class="columns is-paddingless is-hidden is-full">
                    <div id="dropdown-content" class="column  is-paddingless is-half-desktop is-half-widescreen is-pulled-right ml-auto">
                        <!-- Search results will be injected here by InstantSearch.js -->
                        <div id="hits" class="notification">
                            <!-- Close Button -->
                            <button id="close-results" class="delete is-small"></button>
                        </div>
                    </div>
                    <div id="dropdown-footer">
                    <!-- Placeholder for footer, for refining search results or pagination-->
                    </div>
                </div> 
                """
        nav = soup.find('nav')
        if nav: 
            dropdown_soup = BeautifulSoup(dropdown_html, 'html.parser')
            nav.insert_after(dropdown_soup)
    
    else: 
        logger.info(f"Element with selector '{str_search_div}' not found in the soup.  HTML page is missing search div.")

    return soup 