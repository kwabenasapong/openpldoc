style_guide.rst
=========================
OpenLP Manual Style Guide
=========================

This Style Guide will be used to clarify how the manual is formated and is 
intended to keep all the pages in the manual consistent.

Page Title
==========

Each page will begine with a link reference and a title.  The link reference
should be the same as the title except that it is all in lower case with no 
spaces.  Titles are to be in Title Case.

.. code-block:: rst

    .. _bibles:
    
    ======
    Bibles
    ======


Line Length
===========

Each line of the document should be no longer than 120 characters.  While
the build system can wrap the text, lines longer than 120 characters are 
difficult to manage in a text editor.

Pictures
========

All pictures will be in the .png format and stored in the pics directory of 
the manual.  If the pictures is for a specific page the filename will start 
with the page name and contain no spaces.

All pictures used in the page will be described at the end of the document and
image pointers will be used inside the document when an image is to be 
displayed.  The image deffinition uses upper case for the image title and the
in line image link uses lower case for the image title.  No spaces are to be
used in the image deffinition title. The image deffinition title will start 
with the page name unless the image is used across pages.

End of Page Example:

.. code-block:: rst
    
    .. pictures used in this page

    .. |DELETEICON| image:: pics/theme_delete.png

In Page Example:

.. code-block:: rst
    
    Click on the |deleteicon| Delete Icon to delete the Bible.


On Screen Buttons
=================

When instructing the user to use an on screen button, use the Gui label formated
to make the button stand out.  

Gui Label Format :guilabel:`Next`

Menu Paths
==========

When describing a menu path, use the menu selection format.

:menuselection:`File --> Import --> Bible`

Referance Links For Headers
===========================

All sublevel headers will have a referance link above the header. 
The referance link name will start with the page title and then the sublevel
title.  No spaces are allowed in the link reference.

.. code-block:: rst
    
    .. _bibles_sublevel:
    
    Sublevel
    ========


Terminal Commands
=================

When telling the user to enter a command on the command prompt or in a terminal
window, use a double colon and 1 blank line before what the user is to type. 
Add 1 blank line after the what the user is to type.

.. code-block:: rst
    
    To convert a Bible using the command prompt in
    Windows or a terminal in Linux or macOS you would type:
    
    mod2osis biblename > biblename.osis


Codeing
=======

When entering coding use the wrap the coding inside two ` characters.

.. code-block:: rst
    
    ``<div align="left">``
    
 
Toolbar Descriptions
====================

When describing the items in a toolbar with one line descriptions, use the 
toolbar formatting.

.. code-block:: rst
    
    |image| image description::
        some description about the image.
    
When the toolbar items need more detail, or you are documenting a feature, 
then use an inline Icon with Icon name

.. code-block:: rst
    
    Selecting the |biblelock| Lock icon locks and unlocks the search results.  
    
    This feature can be used to combine multiple search results into one ... 


End of File
===========

Only leave upto one blank line at the end of the page.

Definitions
===========

Sentence case
+++++++++++++

The first letter of the first word is upper case, all other letters are lower case, unless the word is a proper noun.

Title case
++++++++++
The first letter of all words is upper case, except for secondary 2 letter words ("Go to Next Slide").

Names of Widgets
++++++++++++++++
All widget names should be normal parts of sentences, e.g. "Cannot drag item from media manager to service manager."

Standards
=========

Labels
++++++

All labels should be sentence case and end with a colon, unless the label is attached to check box or radio button: "Select theme file:"

Group Box Labels
++++++++++++++++

Group box labels should be title case, without any trailing colons: "Display Options"

Menu Items
++++++++++

Menu items should be title case: "Go to Next Slide", "Save As"

Window/Dialog Titles
++++++++++++++++++++

All window and dialog titles should be title case: "Open Service File"

Dialog Text
+++++++++++

Dialog text must be full, proper sentences, with each sentence ending in a period.

Tooltips (hints)
++++++++++++++++

Tooltips should be sentence case, and end with a period: "Open an existing service file."

Combo Boxes
+++++++++++

Data in combo boxes should be in title case: "New International Version"

Check Boxes
+++++++++++

Check boxes should have sentence case labels.

Buttons
+++++++

Buttons should have title case labels.
