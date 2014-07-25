#!/bin/bash

BWD=bower_components
SD=static

if [ -z "`which bower`" ]; then
	echo "You need to install bower ! Type
	npm install -g bower
to do so."
  exit 1
fi;

echo "Creating directory structure"

if ! [ -d $SD ]; then mkdir $SD; fi;
if ! [ -d $SD/js ]; then mkdir $SD/js; fi;
if ! [ -d $SD/css ]; then mkdir $SD/css; fi;

echo "Running bower"
bower install

echo "Copying files"
cp $BWD/chartjs/Chart.min.js $SD/js
cp $BWD/hint.css/hint.min.css $SD/css
cp $BWD/jquery/dist/jquery.min.js $SD/js
cp -r $BWD/bootstrap/dist/* $SD/
cp -r $BWD/fontawesome/css $SD/
cp -r $BWD/fontawesome/less $SD/
cp -r $BWD/fontawesome/scss $SD/
cp -r $BWD/fontawesome/fonts $SD/
