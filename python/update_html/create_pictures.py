from bs4 import BeautifulSoup

def create_picture_tags(soup, filepath):
    figgroup_divs = soup.find_all('div', class_=lambda c: c and 'figgroup' in c.split() and 'picture' in c.split())
    
    for div in figgroup_divs:
        # Create the picture tag
        picture_tag = soup.new_tag('picture')
        
        # Copy all attributes from div to picture
        for attr, value in div.attrs.items():
            picture_tag[attr] = value
        
        # Move the contents of the div into the picture tag
        for child in div.contents:
            if child.name == 'img':
                img_classes = child.get('class', [])
                is_default = 'tablet' in img_classes
                
                for img_class in img_classes:
                    if img_class != 'image' and img_class != 'tablet':
                        source_tag = soup.new_tag('source')
                        if img_class == 'desktop':
                            source_tag['media'] = '(min-width: 1024px)'
                        elif img_class == 'mobile':
                            source_tag['media'] = '(max-width: 600px)'
                        source_tag['srcset'] = child['src']
                        picture_tag.append(source_tag)
                
                # Append the original img tag as the fallback
                if is_default or not picture_tag.find_all('source'):
                    picture_tag.append(child)
            else:
                picture_tag.append(child)
        
        # Replace the div with the picture tag
        div.replace_with(picture_tag)
        
        print(f"Replaced div with picture tag in {filepath}")
        
    return soup


