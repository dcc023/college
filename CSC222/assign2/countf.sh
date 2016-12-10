#!/bin/bash
#countf.sh
#Class: CSC 222
#Author: Evan Roberts
#This script counts all files and directories in a specified directory and its subdirectories.
#	If no arguments are given, the script searches the current file location without counting the directory itself.
#	If directories are given as arguments, the script searches those directories without counting the specified directories themselves.
#	If files are given as arguments, the script includes each file in the file and total count.
#	If '-h' is entered as an argument, the script will display the Help Text and then exit.
#	If the script cannot find an argument that has been specified, it will report the error, then exit.
#After searching all subdirectories, the script will report the total number of items, the number of files, and the number of directories from all arguments; then exit.
#NOTE: THIS SCRIPT CANNOT PROCESS SUBDIRECTORIES OR ARGUMENTS THAT CONTAIN SPACES.
COUNT=0
FILECOUNT=0
DRCTCOUNT=0
count() {
	cd "$1"
	for file in *
	do
		if [[ -f $file ]]; then
			((COUNT++))
			((FILECOUNT++))
		elif [[ -d $file ]]; then
			((COUNT++))
			((DRCTCOUNT++))
			count $file
		fi
	done
	cd ..
}
printhelp() {
	echo -e "Help for - countf.sh :\nThis script reports number of files, subdirectories, and total items in specified directory or directories. If no arguments are given, it searches the current working directory. Files (but not directories) entered as arguments will also be counted.\nThe script exits is unknown arguments are entered.\nEntering '-h' as an argument will display this text.\n\nNOTE: This script cannot process subdirectories or arguments containing spaces."
}

if [ -n "$1" ]; then
	for arg in $@
	do
		if [[ $arg = "-h" ]]; then
			printhelp
			exit 0
		elif [[ -f $arg ]]; then
			((COUNT++))
			((FILECOUNT++))
		elif [[ -d $arg ]]; then
			count $arg
		else
			echo "Unknown arguments. Enter -h as argument for help."
			exit 1
		fi
	done
else
	count $PWD
fi

echo -e "Total items: $COUNT\nFiles:       $FILECOUNT\nDirectories: $DRCTCOUNT"
exit 0
