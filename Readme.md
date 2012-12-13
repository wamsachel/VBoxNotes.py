VBoxNotes.py

===MOTIVATION===
The motivation for this project stems from the fact that I like to edit a VM's 'Description' value to help keep track
of information related to that VM (e.g. created usernames and passwords, ongoing projects inside the VM,
workarounds to problems encountered, etc.).  Sometimes, Virtual Machines can be shelved for long periods of times, 
and when finally called upon I find myself forgetting things such as the username and password I had created for the
machine.  

VBoxNotes.py has a very simplistic feature set.  It can print out the notes stored on a particular VM 
(in fact, this is the default option), or it can write new notes to the .vbox-notes.txt file.  New notes can 
either be the contents of another file (using the -f flag) or simply read in from STDIN.  There is also a quiet 
option (-q) that suppresses the output of the previously stored VM notes.

===Requirements===
VBoxNotes.py has been tested on:
Windows 7 Host OS (64-bit) running Python 2.7 and VirtualBox 4.2.4
Backbox 3.0 Host OS (32-bit) running Python 2.7 and VirtualBox 4.2.2
    
Python module vboxapi
  For Windows, I needed to run the vboxapisetup.py script (as administrator):
 \>python VBOX_DIR\sdk\install\vboxapisetup.py build
 \>python VBOX_DIR\sdk\install\vboxapisetup.py install
        
  Also for Windows, I needed to get the win32com module.  Install Python Windows Extentions
  found here (http://sourceforge.net/projects/pywin32/?source=dlp)
      
===Installation===
VBoxNotes.py can really be placed anywhere.  I have been placing mine in the VirtualBox's install directory

==Usage===
usage: VBoxNotes.py [-h] [-f FILENAME] [-q] [-w] vm_name

VBoxNotes.py requires the name of a locally stored VirtualBox VM.  VM UUIDs are also accepted.  

With no other arguments, VBoxNotes.py will simply print out the previously stored notes to the terminal and then exit.
With the --quiet (-q) flag, printing of the stored notes does not happen.
To write new notes, use the --write (-w) flag.
The -w flag can be used in conjuction with the --file (-f) flag, which then allows the user to pass another file's 
contents into the note file.  
Using -w with no -f flag, will allow the user to enter notes via STDIN.  

Example:
\>python VBoxNotes.py tails -w
\<Older notes printed here\>
Enter any notes you would like saved with this Virtual Machine
(Press Ctrl-C when done):
:Testing testing
:123
:This is my important note
Ctrl-C
3 lines written to <File Path>\tails.vbox-notes.txt

\>
