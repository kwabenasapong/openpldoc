==========================
Frequently Asked Questions
==========================

General Questions
=================

Can I help with OpenLP?
-----------------------

OpenLP is possible because of the commitment of individuals. If you would like 
to help there are several things that you can get involved with. Please see: 
`Contributing <http://wiki.openlp.org/Development:Getting_Started>`_ 
for more information.

I use and like OpenLP and would like to tell others online. Where can I do this?
--------------------------------------------------------------------------------

A variety of places!

* Are you on facebook? Then `become a fan <http://www.facebook.com/openlp>`_
* Are you on twitter? Then `follow openlp <http://twitter.com/openlp>`_, and
  retweet the announcements.
* Give us a thumbs up on the
  `SourceForge project page <http://www.sourceforge.net/projects/openlp>`_ 
* If you have a website or blog, then link to our site http://www.openlp.org
  with a few words saying what the software is and why you like it.
* Add a placemark on our `Worldwide Usage map <http://maps.google.com/maps/ms?ie=UTF8&source=embed&msa=0&msid=113314234297482809599.00047e88b1985e07ad495&ll=13.923404,0&spn=155.179835,316.054688&z=2>`_,
  so others in your locality can see someone close by is using it.
* If you are a member of any Christian Forums or websites, and their rules allow
  it, then perhaps review the software or ask others to review it.

What operating systems will OpenLP 2.4 support?
-----------------------------------------------

OpenLP 2.4 is designed to be cross platform. Currently it has been known to run 
on Windows (Vista, 7, 8, 10), Linux (Ubuntu and its variants, Fedora, Debian,
ArchLinux, Mint, OpenSUSE and many many others), FreeBSD & Mac OS X.
`Please let us know <http://wiki.openlp.org/Help:Contents>`_ if you have 
successfully run it on something else.

Which programming language is 2.4 developed in?
-----------------------------------------------

OpenLP 2.4 is written in `Python3 <http://www.python.org>`_ and uses the 
`Qt5 toolkit <http://www.qt.io>`_. Both are cross-platform which allows the 
software to run on different types of machine and so allow more people access to 
free worship software. Python is one of the easier programming languages to 
learn, so this helps us develop and `find bugs <http://wiki.openlp.org/Bug#Something_has_gone_wrong.2C_what_should_I_do_to_help_get_it_fixed.3F>`_ 
quicker, and also allows more developers to contribute with the project.

Which written languages does OpenLP support?
--------------------------------------------
                            
OpenLP has support for multiple languages which can be seen on the 
:menuselection:`Settings -->Translate` menu. However some of these translations 
are incomplete. If you would like to help complete or start to translate OpenLP 
into your language then see the `Getting started page <http://wiki.openlp.org/Translation:Getting_Started>`_. 

Upgrading
=========

Can I upgrade from any 1.9.x or 2.0.x release to 2.4?
-----------------------------------------------------

No, you should first upgrade to the last stable release in the 2.0-series
(2.0.5) and then upgrade to 2.4 to ensure that data is correctly converted.
You can download OpenLP 2.0.5 from <http://sourceforge.net/projects/openlp/files/openlp/2.0.5/>`_. 

Can I upgrade directly from 1.2 to 2.4?
---------------------------------------

No, you will have to install 2.0.5 first, then import the 1.2 data and then
upgrade to 2.4. See the 2.0 documentation for how to upgrade from 1.2 to
2.0. You can download OpenLP 2.0.5 from <http://sourceforge.net/projects/openlp/files/openlp/2.0.5/>`_. 

Does 2.4 replace older 2.x versions, or can they be run side by side?
---------------------------------------------------------------------

OpenLP 2.4 and earlier 2.x versions cannot run side by side. When running 2.4 for first time
any existing 2.x data will automatically be converted to the 2.4 format.
Note that OpenLP 2.4 is not backwards compatible with earlier 2.x versions. Once you have
upgraded from the older OpenLP versions cannot read the upgraded files. OpenLP 2.4 will
ask if it should make a backup on startup, which can be used in case you want
to downgrade again.

OpenLP 2.4 cannot read service files created by OpenLP 2.0.4 and earlier, it can only
read service files created by OpenLP 2.0.5.

Using OpenLP
============

I have started OpenLP, but I cannot see the songs or bibles section in the Media Manager
----------------------------------------------------------------------------------------

When you installed OpenLP, the first time wizard would have asked which plugins 
you wanted, and songs and bibles should have been selected. If for some reason 
they were not, then you will need to activate them yourself. See below
for instructions.

How do I activate / deactivate a plugin?
----------------------------------------

Plugins can be turned on and off from the Plugin List Screen. Select the plugin 
you wish to start/stop and change its status. You should not need to restart 
OpenLP.

What are these plugins that I keep seeing mentioned?
----------------------------------------------------

The plugins allow OpenLP to be extend easily.  A number have been written 
(Songs, Bibles, Presentations) etc but it is possible for the application to be 
extended with functionality only you require.  If this is the case then go for 
it but lets us know as we can help and it may be something someone else wants.

How do I enable PowerPoint/Impress/PowerPoint Viewer?
-----------------------------------------------------

First of all ensure that the presentation plugin is enabled (see above).
Then to enable a presentation application, go to the `Settings` dialog, switch 
to the `Presentations` tab and check one of the enabled checkboxes. OpenLP will 
automatically detect which of the three you have installed, and enable the 
appropriate checkbox(es). Check the applications you require, and then restart 
OpenLP for the change to be detected. 
Note, PowerPoint Viewer 2010 is not yet supported, use 2003 or 2007.

Why can LibreOffice Impress not be used on Mac OS X?
----------------------------------------------------

