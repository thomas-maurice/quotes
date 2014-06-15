#!/bin/bash

# clean.sh by thomas maurice

# cleans all the temporary files you don't want on your project

echo "Removing .pyc"
for i in `find . -name "*.pyc"`; do
  echo " - $i";
  rm -rf $i
done;

echo "Removing logs"
rm -rf logs

echo "Removing sessions"
rm -rf sessions

echo "All good !"
