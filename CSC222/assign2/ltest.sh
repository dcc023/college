#!/bin/sh

for file in $(ls l*.sh); do
  echo $file
  echo "--------"
  cat $file
done
exit 0

