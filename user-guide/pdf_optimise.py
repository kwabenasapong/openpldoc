#!/usr/bin/env python
import os
import sys
from tempfile import mkdtemp
import re
import shutil

IMAGE_WIDTH = re.compile(r':width: ([\d]+)px', re.UNICODE)

def copy_files(source_dir, temp_dir):
    for root, dirs, files in os.walk(source_dir):
        curr_dir = root[len(source_dir) + 1:]
        full_dir = os.path.join(temp_dir, curr_dir)
        for name in files:
            if name.endswith(u'.rst'):
                if not os.path.exists(full_dir):
                    os.makedirs(full_dir)
                shutil.copy2(os.path.join(root, name),
                    os.path.join(full_dir, name))

def restore_files(temp_dir, restore_dir):
    copy_files(temp_dir, restore_dir)
    shutil.rmtree(temp_dir)

def adjust_image(match):
    try:
        width = int(match.group(1))
        width = int(round(width * 2.4))
        return ':width: %spx' % width
    except:
        return match.group(0)

def process_images(filename):
    fd = open(filename, 'rb')
    contents = fd.read()
    fd.close()
    contents = IMAGE_WIDTH.sub(adjust_image, contents)
    fd = open(filename, 'wb')
    fd.write(contents)
    fd.close()

def process_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for name in files:
            if name.endswith(u'.rst'):
                process_images(os.path.join(root, name))

def main():
    here = os.path.abspath(os.path.split(__file__)[0])
    if len(sys.argv) > 1 and sys.argv[1] == 'restore':
        temp_dir = os.path.abspath(sys.argv[2])
        restore_files(temp_dir, here)
    else:
        temp_dir = mkdtemp()
        print temp_dir
        copy_files(here, temp_dir)
        process_files(here)

if __name__ == '__main__':
    main()