#!/usr/bin/env bash
# a Bash script that displays the content of the file /etc/passwd.
# The username
# user id
# Home directory path for the user
# using the while loop.

IFS=":"
while read -r -a line;
do
	echo "${line[0]}:${line[2]}:${line[5]}"
done < /etc/passwd
