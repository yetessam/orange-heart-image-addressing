from bs4 import BeautifulSoup
from update_html.logging_ohp import logger

def create_picture_tags(soup, filepath):
    figgroup_divs = soup.find_all('div', class_=lambda c: c and 'figgroup' in c.split() and 'picture' in c.split())
    
    for div in figgroup_divs:
        # Create the picture tag
        picture_tag = soup.new_tag('picture')
        
        # Copy all attributes from div to picture
        for attr, value in div.attrs.items():
            picture_tag[attr] = value
        
        # Process img tags inside the div
        img_tags = div.find_all('img')
        default_img = None
        
        for img in img_tags:
            img_classes = img.get('class', [])
            if 'tablet' in img_classes:
                default_img = img
            else:
                source_tag = soup.new_tag('source')
                if 'desktop' in img_classes:
                    source_tag['media'] = '(min-width: 1024px)'
                elif 'mobile' in img_classes:
                    source_tag['media'] = '(max-width: 600px)'
                source_tag['srcset'] = img['src']
                picture_tag.append(source_tag)
        
        # Append the default img as fallback if it exists, otherwise append any img
        if default_img:
            picture_tag.append(default_img)
        elif img_tags:
            picture_tag.append(img_tags[0])
        
        # Get the parent of the div
        parent = div.parent
        
        # Delete the div
        div.decompose()
        
        # Insert the picture tag as the first child of its parent
        parent.insert(0, picture_tag)
        
        logger.debug(f"Deleted div and inserted picture tag as first child of its parent in {filepath}")
        
    return soup
