#!/usr/bin/env python
import os
import sys
from tempfile import mkdtemp
import re
import shutil

IMAGE_WIDTH = re.compile(r'^   :width: ([\d]+)px', re.UNICODE)

def restore_files(temp_dir, restore_dir):
    shutil.copytree(
    shutil.rmtree(temp_dir)

def adjust_image(match):
    try:
        width = int(match.group(1))
        width = int(round(width * 2.4))
        return str(width)
    except:
        return match.group(1)

def process_images(filename):
    contents = open(filename, 'rb').read()
    contents = IMAGE_WIDTH.sub(adjust_image, contents)
    fd = open(filename, 'wb')
    fd.write(contents)
    fd.close()

def find_files(base_dir):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            if name.endswith(u'.rst'):
                process_images(os.path.join(root, name))

def main():
    here = os.path.abspath(os.path.split(__file__)[0])
    if len(sys.argv) > 1 and sys.argv[1] == 'restore':
        temp_dir = os.path.abspath(sys.argv[2])
        restore_files(temp_dir, here)
        return
    temp_dir = mkdtemp()
    shutile.copytree(here, temp_dir)
    find_files(here)

if __name__ == '__main__':
    main()