#!/bin/bash

folder=$1
counter=0
arr_of_paths=()


paths=$(locate $folder)
	for path in $paths:
	do
		last=$(basename "$path")
		if [ $last == $folder ]; then
			let counter++
			
			arr_of_paths+=($path)
			
		fi
		
	done
	#echo ${arr_of_paths[@]}
	len_of_arr=${#arr_of_paths[@]}


if [[ $len_of_arr -gt 0 ]]; then
	
	#echo $counter
	PS3='Choose a path: '
	#echo ${arr_of_paths[0]}
	
	select opt in "${arr_of_paths[@]}"
	do
		cd $opt
		break
	done

	command=''
	until [ "$command" == "exit" ]
	do
		$command
		p=$( pwd )
		echo -n "("$USER:$HOSTNAME")"-"["$p"]"" - " 
		read command
	done

else
	echo 'such folder does not exist'
	read -p 'Do you want to create it (y/n): ' answer
	if [ $answer == 'y' ]; then
		mkdir -p $folder && cd $folder
		echo success
	else
		echo not created
		exit
	fi
fi
