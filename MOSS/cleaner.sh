#!/bin/bash

# Fix: Tries to make a new directory for each file. Check if the directory is already made.

if [[ $# < 1 ]]; then
  echo "Specify the directory to clean submissions."
  exit
fi

cd $1
for file in *
do
  name=$(echo "$file" | grep -o "^[^_]*")
  mkdir $name
  mv $name* $name/.
done
cd ..
