.. _troubleshooting:

===============
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

Find the OpenLP 2.4 folder in your Start menu. Choose the "OpenLP (Debug)" option.

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

.. _t-no-media:

I can not play videos or other media
------------------------------------

If you can not play video or audio through OpenLP, the problem is most likely
that the media players have not be properly configured. The recommended media
player for OpenLP is VLC, see the manual for :ref:`config_players` for how to 
setup VLC as your default player.

If you want to use the System player, but it cannot play your media files, you
can look below for how best to set it up.

Codecs
^^^^^^

You may need to install codecs for certain files to play. Most newer versions
of Windows and OS X will support most media types. Most Linux distributions
will require a little more help to get certain media types to play.

Microsoft Windows
^^^^^^^^^^^^^^^^^

Later versions of Microsoft Windows (Vista, Windows 7) generally come with
everything you need to play most media formats. If for some reason you need
additional codecs we have seen success from the `Combined Community Codec Pack
(CCCP) <http://www.cccp-project.net/>`_.  You might also wish to check out the
K-Lite Codec Pack. If you are having issues, results do seem to vary with the
different options. What works for some may not for others, so some trial and
error may be required.

Mac
^^^

If you are using a Mac. You may wish to play Windows formats. flip4mac enables
you to use popular Windows formats such as .wmv on your Mac. You can get it
`from here <http://dynamic.telestream.net/downloads/download-flip4macwmv.htm>`_.

Ubuntu Linux (and variants)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using Ubuntu Linux, or one of its variants (Kubuntu, Edubuntu, etc...)
it is a fairly quick and easy process to get all the codecs you need to make
things work. You will need to install two meta-packages that contain all the
multimedia codecs that you will generally need. From the Software Center install
ubuntu-restricted-extras and Kubuntu-restricted-extras, or from the terminal::

  user@linux:~ $ sudo apt-get install ubuntu-restricted-extras kubuntu-restricted-extras

**Note** if you are running Kubuntu there is no need to install the
ubuntu-restricted-extras meta-package

For more information on Ubuntu and multimedia issues please check out the
`community documentation <https://help.ubuntu.com/community/RestrictedFormats/>`_.

Arch Linux
^^^^^^^^^^

The following command provides the most complete solution for codecs on Arch
Linux::

  root@linux:~ # pacman -S gstreamer0.10-{base,good,bad,ugly}-plugins gstreamer0.10-ffmpeg

If you need more help with Arch Linux and multimedia please see the `Arch Linux
documentation <https://wiki.archlinux.org/index.php/Codecs>`_.

Debian Linux
^^^^^^^^^^^^

You will need to add the Debian Multimedia Repository. So add the folowing to
/etc/apt/sources.list::

  deb http://www.debian-multimedia.org testing main non-free

Then update the repository info::

  root@linux:~ # apt-get update

Then install the following packages::

  root@linux:~ # apt-get install gstreamer0.10-ffmpeg gstreamer0.10-lame gstreamer0.10-plugins-really-bad gstreamer0.10-plugins-bad gstreamer0.10-plugins-ugly gstreamer0.10-plugins-good gstreamer0.10-x264

Fedora Linux
^^^^^^^^^^^^
You will need to set up Fedora to play most media formats. This is accomplished 
using the rpmfusion repository.

**Note** the following commands will enable a third party repository to your
system. Please check out `the RPM Fusion site <http://rpmfusion.org>`_ for more information.

To enable both the free and nonfree components for any Fedora official release
enter the following commands::

  su -c 'yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm'

After enabling the rpmfusion repository you will want to refresh your package
list, perform any updates and search for gstreamer-good, bad, and ugly and
install.

Follow the tutorial `using the rpmfusion repository <http://www.linuxjournal.com/video/getting-mp3-support-fedora-using-rpmfusion-repositories>`_
to enable extra audio and video formats on Fedora

.. _t-no-media-items:

The Media Manager appears to be missing some features
-----------------------------------------------------

If you do not see all the features listed in the Media Manager, you may need
to enable them.

To enable the plugins navigate to :menuselection:`Settings --> Plugins` or
press :kbd:`Alt+F7`. You will want to click on the plugin to the left that you
would like to enable and select **active** from the drop down box to the right.

.. image:: pics/plugin_list_main.png

By default all plugins should be enabled during the first run wizard except the
remotes plugin, unless you specify differently.

I can not see the book, chapter, and verse when I display scripture
-------------------------------------------------------------------

The book, chapter, and verse should be displayed when you display scripture. If
you can not see this your theme probably has the text size too small for the
info to be seen. See the section of the manual on :ref:`themes` if you need more info
on text sizes in themes.

I am using PowerPoint 2010 or PowerPoint Viewer 2010 and presentations do not work
----------------------------------------------------------------------------------

Currently OpenLP does not support PowerPoint Viewer 2010. PowerPoint 2010 should
work correctly, although some users have reported problems. If you have issues
with PowerPoint 2010 or PowerPoint Viewer 2010 try the PowerPoint 2003 or 2007
Viewers. `Download the PowerPoint 2007 viewer for free
<http://www.microsoft.com/downloads/en/details.aspx?FamilyID=048dc840-14e1-467d-8dca-19d2a8fd7485&displaylang=en>`_.

I have PowerPoint installed but it does not show as a presentation option
-------------------------------------------------------------------------

