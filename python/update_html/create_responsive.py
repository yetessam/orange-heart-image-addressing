from bs4 import BeautifulSoup
from ..logging_ohp import logger

def create_responsive(soup, filepath):
    # Turn off this processing for now.
    return soup
    
    # Find all elements with a class containing both "container" and "gallery"
    container_gallery_elements = soup.find_all(class_=lambda c: c and 'container' in c.split() and 'gallery' in c.split())
    
    for element in container_gallery_elements:
        # Create the new section and div tags
        section_tag = soup.new_tag('section', **{'class': 'section'})
        container_div = soup.new_tag('div', **{'class': 'container'})
        
        # Move all children of the current element into the new container div
        children = list(element.children)
        for child in children:
            container_div.append(child.extract())
        
        # Process section children
        section_children = container_div.find_all('section')
        for section in section_children:
            # Create new div tag with class "box"
            box_div = soup.new_tag('div', **{'class': 'box'})
            
            # Copy all attributes from section to div
            for attr, value in section.attrs.items():
                box_div[attr] = value
            
            # Move all contents from section to div
            box_div.extend(section.contents)
            
            # Replace section with the new div
            section.replace_with(box_div)
        
        # Add the container div to the section tag
        section_tag.append(container_div)
        
        # Append the new section tag to the current element
        element.append(section_tag)
        
        print(f"Modified DOM structure in {filepath}")
        
    return soup

