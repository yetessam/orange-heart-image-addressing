from bs4 import BeautifulSoup
from update_html.bulma_classes import bulma_classes
from ..logging import logger

def apply_bulma_classes(soup):
    for selector, class_attr in bulma_classes.items():
        elements = soup.select(selector)
        for element in elements:
            if 'class' not in element.attrs:
                # If the element does not have a class attribute, add one
                element['class'] = [class_attr]
                logger.debug(f"Applied Bulma class '{class_attr}' to <{element.name}> tag without existing classes.")
            elif class_attr not in element['class']:
                # If the element has a class attribute but does not contain the class_attr, add it
                element['class'].append(class_attr)
                logger.debug(f"Added Bulma class '{class_attr}' to existing classes of <{element.name}> tag.")
            else:
                # If the element already has the class_attr, skip
                logger.debug(f"Skipped <{element.name}> tag as it already contains the Bulma class '{class_attr}'.")
                
    return soup
