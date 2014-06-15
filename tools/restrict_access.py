#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Restricts access to certain pages to certain users/groups
"""

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
				raise cherrypy.HTTPError(401)
		except:
			raise cherrypy.HTTPError(401)

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
				raise cherrypy.HTTPError(401)
		except Exception as e:
			print e
			raise cherrypy.HTTPError(401)
	
cherrypy.tools.restrict_access = cherrypy.Tool('before_handler', restrict_access)
