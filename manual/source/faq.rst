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

What operating systems will OpenLP 2.2 support?
-----------------------------------------------

OpenLP 2.2 is designed to be cross platform. Currently it has been known to run 
on Windows (Vista, 7, 8, 10), Linux (Ubuntu and its variants, Fedora, Debian,
ArchLinux, Mint, OpenSUSE and many many others), FreeBSD & Mac OS X.
`Please let us know <http://wiki.openlp.org/Help:Contents>`_ if you have 
successfully run it on something else.

Which programming language is 2.2 developed in?
-----------------------------------------------

OpenLP 2.2 is written in `Python3 <http://www.python.org>`_ and uses the 
`Qt4 toolkit <http://qt.nokia.com>`_. Both are cross-platform which allows the 
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

Can I upgrade from any 1.9.x or 2.0.x release to 2.2?
-----------------------------------------------------

No, you should first upgrade to the last stable release in the 2.0-series
(2.0.5) and then upgrade to 2.2 to ensure that data is correctly converted.

Can I upgrade directly from 1.2 to 2.2?
---------------------------------------

No, you will have to install 2.0.5 first, then import the 1.2 data and then
upgrade to 2.2. See the 2.0 documentation for how to upgrade from 1.2 to
2.0.

Does 2.2 replace 2.0, or can they be run side by side?
------------------------------------------------------

OpenLP 2.2 and 2.0 cannot run side by side. When running 2.2 for first time
any existing 2.0 data will automatically be converted to the 2.2 format.
Note that OpenLP 2.2 is not backwards compatible with 2.0. Once you have
upgraded from 2.0, version 2.0 cannot read the upgraded files. OpenLP 2.2 will
ask if it should make a backup on startup, which can be used in case you want
to downgrade to 2.0 again.

OpenLP 2.2 cannot read service files created by OpenLP 2.0.4 and earlier, it can only
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

Is it possible to get Bible x? How?
-----------------------------------

The Bible plugin has a `Import Wizard` which can import Bibles 
from a variety of sources. The following sources are supported:

CSV
    The format is documented in the `OpenLP API documentation <http://docs.openlp.org/plugins/bibles.html#module-openlp.plugins.bibles.lib.csvbible>`_.

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

(Advanced) Where do I find the configuration file?
==================================================

Linux, FreeBSD & PC-BSD
-----------------------

If your distribution supports the XDG standard, you will find OpenLP's 
configuration file in::

    /home/<user>/.config/OpenLP/OpenLP.conf

If that file and/or directory does not exist, look for::

    /home/<user>/.openlp/openlp.conf

``<user>`` is your username.

OS X
----

You will find your configuration file here::

    /Users/<user>/Library/Preferences/org.openlp.OpenLP.plist

``<user>`` is your username.

Windows
-------

On Windows, OpenLP does not use a configuration file, it uses the Windows 
registry. You can find the settings here::

    HKEY_CURRENT_USER\Software\OpenLP\OpenLP

Troubleshooting
===============

Something has gone wrong, what should I do to help get it fixed?
----------------------------------------------------------------

If you have found an error in the program (what we call a bug) you should report 
this to us so that OpenLP can be improved. Before reporting any bugs please 
first make sure that there is not already a bug report about your problem:

#. Check the `Launchpad bug list <https://bugs.launchpad.net/openlp>`_
#. `OpenLP support System <http://support.openlp.org/>`_
#. Check the `<http://forums.openlp.org/>`_ forum

If there **is already a bug report**, you may be able to help by providing 
further information. However, **if no one else has reported** it yet, then 
please post a new bug report.

#. The **preferred place** for reporting bugs is the
   `bugs list <https://bugs.launchpad.net/openlp>`_ on Launchpad.
#. Alternatively, if you do not have a Launchpad account and do not want to sign
   up for one, you can post in the
   `bug reports forum <http://support.openlp.org/>`_.
#. If none of these ways suits you, you can send an email to
   ``support (at) openlp.org``.

What information should I include in a bug report?
--------------------------------------------------

Since OpenLP 1.9.4, there is a bug report dialog which automatically opens when
OpenLP hits a serious bug. However, this does not appear all the time, and in
some behavioural bugs, you will have to file a bug report yourself. The following
items are information the developers need in order to reproduce the bug.

Operating System
    Include information such as the version of your operating system, the
    distribution (e.g. Ubuntu, Fedora, etc.) if you are using Linux, or the
    edition (e.g. Home, Basic, Business, etc.) if you are using Windows.

Version of OpenLP
    You can find out the version of OpenLP by going to :menuselection:`Help --> About`

Steps to Reproduce
    The exact steps the developers need to follow in order to reproduce the bug.

Version of MS Office or LibreOffice
    If you are using the song imports or the presentation plugin, you will need to
    supply the version of Office or LibreOffice.

Bible Translation and Source
    If the bug occurred while you were working with Bibles, specify the
    translation of the Bible, and the source format if you imported it yourself.

**Any** Other Information
    Often bugs are caused by something that might not seem to be directly
    related to the bug itself. If you have any other information with regards to
    actions you performed or other activities when the bug occurred, it would be
    welcomed by the developers.

The more information you give us, the better we can help you.

I have been asked to email a debug log, where do I find this?
-------------------------------------------------------------

We may need a debug log to help pin-point the issue. A new log file is created 
each time you start OpenLP so copy the file before you run the software a second 
time. On Windows a Debug option is available in the start menu. On other systems, 
you will need to run OpenLP from the command line, with the following 
option: ```-l debug```. Please note, that is a lowercase **L**.

