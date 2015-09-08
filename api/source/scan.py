#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
from modulefinder import ModuleFinder
import pkgutil
import string
import multiprocessing

PACKAGE_RST = string.Template("""$underline
$title
$underline

.. toctree::
   :glob:
   :maxdepth: 2

   $title/*

.. automodule:: $module
""")

MODULE_RST = string.Template("""$underline
$title
$underline

.. automodule:: $module
$exclude""")


def find_modules(importer, module, package):
    if module.startswith('openlp'):
        title = str(module.split('.')[-1])
        underline = str(len(title) * '=')
        values = {'underline': underline, 'title': title, 'module': module}
        path = os.path.join(find_modules.root_path, module.replace('.', os.path.sep) + '.rst')
        if package:
            with open(os.path.join(path), 'w+') as file:
                file.write(PACKAGE_RST.substitute(values))
        else:
            finder = ModuleFinder()
            exclude = ''
            try:
                finder.run_script(os.path.join(importer.path, title + '.py'))
            except ImportError:
                print('Failed to import {0}{1}'.format(module, ' '*25))
                raise
            except:
                print('Failed in module {0}'.format(module))
                raise
            for name in finder.modules.keys():
                if name.startswith('sqlalchemy'):
                    exclude = "   :exclude-members: mapper, or_, and_\n"
            values['exclude'] = exclude
            with open(os.path.join(path), 'w+') as file:
                file.write(MODULE_RST.substitute(values))
    find_modules.queue.put(module)


def find_modules_init(queue, root_path):
    find_modules.queue = queue
    find_modules.root_path = root_path


def progress(queue, number):
    progress_percentage = 0
    while number > progress_percentage:
        try:
            module = queue.get(True, 5)
        except queue.Empty:
            break
        percent = round((progress_percentage/number)*100)
        sys.stdout.write('{0}% File: {1}{2}\r'.format(percent, module, ' '*25))
        sys.stdout.flush()
        progress_percentage += 1
    sys.stdout.write('100%{0}\n'.format(' '*50))
    sys.stdout.flush()


def main():
    modules = []

    path_to_code = os.path.abspath(os.path.join(os.path.split(__file__)[0],
                                                '..', '..', '..', '..', 'openlp', 'trunk'))
    if not os.path.exists(path_to_code):
        print('Incorrect path to code, expecting "%s"' % path_to_code)
        sys.exit(1)

    root_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], 'api'))

    sys.path.insert(0, path_to_code)

    if os.path.isdir(root_path):
        shutil.rmtree(root_path)
    os.makedirs(root_path)

    pkg = pkgutil.walk_packages([path_to_code], onerror=print)

    for importer, module, package in pkg:
        if module.startswith('openlp'):
            path = os.path.join(root_path, module.replace('.', os.path.sep))
            if package:
                if not os.path.exists(path):
                    os.makedirs(path)
            modules.append([importer, module, package])

    del sys.path[0]

    queue = multiprocessing.Queue()
    thread = multiprocessing.Process(target=progress, args=(queue, len(modules)))
    thread.start()
    pool = multiprocessing.Pool(None, find_modules_init, [queue, root_path])
    pool.starmap(find_modules, modules)
    pool.close()


if __name__ == '__main__':
    main()
