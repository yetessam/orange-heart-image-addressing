from bs4 import BeautifulSoup
from update_html.bulma_classes import bulma_classes

def apply_bulma_classes(soup):
    for tag, class_attr in bulma_classes.items():
        for element in soup.find_all(tag):
            if 'class' not in element.attrs:
                # If the element does not have a class attribute, add one
                element['class'] = [class_attr]
                print(f"Applied Bulma class '{class_attr}' to <{tag}> tag without existing classes.")
            elif class_attr not in element['class']:
                # If the element has a class attribute but does not contain the class_attr, add it
                element['class'].append(class_attr)
                print(f"Added Bulma class '{class_attr}' to existing classes of <{tag}> tag.")
            else:
                # If the element already has the class_attr, skip
                print(f"Skipped <{tag}> tag as it already contains the Bulma class '{class_attr}'.")

    return soup
