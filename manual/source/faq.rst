==========================
Frequently Asked Questions
==========================

General Questions
=================

Can I help with OpenLP?
-----------------------

OpenLP is possible because of the commitment of individuals. If you would like to help there are several things that
you can get involved with. Please see our `Contribute`_ page for more information.

I use and like OpenLP and would like to tell others online. Where can I do this?
--------------------------------------------------------------------------------

A variety of places!

* Are you on Facebook? Then `become a fan`_.
* Are you on Twitter? Then `follow OpenLP`_, and retweet the announcements.
* If you have a website or blog, then link to `our web site`_ with a few words saying what OpenLP is and why you like it.
* Add a placemark on our `Worldwide Usage map`_, so others in your locality can see someone close by is using it.
* If you are a member of any Christian forums or websites, and their rules allow it, then perhaps review OpenLP or ask
  others to review it.

What operating systems does OpenLP support?
-------------------------------------------

OpenLP is designed to be cross platform. Currently it has been known to run on Windows (Vista, 7, 8, 10), Linux (Ubuntu
and its variants, Fedora, Debian, ArchLinux, Mint, OpenSUSE and many others), FreeBSD and macOS. `Please let us know`_
if you have successfully run it on something else.

Which programming language is OpenLP developed in?
--------------------------------------------------

OpenLP is written in `Python 3`_ and uses the `Qt5 toolkit`_ via the `PyQt5 library`. Both are cross-platform which
allows the software to run on different types of machine and so allow more people access to free worship software.
Python is one of the easier programming languages to learn, so this helps us develop and `find bugs`_ faster, and also
allows more developers to contribute with the project.

Which written languages does OpenLP support?
--------------------------------------------
                            
OpenLP has support for multiple languages which can be seen on the :menuselection:`Settings -->Translate` menu. However
some of these translations are incomplete. If you would like to help complete or start to translate OpenLP into your
own language then see the `Getting started page`_ for translations. 

Upgrading
=========

.. warning::

   Newer versions of OpenLP are not backwards compatible with earlier versions. Once you have upgraded to a newer
   version, the older version of OpenLP will not be able to read the upgraded files.
   
.. note::
   
   It is always a good idea to make a backup when prompted by OpenLP.

Can I upgrade from any 1.9.x or 2.0.x release to 2.4?
-----------------------------------------------------

No, you should first upgrade to the last stable release in the 2.0-series (2.0.5) and then upgrade to 2.4 to ensure
that data is correctly converted.  You can download OpenLP 2.0.5 from `<https://get.openlp.org/2.0.5/>`_. 

Can I upgrade directly from 1.2 to 2.4?
---------------------------------------

No, you will have to install 2.0.5 first, then import the 1.2 data and then upgrade to 2.4. See the 2.0 documentation
for how to upgrade from 1.2 to 2.0. You can download OpenLP 2.0.5 from `<https://get.openlp.org/2.0.5/>`_. 

Does 2.4 replace older 2.x versions, or can they be run side by side?
---------------------------------------------------------------------

OpenLP 2.4 and earlier 2.x versions cannot run side by side. When running 2.4 for first time any existing 2.x data will
automatically be converted to the 2.4 format. OpenLP 2.4 will ask if it should make a backup on startup, which can be
used in case you want to downgrade again.

OpenLP 2.4 cannot read service files created by OpenLP 2.0.4 and earlier, it can only read service files created by
OpenLP 2.0.5 and higher.

Where can I download an older version of OpenLP?
------------------------------------------------

.. warning::

   Only the most current version of OpenLP is supported. If you submit a bug report for an older version, you will be
   told to upgrade first.

Sometimes you might need to download an older version of OpenLP. You can always find previous versions of OpenLP on our
download server: `<https://get.openlp.org/>`_

Using OpenLP
============

I have started OpenLP, but I cannot see the songs or bibles section in the Library
----------------------------------------------------------------------------------

