#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import random
import re
import controllers.config as config
import controllers.config
import controllers.login
import controllers.manage_quotes
import models.quotes as quotes

class Index():
	def __init__(self):
		self.login = controllers.login.Login()
		self.logout = self.login.logout
		self.manage = controllers.manage_quotes.Manage()

	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def index(self): 
		if cherrypy.session.get("log") == True:
			env = {'mountpoint': config.mountPoint}
			liste = list(quotes.Quote.select())
			qs = list(quotes.Quote.select().orderBy("id"))
			random.shuffle(liste)
			tmpl =  controllers.config.lookup.get_template("main.html")
			return tmpl.render(quotes=qs, randquotes=liste, env=config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)
		else:
			raise cherrypy.HTTPRedirect(config.mountPoint + "/login")
			
@cherrypy.expose
@cherrypy.tools.restrict_access()
def error_page_404(status, message, traceback, version):
	tmpl = controllers.config.lookup.get_template("404.html")
	return tmpl.render(env=config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)

@cherrypy.expose
@cherrypy.tools.restrict_access()
def error_page_401(status, message, traceback, version):
	tmpl = controllers.config.lookup.get_template("401.html")
	return tmpl.render(env=config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)

cherrypy.config.update({'error_page.404': error_page_404, 'error_page.401': error_page_401})	
application = cherrypy.tree.mount(Index(), config.mountPoint, config=controllers.config.monitorConfig)

if __name__ == "__main__":
	cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
	cherrypy.quickstart(Index(), config=controllers.config.monitorConfig)
