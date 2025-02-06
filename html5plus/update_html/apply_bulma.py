from bs4 import BeautifulSoup

# Import the mapping table between CSS selectors and Bulma classes

from .bulma_classes import bulma_classes

def apply_bulma_classes(soup, logger):
    for selector, class_attr in bulma_classes.items():
        elements = soup.select(selector)
        for element in elements:
            if 'class' not in element.attrs:
                # If the element does not have a class attribute, add one
                element['class'] = [class_attr]
                logger.debug(f"<{element.name}> element has class='{class_attr}'")
            elif class_attr not in element['class']:
                # If the element has a class attribute but does not contain the class_attr, add it
                element['class'].append(class_attr)
                logger.debug(f"<{element.name}> appended with Bulma class '{class_attr}' .")
            else:
                # If the element already has the class_attr, skip
                logger.debug(f"Skipped <{element.name}> tag - it already contains the Bulma class '{class_attr}'.")
                
    return soup
