OpenLP Documentation
====================
This repository holds the OpenLP manual and some other documentation.

Getting Started
---------------
To get up and running with the documentation, you'll need to install `Sphinx <https://www.sphinx-doc.org>`_ 
and the `Read The Docs theme <https://sphinx-rtd-theme.readthedocs.io>`_.

Linux
~~~~~
If you're using Linux, you'll want to check your package manager for those packages.

Ubuntu/Debian::

    $ sudo apt install python3-sphinx python3-sphinx-rtd-theme

Fedora::

   $ sudo dnf install python3-sphinx python3-sphinx_rtd_theme

macOS
~~~~~
On macOS you can install Sphinx via MacPorts or Homebrew.

MacPorts::

    $ sudo port install py37-sphinx py37-sphinx_rtd_theme

Homebrew::

    $ sudo brew install sphinx-doc

Homebrew doesn't have the Read The Docs theme, so you'll need to install it via pip::

    $ sudo pip install sphinx_rtd_theme

Windows
~~~~~~~
On Windows you'll need to use ``pip`` to install Sphinx and the Read The Docs theme::

    $ pip install sphinx sphinx_rtd_theme

Editing the Documentation
-------------------------
The documentation is written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_. If
you haven't ever used reStructuredText before, take a look at the
`reStructuredText primer <http://www.sphinx-doc.org/en/stable/rest.html>`_ for a good introduction
to the format.

reStructuredText is a plain-text format, so any text editor will work. Popular editors are
`vim <https://www.vim.org/>`_, `Atom <https://atom.io/>`_,
`Visual Studio Code <https://code.visualstudio.com/>`_ (Linux, macOS, Windows),
`Notepad++ <https://notepad-plus-plus.org/>`_ (Windows).

Building the Documentation
--------------------------
Now that you have the dependencies installed and you've edited some pages, you'll want to build the
documentation. Let's start with the manual. Go into the ``manual`` directory, and then run
``make html``::

    $ cd manual
    $ make html

This will run Sphinx on the documentation and build the HTML in the ``build/html`` directory. To
view the documentation, let's run Python's built-in web server on that directory::

    $ cd build/html
    $ python3 -m http.server

Now open your browser to `http://localhost:8000/ <http://localhost:8000/>`_ and you should see the OpenLP manual.
