#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	config.py
	
	This is the general configuration file. It serves to load the config.yml
	one and set up all the pathes needed. It also configures cherrypy by adding
	all the tools and plugins needed by the application.
"""

import cherrypy
import os
import yaml
import tools.db
import tools.restrict_access
import tools.update_env

from mako.template import Template
from mako.lookup import TemplateLookup

stream = open("config.yml", "r")
conf = yaml.load(stream)
stream.close()

baseDir = conf["basedir"]
name = conf["name"]
templateDir = "views"
sessionDir = baseDir + "/sessions"
logDir = baseDir + "/logs"
accessLog = logDir + "/access.log"
errorLog = logDir + "/error.log"
databaseFile = baseDir + "/" + conf["database"]
staticDir = baseDir + "/static"
mountPoint = "/quote"

try:
	if not os.path.exists(sessionDir):
		os.mkdir(sessionDir)
	if not os.path.exists(logDir):
		os.mkdir(logDir)
	if not os.path.exists(errorLog):
		open(errorLog, 'w').close() 
	if not os.path.exists(accessLog):
		open(accessLog, 'w').close() 
except:
	pass

htmlEnv = {
	"mountpoint": mountPoint,
	"name": name,
}

monitorConfig = {
	"/": {
		'tools.sessions.on': True,
		'tools.sessions.storage_type': "file",
		'tools.sessions.storage_path': sessionDir,
		'tools.sessions.timeout': 60,
		'tools.staticdir.root': staticDir,
		
		'tools.db.on': True,
		'tools.db.database': databaseFile,
			
		'tools.update_env.on': True,
		
		'log.error_file': errorLog,
        'log.access_file': accessLog
	},
  "/static": {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': staticDir
  }
} 

lookup = TemplateLookup(directories=[baseDir + '/' + templateDir], input_encoding='utf-8')
