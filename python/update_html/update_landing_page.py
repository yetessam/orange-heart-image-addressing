from bs4 import BeautifulSoup

def update_landing_page(soup, filename):
    # Check if body has a class that contains "landing-page"
    if not soup.body or 'landing-page' not in soup.body.get('class', []):
        return
    
    # Create a new div to act as the flex container
    flex_container = soup.new_tag('div', **{'class': 'flex-container'})
    
    # Create a new div for the text content
    text_content = soup.new_tag('div', **{'class': 'flex-text'})
    for element in soup.body.find_all(['h1', 'h2', 'p'], recursive=False):
        text_content.append(element.extract())
    
    # Create a new div for the image content
    image_content = soup.new_tag('div', **{'class': 'flex-image'})
    for element in soup.body.find_all('img', recursive=False):
        image_content.append(element.extract())
    
    # Append the new divs to the flex container
    flex_container.append(text_content)
    flex_container.append(image_content)
    
    # Find the main content container or create a new one if not existing
    main_content = soup.body.find('main')
    if not main_content:
        main_content = soup.new_tag('main')
        soup.body.append(main_content)
    
    # Replace the main content with the new flex container
    main_content.clear()
    main_content.append(flex_container)
    
    return soup


from bs4 import BeautifulSoup

def update_landing_page(soup, filename):
    # Check if body has a class that contains "landing-page"
    if not soup.body or 'landing-page' not in soup.body.get('class', []):
        return
    
    # Find the main content to transform
    main_content = soup.find('main', {'class': 'container'})
    if not main_content:
        print(f"Main content not found in {filename}")
        return

    # Create the new section with the desired class
    hero_section = soup.new_tag('section', **{'class': 'hero is-success is-halfheight'})
    
    # Create the hero-body div
    hero_body = soup.new_tag('div', **{'class': 'hero-body'})
    
    # Create the inner div for text content
    text_content_div = soup.new_tag('div', style='flex: 1; padding: 20px;')
    
    # Extract the title and subtitle from the article and section
    article = main_content.find('article', {'role': 'article'})
    if not article:
        print(f"Article not found in {filename}")
        return
    
    h1 = article.find('h1', {'class': 'title topictitle1'})
    if h1:
        text_content_div.append(h1.extract())
    
    section = article.find('section', {'class': 'section'})
    if section:
        h2 = section.find('h2', {'class': 'title sectiontitle hero-title'})
        if h2:
            text_content_div.append(h2.extract())
    
    # Create the inner div for image content
    image_content_div = soup.new_tag('div', style='flex: 2; padding: 20px;')
    
    # Extract the image from the figure
    figure = section.find('figure', {'class': 'fig fignone image'})
    if figure:
        image_content_div.append(figure.extract())
    
    # Append the inner divs to the hero-body div
    hero_body.append(text_content_div)
    hero_body.append(image_content_div)
    
    # Append the hero-body div to the hero section
    hero_section.append(hero_body)
    
    # Replace the main content with the new hero section
    main_content.clear()
    main_content.append(hero_section)
    
    # Embed necessary CSS for flexbox layout directly into the HTML
    soup = embed_flexbox_css(soup)
    
    return soup


def embed_flexbox_css(soup):
    style_tag = soup.new_tag('style')
    style_tag.string = """
    .hero-body {
        display: flex;
        align-items: center;
    }
    .image-content img {
        width: 100%;
        height: auto;
    }
    """
    soup.head.append(style_tag)
    return soup

