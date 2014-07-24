#!/bin/bash

# clean.sh by thomas maurice

# cleans all the temporary files you don't want on your project

echo "Removing .pyc"
for i in `find . -name "*.pyc"`; do
  echo " - $i";
  rm -rf $i
done;

echo "Removing desing stuff"
rm -rf static/fonts
rm -rf static/less
rm -rf static/scss
rm -rf static/js/bootstrap*
rm -rf static/js/Chart*
rm -rf static/js/jquery*
rm -rf static/css/bootstrap*
rm -rf static/css/font-awesome*
rm -rf static/css/hint*

echo "Removing logs"
rm -rf logs

echo "Removing sessions"
rm -rf sessions

echo "All good !"