When you installed OpenLP, the first time wizard would have asked which plugins you wanted, and songs and bibles should
have been selected. If for some reason they were not, then you will need to activate them yourself. See below for
instructions.

How do I activate / deactivate a plugin?
----------------------------------------

Plugins can be turned on and off from the Plugin List Screen. Select the plugin you wish to start/stop and change its
status. You should not need to restart OpenLP.

What are these plugins that I keep seeing mentioned?
----------------------------------------------------

The plugins allow OpenLP to be extend easily. A number have been written (Songs, Bibles, Presentations) etc but it is
possible for the application to be extended with functionality only you require. If this is the case then go for it but
let us know as we can help and it may be something someone else wants.

How do I enable PowerPoint/Impress/PowerPoint Viewer?
-----------------------------------------------------

.. note::

   PowerPoint, Keynote and LibreOffice are not supported on macOS due to limitations with the platform. This is
   outside of our control.

.. note::

   PowerPoint Viewer 2010 is not supported, use 2003 or 2007.

First of all ensure that the presentation plugin is enabled (see above). Then to enable a presentation application, go
to the `Settings` dialog, switch to the `Presentations` tab and check one of the enabled checkboxes. OpenLP will 
automatically detect which of the three you have installed, and enable the appropriate checkbox(es). Check the
applications you require, and then restart OpenLP for the change to be detected. 

I am on Windows and PowerPoint is installed, but it does not appear as an option
--------------------------------------------------------------------------------

Try installing the `Visual C++ Runtime Redistributable`_.

Why don't PowerPoint presentations advance automatically?
---------------------------------------------------------

The reason that PowerPoint does not advance automatically is that it can only do so when it has the focus. But when
using OpenLP for controlling presentation, OpenLP has the focus. So in order to make PowerPoint advance automatically
the focus must be switched to PowerPoint, which can be done by clicking the Powerpoint-icon in the taskbar once the
PowerPoint presentation has opened.

Is it possible to get a particular translation of the Bible? How?
-----------------------------------------------------------------

.. note::

   OpenLP does not have distrubution rights for most popular translations of the Bible. Bible societies require
   exhorbitant licensing costs which OpenLP could never afford. We cannot help you find those Bibles.

The Bible plugin has a `Import Wizard` which can import Bibles from a variety of sources. The following sources are
supported:

CSV
    The format is documented in the `OpenLP API documentation`_.

OSIS
    An XML format for Bible. You can export Bibles from the `Sword Project`_ into OSIS using the ``mod2osis`` tool.
    After using the Sword software Media Manager (or other Sword frontend, like BibleTime or Xiphos) to download the
    required Bible, run the following command from the command line (works on Windows and Linux)::

        mod2osis NAME > NAME.osis

    The ``NAME`` parameter is the name of your Bible, as you see it in Sword. Note that the ``NAME`` is case sensitive
    on all environments. Once you have exported your Bible to OSIS, the Bible import wizard will the read ``NAME.osis``
    file and import your Bible.

OpenSong
    OpenSong has a good selection of Bibles on their `download page`_.

Web Download
    OpenLP can download Bibles on demand from the following 3 sites:

    * `Crosswalk`_
    * `BibleGateway`_
    * `BibleServer`_

Zefania
   The Zefania project has many bibles available from `their website`_.

Why do my Bible verses take a long time to load?
------------------------------------------------

In order to better conform to copyright law, the Web Download Bibles are not downloaded when you import them, but on
the fly as you search for them. As a result, the search takes a little longer if you need to download those particular
verses. Having said that, the Web Download Bibles cache downloaded verses so that you do not need to download them
again.

My Bible is on the Web Download sites, but my Church is not on the internet. What options do I have?
----------------------------------------------------------------------------------------------------

When you create and save a service, all the items in the service are saved with it. That means any images,
presentations, songs and media items are saved. This is also true for bibles. What this means is you can create the
service on your home computer, insert a Bible passage from the web, save it and then open the service using your church
computer and voila, the Bible passage should be there! Note this can also be done with songs, etc!


