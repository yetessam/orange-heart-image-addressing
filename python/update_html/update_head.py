from bs4 import BeautifulSoup

def update_head(soup, filepath):
    # Check if a viewport meta tag already exists
    viewport_meta = soup.find('meta', attrs={'name': 'viewport'})
    if viewport_meta:
        # Update the existing viewport meta tag
        viewport_meta['content'] = 'width=device-width, initial-scale=1.0'
        print(f"Updated viewport meta tag in {filepath}")
    else:
        # Create a new viewport meta tag if it doesn't exist
        meta_tag = soup.new_tag('meta', attrs={
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        })
        
        head = soup.head
        if head:
            # Find all meta tags in the head
            meta_tags = head.find_all('meta')
            if meta_tags:
                # Append the new meta tag after the last existing meta tag
                last_meta = meta_tags[-1]
                last_meta.insert_after(meta_tag)
            else:
                # Append the new meta tag to the head if no other meta tags exist
                head.append(meta_tag)
            
            print(f"Added viewport meta tag to {filepath}")
           
            # Create a new script tag
            new_script = soup.new_tag('script', src="https://use.fontawesome.com/releases/v5.14.0/js/all.js", defer=True)

            # Find the head tag and append the new script tag to it
            head.append(new_script)
            
            print(f"Added font awesome script tag to {filepath}")
           
    return soup

