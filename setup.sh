#!/bin/bash

for dir in "$@";

	do	
		if [ ! -d $dir ]; then                 # to check if the directory does not exist
		echo ""$dir" does not exist. " 
		mkdir "$dir"	
         	fi
		touch "$dir/app.log"
		touch "$dir/db.log"
		touch "$dir/web.log"  # create app.log, db.log and web.log file

		echo "Setup complete for $dir ."
	done
