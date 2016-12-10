#!/bin/bash
#Filename: countf.sh
#Written by John Owens (JD Owens) 1-23-14
#Description: This shell script counts the number of files and directories recursively. It displays the total number of files, total number of directories, and the total number of files plus directories.
#Arguments:(Default): If no arguments are presented, the program starts in the current directory. (Arguments):starts in the given directories. The numbers displayed are totaled from all arguments. 
#Notes: 
#1)Does not count the literal working directory itself, only the ones inside it and below.
#2)Arguments given must be below the directory the script is in, not above it in the file hierarchy.
#3)Anything that isn't a directory that is placed into the arguments will result in the user being prompted and exiting the program.
#4)enter "-h" into the arguments for help screen
f=0
d=0
total=0
count()
{
	cd $1
	for file in *
	do
		if [[ -f $file ]];
		then
		((f++))
		((total++))
		elif [[ -d $file ]];
		then
		((d++))	
		((total++))
		count $file
		fi
	done
	cd ..
}
help()
{
echo -e "This shell script counts the number of files and directories recursively. It displays the total number of files, total number of directories, and the total number of files plus directories." 
echo -e	 "\nArguments:\nDefault: If no arguments are presented, the program starts in the current directory.\nArguments: If arguments are presented (Which must be directories or paths to subdirectories below the script's current location), it then starts in the given directories. The numbers displayed are totaled from all arguments." 
}
if [[ -z "$1" ]]; # there are no args
	then
	  count . 

	else # there are
	  for args in $@
	  do
		if [[ -d $args ]]; #it's a directory
		  then
		  count $args
		elif [[ $args = "-h" ]];
		then
		 help
		 exit 0
		else #it's not one 
		  echo "Please enter valid directories as arguments"
		  exit 0
		fi
	  done
fi	  
echo -e "The total number of files: $f"
echo -e "The total number of directories: $d"
echo -e "The total is: $total"
exit 0
