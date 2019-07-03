#!/bin/bash
while true
do
	echo "Press [CTRL+C] to stop.."
        http http://$1/employees
	sleep 2
done
