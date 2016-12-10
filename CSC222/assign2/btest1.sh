#!/bin/sh
rm –rf fred*
echo > fred1
echo > fred2
mkdir fred3
echo > fred4
echo > fred5
echo > fred6
echo > fred7

for file in fred*
do 
  echo the current file is $file 

  if [ -d "$file" ] ; then
      echo the current directory is $file
      break;
  fi
done
echo first directory starting fred was $file
rm –rf fred*
exit 0

