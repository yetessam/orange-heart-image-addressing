from bs4 import BeautifulSoup

#  This module updates the meta tags in the HTML content 

def update_head(html_content, filepath):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update the head section
    meta_tag = soup.new_tag('meta', attrs={
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'
    })
    
    head = soup.head
    if head:
        if head.title:
            head.title.insert_after(meta_tag)
        else:
            charset_meta = head.find('meta', attrs={'charset': True})
            if charset_meta:
                charset_meta.insert_after(meta_tag)
            else:
                head.insert(0, meta_tag)
        print(f"Added viewport meta tag to {filepath}")
    
    return str(soup)

