#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import sqlobject as sql
import controllers.config
from models.users import *

def restrict_access(public=False, users = [], groups=[]):
	if public == True:
		return
	
	# Not a public page
	
	if cherrypy.session.get("log") != True:
		raise cherrypy.HTTPRedirect(controllers.config.mountPoint + "/login")
	else:
		pass
	
	if users != []:
		try:
			if cherrypy.session.get("username") in users:
				pass
			else:
				raise cherrypy.HTTPRedirect(controllers.config.mountPoint + "/login")
		except:
			raise cherrypy.HTTPRedirect(controllers.config.mountPoint + "/login")

	if groups != []:
		try:
			u = User.byLogin(cherrypy.session.get("username"))
			isok = False

			for g in u.groups:
				if g.name in groups:
					isok = True
				else:
					pass
			
			if isok == True:
				pass
			else:
				raise cherrypy.HTTPRedirect(controllers.config.mountPoint + "/login")
		except Exception as e:
			print e
			raise cherrypy.HTTPRedirect(controllers.config.mountPoint + "/login")
	
cherrypy.tools.restrict_access = cherrypy.Tool('before_handler', restrict_access)