Currently the presentations plugin does not support Impress on OS X. The 
reason for that is that the interoperability component (pyuno) in LibreOffice on
Mac OS X cannot be used by OpenLP due to incompatibilities between the version
of Python used by LibreOffice and the Python version used by OpenLP.

Why can MS PowerPoint not be used on Mac OS X?
----------------------------------------------

Currently the presentations plugin does not support PowerPoint on OS X. The 
reason for that is that so far we have found that the available method to
control PowerPoint on OS X is not good enough for integration with OpenLP.
If this changes we will look at including this feature.

I am on Windows and PowerPoint is installed, but it does not appear as an option
--------------------------------------------------------------------------------

Try installing the `Visual C++ Runtime Redistributable <http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en>`_.

Why does PowerPoint presentations not advance automatically
-----------------------------------------------------------

The reason that PowerPoint does not advance automatically is that it can only do
so when it has the focus. But when using OpenLP for controlling presentation,
OpenLP has the focus. So in order to make PowerPoint advance automatically the
focus must be switched to PowerPoint, which can be done by clicking the
Powerpoint-icon in the taskbar once the PowerPoint presentation has opened.

Is it possible to get Bible x? How?
-----------------------------------

The Bible plugin has a `Import Wizard` which can import Bibles 
from a variety of sources. The following sources are supported:

CSV
    The format is documented in the `OpenLP API documentation <http://api.openlp.io/api/openlp/plugins/bibles/lib/csvbible.html#module-openlp.plugins.bibles.lib.csvbible>`_.

OSIS
    An XML format for Bible. You can export Bibles from the `Sword Project <http://www.crosswire.org/sword/software/>`_
    into OSIS using the ``mod2osis`` tool. After using the Sword software Media
    Manager (or other Sword frontend, like BibleTime or Xiphos) to download the
    required Bible, run the following command from the command line (works on
    Windows and Linux)::

        mod2osis <name> > <name>.osis

    The ``<name>`` parameter is the name of your Bible, as you see it in Sword.
    Note that the ``<name>`` is case sensitive on all environments. Once you
    have exported your Bible to OSIS, the Bible import wizard will the read
    ``<name>.osis`` file and import your Bible.

OpenSong
    OpenSong has a good selection of Bibles on their
    `download page <http://www.opensong.org/d/downloads#bible_translations>`_.

Web Download
    OpenLP can download Bibles on demand from the following 3 sites:

    * `Crosswalk <http://biblestudy.crosswalk.com/bibles/>`_
    * `BibleGateway <http://www.biblegateway.com/versions/>`_
    * `BibleServer <http://www.bibleserver.com>`_

Zefania
   The Zefania project has many bibles available from `their website <http://sourceforge.net/projects/zefania-sharp/files/Bibles/>`_

Why do my Bible verses take a long time to load?
------------------------------------------------

In order to better conform to copyright law, the Web Download Bibles are not 
downloaded when you import them, but on the fly as you search for them. As a 
result, the search takes a little longer if you need to download those 
particular verses. Having said that, the Web Download Bibles cache downloaded 
verses so that you do not need to download them again.

My Bible is on the Web Download sites, but my Church is not on the internet. What options do I have?
----------------------------------------------------------------------------------------------------

When you create and save a service, all the items in the service are saved with 
it. That means any images, presentations, songs and media items are saved. This 
is also true for bibles. What this means is you can create the service on your 
home computer, insert a Bible passage from the web, save it and then open the 
service using your church computer and voila, the Bible passage should be there! 
Note this can also be done with songs, etc!


Location of OpenLP files
========================

Where do I find the configuration file?
---------------------------------------

Linux, FreeBSD & PC-BSD
^^^^^^^^^^^^^^^^^^^^^^^

If your distribution supports the XDG standard, you will find OpenLP's 
configuration file in::

    /home/<user>/.config/OpenLP/OpenLP.conf

If that file and/or directory does not exist, look for::

    /home/<user>/.openlp/openlp.conf

``<user>`` is your username.

Mac OS X
^^^^^^^^

You will find your configuration file here::

    /Users/<user>/Library/Preferences/org.openlp.OpenLP.plist

``<user>`` is your username.

Windows
^^^^^^^

On Windows, OpenLP does not use a configuration file, it uses the Windows 
registry. You can find the settings here::

    HKEY_CURRENT_USER\Software\OpenLP\OpenLP

.. _data_folder:

Where do I find the data folder?
--------------------------------

Normally you can open the data folder by using the menu :menuselection:`Tools --> Open Data Folder`
and a fileexplorer window will appear with the data folder. In some cases due to
bugs or other issues this is not an option, and the folder must be found
manually.

Linux, FreeBSD & PC-BSD
^^^^^^^^^^^^^^^^^^^^^^^

The data folder is located in ``/home/<user>/.local/share/openlp``.

Mac OS X
^^^^^^^^

On Mac OS X the data folder is located in ``/Users/<username>/Library/Application Support/openlp``

Windows
^^^^^^^

To get to the data folder on Windows, pres the Windows Key and "R" at the same
time. This will open a the :menuselection:`Run dialog`. Enter ``%appdata%\OpenLP``
and press <Enter>. This will open a fileexplorer with in the data folder.

Features
========

Why has popular feature request X not been implemented?
-------------------------------------------------------

There are only a handful of developers working in their spare time. If 
we were to try and include everything we wanted to implement, then 2.4 would not 
likely ever get released.

I have a great idea for a new feature, where should I suggest it?
-----------------------------------------------------------------

First of all check it is not on the `Feature Requests <http://wiki.openlp.org/Feature_Requests>`_ 
page. If it is, then you need to say no more, it has already been suggested! If it 
is not on the list, then head to the `forum <http://forums.openlp.org>`_ 
and post the idea there.
