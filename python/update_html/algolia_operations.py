from bs4 import BeautifulSoup
from update_html.logging_ohp import logger
from update_html.head_operations import apply_meta_tag, add_script_tag



def apply_algolia_verification_metatag(soup):
    """
        Applies the Algolia site verification meta tag to the soup object using the apply_meta_tag helper function.
    """
    return apply_meta_tag(soup, 'algolia-site-verification', '204AB1DCEC8BAEEF')


def apply_algolia_scripts(soup):
    """
        Adds the Algolia search scripts to the soup object using the add_script_tag helper function.
    """

     # External CDN scripts
    scripts = [
        {"src": "https://cdn.jsdelivr.net/npm/algoliasearch@4.10.3/dist/algoliasearch.umd.min.js"},
        {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/instantsearch.js/4.75.5/instantsearch.production.min.js",
            "integrity": "sha512-QWlXe/zpXfXKKHds/YEyrMtzcKNME8+pxry8swnOWgxg6VjwmnkeMOTqlRjNyKVoNKuMyPN5UN/kyZHWgcGUeg==",
            "crossorigin": "anonymous",
            "referrerpolicy": "no-referrer"
        }
    ]

    # Local scripts 
    scripts.append(  {"src": "js/search.js"})

     # Make the 3 script tags for the Aloglia search    
    for script in scripts:
        soup =  add_script_tag(soup, script)
   
    return soup

