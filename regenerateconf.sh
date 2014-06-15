#!/bin/bash

# RegenConf.sh by Thomas Maurice
# Regenerates your quote config file according to the
# folder you are currently in

if [ -z "$1" ]; then
	name="quotes"
else
	name="$1"
fi;

echo "basedir: `pwd`
database: database.sqlite
name: $name" > config.yml

echo "Done"