Location of OpenLP files
========================

Where do I find the configuration file?
---------------------------------------

Linux, FreeBSD and PC-BSD
^^^^^^^^^^^^^^^^^^^^^^^^^

If your distribution supports the XDG standard, you will find OpenLP's configuration file in::

    /home/<user>/.config/OpenLP/OpenLP.conf

If that file and/or directory does not exist, look for::

    /home/<user>/.openlp/openlp.conf

``<user>`` is your username.

macOS
^^^^^

You will find your configuration file here::

    /Users/<user>/Library/Preferences/org.openlp.OpenLP.plist

``<user>`` is your username.

Windows
^^^^^^^

On Windows, OpenLP does not use a configuration file, it uses the Windows registry. You can find the settings here::

    HKEY_CURRENT_USER\Software\OpenLP\OpenLP

.. _data_folder:

Where do I find the data folder?
--------------------------------

Normally you can open the data folder by using the menu :menuselection:`Tools --> Open Data Folder` and a file manager
window will appear with the data folder. In some cases due to bugs or other issues this is not an option, and the
folder must be found manually.

Linux, FreeBSD and PC-BSD
^^^^^^^^^^^^^^^^^^^^^^^^^

The data folder is located in ``/home/<user>/.local/share/openlp``.

macOS
^^^^^

On macOS the data folder is located in ``/Users/<username>/Library/Application Support/openlp``

Windows
^^^^^^^

To get to the data folder on Windows, pres the Windows Key and "R" at the same time. This will open a the
:menuselection:`Run dialog`. Enter ``%appdata%\OpenLP`` and press <Enter>. This will open a file manager within the
data folder.

Features
========

Why has popular feature request X not been implemented?
-------------------------------------------------------

There are only a handful of developers working in their spare time. If we were to try and include everything we wanted
to implement, then we would never be able to release any new versions of OpenLP.

I have a great idea for a new feature, where should I suggest it?
-----------------------------------------------------------------

First of all check it is not listed as a "wishlist" bug on `Launchpad`_. If it is, then you need to say no more, it has
already been suggested! If it is not on the list, then head to the `forums`_ and post the
idea there.

.. _Contribute: https://openlp.org/contribute
.. _become a fan: https://www.facebook.com/openlp
.. _follow OpenLP: https://twitter.com/openlp
.. _our web site: https://openlp.org/
.. _Worldwide Usage map: https://maps.google.com/maps/ms?ie=UTF8&source=embed&msa=0&msid=113314234297482809599.00047e88b1985e07ad495&ll=13.923404,0&spn=155.179835,316.054688&z=2
.. _Please let us know: https://forums.openlp.org/
.. _Python 3: http://www.python.org/
.. _Qt5 toolkit: https://www.qt.io/
.. _PyQt5 library: https://www.riverbankcomputing.com/software/pyqt/intro
.. _find bugs: http://wiki.openlp.org/Bug#Something_has_gone_wrong.2C_what_should_I_do_to_help_get_it_fixed.3F
.. _Getting started page: http://wiki.openlp.org/Translation:Getting_Started
.. _Visual C++ Runtime Redistributable: http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en
.. _OpenLP API documentation: http://api.openlp.io/api/openlp/plugins/bibles/lib/csvbible.html#module-openlp.plugins.bibles.lib.csvbible
.. _Sword Project: http://www.crosswire.org/sword/software/
.. _download page: http://www.opensong.org/home/download#bibles
.. _Crosswalk: http://biblestudy.crosswalk.com/bibles/
.. _BibleGateway: http://www.biblegateway.com/versions/
.. _BibleServer: http://www.bibleserver.com
.. _their website: http://sourceforge.net/projects/zefania-sharp/files/Bibles/
.. _Launchpad: https://bugs.launchpad.net/openlp
.. _forums: https://forums.openlp.org/
