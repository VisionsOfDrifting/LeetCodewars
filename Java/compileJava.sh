#!/bin/sh
#A short script to compile and run java programs
#usage function def
usage(){
echo "Usage: $0 Filename.java"
exit 1
}
#invoke usage if filename not supplied
[ $# -eq 0 ] && usage
#-F sets the field seperator, like tokenization 
FILENAME=$(echo "$1" | awk -F'.' '{print $1}')
#$(basename "$1" .java)
echo "Program:" $FILENAME
javac $FILENAME.java
echo "Output:"
java $FILENAME
