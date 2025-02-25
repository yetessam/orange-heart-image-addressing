import os

from bs4 import BeautifulSoup
from ...htmlprocessor import HTMLProcessor
from ...common.headoperations import apply_meta_tag, add_script_tag 


def apply_algolia_verification_metatag(soup):
    """
        Applies the Algolia site verification meta tag to the soup object using the apply_meta_tag helper function.
    """
    return apply_meta_tag(soup, 'algolia-site-verification', '204AB1DCEC8BAEEF')


def apply_algolia_scripts(soup, HTMLP):
    """
        Adds the Algolia search scripts to the soup object using the add_script_tag helper function.
    
        If there's a problem with the integrity attribute value, the Search box will not be created at all.
        
        To Do:   can we check for whether an error is being thrown by Instant Search to indicate that there's a problem,
        right now it fails gracefully and quietly and there is an very generic sha512 token error in the Console log in Developer Tools.
    """

    # External CDN scripts
    scripts = [
        {   "src": "https://cdn.jsdelivr.net/npm/algoliasearch@4.10.3/dist/algoliasearch.umd.min.js" } ,
        { 
            "crossorigin": "anonymous",
            "referrerpolicy": "no-referrer",
            "src": "https://cdnjs.cloudflare.com/ajax/libs/instantsearch.js/4.75.5/instantsearch.production.min.js",  
            "integrity":"sha512-QWlXe/zpXfXKKHds/YEyrMtzcKNME8+pxry8swnOWgxg6VjwmnkeMOTqlRjNyKVoNKuMyPN5UN/kyZHWgcgUeg=="
            }
    ]
    # Local scripts 
   
    
    js_path = os.path.join(HTMLP.root_relative, 'js', 'search.js') 
    scripts.append(  {"src": f"{js_path}"})

    js_path = os.path.join(HTMLP.root_relative, 'js', 'algolia.js') 
    scripts.append({"src": f"{js_path}"})
    
    comments = [
        " InstantSearch.js Library ", 
        " Algolia Search library ", 
        " Algolia and InstantSearch setup ",
        " Dropdown functionality "]
      
     # Make the script tags for the Aloglia search    
    for script, comment in zip(scripts,comments):
        soup =  add_script_tag(soup, script, comment)
  
   
    script_html = """
    <!-- Initialize components once the DOM is ready -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize dropdown from search.js
        initializeDropdown();

        // Start Algolia search from algolia.js
    
        startSearch();  // This starts the search instance
    });
    </script> 
    
    """

    script_soup = BeautifulSoup(script_html, 'html.parser')
    soup.body.append(script_soup)
    
    return soup

