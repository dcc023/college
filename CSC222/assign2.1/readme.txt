===============================
Homework No.2 by Dylan Campbell
===============================
------------------------------------------------
For those who are curious how this countf.sh works
------------------------------------------------

How-To
======
The script takes whatever directory you are currently in as the starting location for the search.

Once you are in the given PATH you want to start searching, run the script.

It will give you the number of files AND also the number of directories it found.


What is involved?
=================
Use of globstar so that I could utilize the **/* feature that will recursively search through all the directories.

Made sure to use #!/bin/bash since that would be the only way to access globstar as well as using integer incrementing(++).

Utilization of a for loop and if statement to check every file that was recursively found and decide whether it was a file or directory.


Credits
=======
Praise be to stackoverflow and google

