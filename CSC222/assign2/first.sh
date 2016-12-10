#!/bin/sh
# first
# this file looks for the files containing POSIX
# and print it
for file in *
do
   if grep  POSIX $file
   then
      echo $file
   fi
done
exit 0

