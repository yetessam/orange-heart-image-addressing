import argparse
import os
import sys
from bs4 import BeautifulSoup

from update_html.apply_bulma import apply_bulma_classes
from update_html.bulma_classes import bulma_classes
from update_html.copy_resource import copy_resource
from update_html.create_pictures import create_picture_tags
from update_html.create_responsive import create_responsive
from update_html.file_operations import copy_files, read_html_file, write_html_file
from update_html.logging_ohp import logger
from update_html.modify_navbar import modify_navbar
from update_html.update_head import update_head


def parse_arguments():
    parser = argparse.ArgumentParser(description='Pass through the DITA OT output folder, the target src folder and the Python resources folder')
    parser.add_argument('--out_dir', type=str, required=True, help="DITA OT folder where the HTML files are build, normally called 'out'")
    parser.add_argument('--src_dir', type=str, required=True, help='After processing, this folder contains the Bulma-ready HTML.')
    parser.add_argument('--res_dir', type=str, required=True, help='This folder contains additional resource files such as css or icons.')
    return parser.parse_args()

def find_html_files(out_dir):
    html_files = []
    for root, dirs, files in os.walk(out_dir):
        for fname in files:
            if fname.endswith('.html'):
                html_files.append(os.path.join(root, fname))
    return html_files

def process_html_file(filepath):
    content = read_html_file(filepath)
    soup = BeautifulSoup(content, 'html.parser')
    soup.prettify()

    # Passing through the filepath to improve error messages
    soup = update_head(soup, filepath)
    soup = create_picture_tags(soup, filepath)
    soup = create_responsive(soup, filepath)

    soup = apply_bulma_classes(soup)
    soup = modify_navbar(soup)
    
    write_html_file(filepath, soup.prettify())
    print(f"Modified and saved HTML file: {filepath}")

def setup_directories(out_dir, src_dir):
    if not os.path.exists(out_dir):
        raise FileNotFoundError(f"Could not find the html 5 out directory: {out_dir}. Exiting.")
    
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print(f"Created destination directory: {src_dir}")

def build_search_index(src_dir):
    # Placeholder for search index building logic
    logger.debug(f"Placeholder for build_search_index logic in {src_dir}")
    # Implement search index logic here

def process_html_files(out_dir, src_dir, res_dir):
    logger.info(f"process_html_files to copy from out directory: {out_dir}, to src directory: {src_dir} with resources from {res_dir}")

    setup_directories(out_dir, src_dir)

    html_files = find_html_files(out_dir)
    if not html_files:
        raise FileNotFoundError(f"No HTML files found in the {out_dir}. Exiting.")
    
    logger.debug(f"Found {len(html_files)} HTML files:")
    for filepath in html_files:
        print(filepath)
        process_html_file(filepath)

    copy_files(out_dir, src_dir)
    logger.info(f"Copied all files from {out_dir} to {src_dir}\n\n")

    # Copy bulma css resource and the index redirect 
    css_dest_dir = os.path.join(src_dir, "css")
    css_file = "bulma.css"
    index_file  = "index.html"
    
    copy_resource(res_dir, css_dest_dir, css_file)
    copy_resource(res_dir, src_dir, index_file)
    
    build_search_index(src_dir)

def main():
    args = parse_arguments()
    out_dir = args.out_dir
    src_dir = args.src_dir
    res_dir = args.res_dir

    logger.info(f"Output directory: {out_dir}")
    logger.info(f"Web site source directory: {src_dir}")
    logger.info(f"Resource directory: {res_dir}\n\n")
    
    try:
        process_html_files(out_dir, src_dir, res_dir)
    except Exception as e:
        logger.error(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