Installing the `Visual C++ Runtime Redistributable. <http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en>`_
has fixed this problem according to some of our users.

I am running a Linux Distro and cannot see the menu icons
---------------------------------------------------------

This seems to be a problem with XFCE and some versions of Gnome too. To correct
this problem, open  a terminal and type in the following commands::

  gconftool-2 --type boolean --set /desktop/gnome/interface/buttons_have_icons true

  gconftool-2 --type boolean --set /desktop/gnome/interface/menus_have_icons true

I chose to use a web Bible but it did not download the entire Bible
-------------------------------------------------------------------

Due to copyright restrictions OpenLP cannot download an entire Bible. It can
only download the section you search for. If you do not have an internet
connection where you intend to use OpenLP you will need another scripture
source. For more information about acquiring Bibles please see the section on
the :ref:`import_bibles`.

OpenLP is using a large amount of RAM when showing a presentation
-----------------------------------------------------------------

OpenLP uses a large amount of RAM when showing a presentation due to the way it
handles presentations. OpenLP itself is unable to show those presentations or
load the presentation files, so it interacts with the presentation through
either Microsoft PowerPoint or LibreOffice Impress. In order to show the slides
in the slide controller, OpenLP requests that the presentation application
export the slides to images, and then uses those images as slides. This results
in a large amount of RAM being used, especially in presentations with more than
about 20 slides.

OpenLP is not displaying correctly, or is not on the correct screen
-------------------------------------------------------------------

Please read the documentation on :ref:`dualmonitors`. It is very important to
have dual monitors setup properly for OpenLP to function as expected.

Previews are slow to load when using a theme with an image background
---------------------------------------------------------------------

If you are using a JPG formatted image for your background try converting it 
to another format. There is a notable performance difference between JPG and 
a format such as PNG. Other formats work in OpenLP but PNG is the preferred 
image format and yields the best performance. Images should also be sized to
the size of your output. For example, if your output screen is 1024x768 you 
should size your background image to 1024x768 also. OpenLP does not scale
images.

OpenLP crashes on startup on Windows
------------------------------------

If Windows is missing a proper driver for the graphics card on the computer, it
might cause OpenLP to crash on startup, resulting in a message saying 
:guilabel:`OpenLP has stopped working`. To fix this find, download and install
the newest driver for your graphics card.

I saved service-files in the servicemanager folder but now they are gone
------------------------------------------------------------------------

The `servicemanager` folder which can be found in OpenLP's data folder is used
internally by OpenLP for temporary files and anything in there can and will be
deleted by OpenLP. In general you should not modify or create files in OpenLP's
data folder unless you know what you are doing.

OpenLP freezes on Xfce4 in a dual monitor setup
-----------------------------------------------

There is an issue with the Xfce4 compositor that makes OpenLP freeze when using
a dual monitor setup. See configuration of dual monitor for :ref:`xfce4display`
for a solution.

MP3's and other audio formats do not work
-----------------------------------------

This is a known issue on some systems, and we have no solution at the moment.

Videos can be slow or pixelated. Background Videos are very slow
----------------------------------------------------------------

If you are just playing videos from the Media plugin, try selecting the 
:guilabel:`Use System for Video playback` option in the Media configuration,
accessible by going to :menuselection:`Settings --> Configure OpenLP --> Media`.
As for text over video, we have no solution for speeding this up. Reducing the
monitor resolution and avoiding shadows and outline text will help. We are
hoping a future release of the toolkit we are using (QtWebKit) will help improve
this, but there is no timeframe at present.

Why do live backgrounds not work in OpenLP 2.4 on Windows & Mac OS X
--------------------------------------------------------------------

Due to issues in one of the underlying frameworks that OpenLP uses (Qt5),
live backgrounds do not work in OpenLP 2.4. We aim to fix this in OpenLP 2.6.

Downgrade guide (how to restore a backup)
-----------------------------------------
In some cases new versions of OpenLP can contain bugs that was not discovered
during testing, which in some cases can mean that OpenLP cannot function
probably and the only way out is to downgrade to the previous version.

Since the OpenLP 2.2 release, new versions of OpenLP always ask if a backup
should be made of the data on the first run. It is always recommend to create
this backup, since OpenLPs data format often changes between versions, which
means that older OpenLP versions cannot read the data created by newer versions.
In case of downgrading this backup can be restored. To perform a downgrade
follow these steps:

#. Open OpenLP and in the menu go to :menuselection:`Tools --> Open Data` Folder
   to open the current data folder in a fileexplorer. If OpenLP cannot open due
   to a bug see :ref:`data_folder`.
#. Keep the fileexplorer window open and close OpenLP
#. Uninstall OpenLP and install the old version (if you have not done this
   already). Do not run OpenLP when the installation completes.
#. In the fileexplorer go up one folder-level. You should now see a lot of
   folders, find the folders that starts with ``openlp``. Depending on how many
   upgrades you have done you will see some folders looking like
   ``openlp-20160128-185424``. These folders are the backups made by OpenLP on
   upgrade. The numbers are a timestamp that you can use to find the backup with
   the you wish to restore.
#. Rename the ``openlp`` folder to ``openlp-broken-update`` or similar.
#. Rename the backup folder you wish to restore to ``openlp``.
#. Start OpenLP and watch it load your restored data.

Note: This does not restore your settings!
