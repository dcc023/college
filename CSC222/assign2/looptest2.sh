#!/bin/sh

for file in $(ls l*.sh); do
  cat $file
done
exit 0

