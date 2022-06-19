#!/bin/bash

#source='/home/kali/Bash_Scripts/source'
#destination='/home/kali/Bash_Scripts/destination'

source=$1
destination=$2

for file in $( find $source -printf "%P\n" );
do
	if [ -a $destination/$file  ]; then
		if [ $source/$file -nt $destination/$file ]; then
			echo "Newer version of $file is detected"
			cp -r $source/$file $destination/$file
		fi
	else
		echo "Copying $file..."
		cp -r $source/$file $destination/$file
	fi
done
