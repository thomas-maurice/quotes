#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import controllers.config

def update_env():
	try:
		pass
	except Exception as e:
		pass
	
cherrypy.tools.update_env = cherrypy.Tool('before_handler', update_env)