If you have not been given a specific email address to send it to, then please do 
not paste the log contents straight into a forum post. Instead, open the log 
file in a text editor (such as notepad on Windows) and copy and paste the 
contents into somewhere like `pastebin.com <http://pastebin.com>`_. Then give us 
the link to the page that is created.

Windows
^^^^^^^

Find the OpenLP 2.2 folder in your Start menu. Choose the "OpenLP (Debug)" option.

OpenLP will start up. Go to the :menuselection:`Tools --> Open Data Folder` menu 
option, and an Explorer window will appear containing folders such as alerts, 
bibles, custom etc. Keep this Explorer window open.

Now repeat the steps you need to take in OpenLP to reproduce the problem you had, 
and then close down OpenLP. 

In the Explorer window you left open, navigate up one level into the openlp 
folder. You will see the ``openlp.log`` file. This is the file to e-mail.

Linux/FreeBSD
^^^^^^^^^^^^^

If you installed OpenLP from a package::

    @:~$ openlp -l debug

Alternately, if you are running OpenLP from source::

    @:~$ ./openlp.pyw -l debug

If your Linux distribution supports the XDG standard, you will find the log in::

    ~/.cache/openlp/openlp.log

Otherwise, you will find the log file in::

    ~/.openlp/openlp.log

Mac OS X
^^^^^^^^

Open Terminal.app and navigate to where you installed OpenLP, usually 
``/Applications``::

    @:~$ cd /Applications

Then go into the OpenLP.app directory, down to the OpenLP executable::

    @:~$ cd OpenLP.app/Contents/MacOS

And then run OpenLP in debug mode::

    @:~$ ./openlp -l debug

Once you have done that, you need to get the log file. In your home directory, 
open the Library directory, and the Application Support directory within that. 
Then open the openlp directory, and you should find the openlp.log file in that 
directory::

    /Users/<username>/Library/Application Support/openlp/openlp.log

``<username>`` is your username.

The command line shows many error messages
------------------------------------------

When running OpenLP from the command line, you might get something like this::

    WARNING: bool Phonon::FactoryPrivate::createBackend() phonon backend plugin could not be loaded 
    WARNING: bool Phonon::FactoryPrivate::createBackend() phonon backend plugin could not be loaded 
    WARNING: Phonon::createPath: Cannot connect  Phonon::MediaObject ( no objectName ) to  VideoDisplay ( no objectName ). 
    WARNING: Phonon::createPath: Cannot connect  Phonon::MediaObject ( no objectName ) to  Phonon::AudioOutput ( no objectName ). 
    WARNING: bool Phonon::FactoryPrivate::createBackend() phonon backend plugin could not be loaded

These error messages indicate that you need to install an appropriate backend 
for Phonon.

Linux/FreeBSD
^^^^^^^^^^^^^

If you are using Gnome, you need to install the GStreamer backend for Phonon. On 
Ubuntu you would install the ```phonon-backend-gstreamer``` package::

    @:~$ sudo aptitude install phonon-backend-gstreamer

If you are using KDE, you need to install the Xine backend for Phonon. On Kubuntu 
you would install the ```phonon-backend-xine``` package::

    @:~$ sudo aptitude install phonon-backend-xine

If you know which audiovisual system you are using, then install the appropriate 
backend.

phonon-backend-vlc may also be worth trying on some systems.

Windows & Mac OS X
^^^^^^^^^^^^^^^^^^

Phonon should already be set up properly. If you are still having issues see
:ref:`t-no-media` in the Troubleshooting section. If that does not work, let the
developers know.

MP3's and other audio formats do not work
-----------------------------------------

This is a known issue on some systems, and we have no solution at the moment.

Videos can be slow or pixelated. Background Videos are very slow
----------------------------------------------------------------

If you are just playing videos from the Media plugin, try selecting the 
:guilabel:`Use Phonon for Video playback` option in the Media configuration,
accessible by going to :menuselection:`Settings --> Configure OpenLP --> Media`.
As for text over video, we have no solution for speeding this up. Reducing the
monitor resolution and avoiding shadows and outline text will help. We are
hoping a future release of the toolkit we are using (QtWebKit) will help improve
this, but there is no timeframe at present.

Why do live backgrounds not work in OpenLP 2.2 on Windows & Mac OS X
--------------------------------------------------------------------

Due to changes in one of the underlying frameworks that OpenLP uses (Qt4),
live backgrounds do not work in OpenLP 2.2. This will be fixed in OpenLP 2.4.

Why do playback of linked audio not work in OpenLP 2.2 on Mac OS X
------------------------------------------------------------------

Due to changes in one of the underlying frameworks that OpenLP uses (Qt4),
playback of linked audio does not work in OpenLP 2.2. This will be fixed in
OpenLP 2.4.

Features
========

Why has popular feature request X not been implemented?
-------------------------------------------------------

There are only a handful of developers working in their spare time. If 
we were to try and include everything we wanted to implement, then 2.2 would not 
likely ever get released.

I have a great idea for a new feature, where should I suggest it?
-----------------------------------------------------------------

First of all check it is not on the `Feature Requests <http://wiki.openlp.org/Feature_Requests>`_ 
page. If it is, then you need to say no more, it has already been suggested! If it 
is not on the list, then head to the `forum <http://forums.openlp.org>`_ 
and post the idea there.
