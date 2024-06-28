import os
import shutil

def read_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_html_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

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

