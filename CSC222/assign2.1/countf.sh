#!/bin/bash

shopt -s globstar
d=0;
f=0;

for file in **/*
do
    if [ -d "$file" ]; then
       ((d++))
    elif [ -f "$file" ]; then
       ((f++))
    fi
done

echo "There were $f files and $d directories found."
