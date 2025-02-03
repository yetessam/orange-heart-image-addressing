import os
import shutil
from .logging_ohp import logger

def read_html_file(filepath):
    try:	
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        logger.error(f"Error reading file {filepath}: {e}");

def write_html_file(filepath, content):
    try:	
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        logger.error(f"Error writing file {filepath}: {e}");

def copy_files(src, dst):
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_files(s, d)
            else:
                shutil.copy2(s, d)
    else:
        shutil.copy2(src, dst)

