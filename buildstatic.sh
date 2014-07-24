#!/bin/bash

BWD=bower_components
SD=static

if ! [ -d $SD ]; then mkdir $SD; fi;
if ! [ -d $SD/js ]; then mkdir $SD/js; fi;
if ! [ -d $SD/css ]; then mkdir $SD/css; fi;

bower install

cp $BWD/chartjs/Chart.min.js $SD/js
cp $BWD/hint.css/hint.min.css $SD/css
cp $BWD/jquery/dist/jquery.min.js $SD/js
cp -r $BWD/bootstrap/dist/* $SD/
cp -r $BWD/fontawesome/css $SD/
cp -r $BWD/fontawesome/less $SD/
cp -r $BWD/fontawesome/scss $SD/
cp -r $BWD/fontawesome/fonts $SD/
