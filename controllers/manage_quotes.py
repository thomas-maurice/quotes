#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	manage_quotes.py
	
	This file's purpose is to manage the quotes, that is to say add some
	delete some, display all, and everyhting. This file also ensures that
	anyone trying to access a quote has the right to do it. Otherwise it
	will deny access.
"""

import cherrypy
import controllers.config
from models.quotes import *

class Manage:
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def add_one(self, quote, author):
		"""
				Add one quote
		"""
		if quote=="" or author=="":
			return '{"status": "fail", "msg": "Empty fields !"}'
		else:
			try:
				q = Quote(quote=quote.encode("utf-8"), author=author, submitter=cherrypy.session['username'])
				return '{"status": "ok", "msg": "Quote created !"}'
			except Exception as e:
				print e
				return '{ "status": "fail", "msg": "'+str(e)+'"}'
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def edit_one(self, qid, quote, author):
		"""
				Edit one quote
		"""
		try:
			q = Quote.get(int(qid))
			if q.submitter == cherrypy.session.get("username") or cherrypy.session.get("username") == "admin":
				q.quote = quote
				q.author = author
				return '{"status": "ok", "msg": "Quote edited"}'
			else:
				return '{"status": "fail", "msg": "Nope"}'
		except Exception as e:
			print e
			return '{ "status": "fail", "msg": "'+str(e)+'"}'
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def del_one(self, qid):
		"""
			Delete a quote. Only if the person tying to access the page is
			entitled to do so. Otherwise access will be denied.
		"""
		try:
			q = Quote.get(int(qid))
			if q.submitter == cherrypy.session.get("username") or cherrypy.session.get("username") == "admin":
				q.destroySelf()
				return '{"status": "ok", "msg": "Quote removed"}'
			else:
				return '{"status": "fail", "msg": "Nope"}'
		except Exception as e:
			print e
			return '{ "status": "fail", "msg": "'+str(e)+'"}'
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def stats(self):
		"""
			Generates the stats page :)
		"""
		quotes = list(Quote.select())
		auths = {}
		for q in quotes:
			try:
				auths[q.author] = auths[q.author]+1
			except KeyError:
				auths[q.author] = 1
		tmpl =  controllers.config.lookup.get_template("quotes_stats.html")
		return tmpl.render(data=auths, env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)
		
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def add(self):
		"""
			Displays the page needed to add a quote. This is not the actual
			AJAX target page.
		"""
		tmpl =  controllers.config.lookup.get_template("quotes_add.html")
		return tmpl.render(env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session, add=True)
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def edit(self, qid):
		"""
			Displays the page needed to add a quote. This is not the actual
			AJAX target page.
		"""
		try:
			quote = Quote.get(int(qid))
		except:
			raise cherrypy.HTTPError(404)
		tmpl =  controllers.config.lookup.get_template("quotes_add.html")
		return tmpl.render(quote=quote,env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session, add=False)
		

	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def all(self):
		"""
			Display all the quotes
		"""
		liste = list(Quote.select())
		tmpl =  controllers.config.lookup.get_template("quotes_all.html")
		return tmpl.render(quotes=liste, env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def one(self, i):
		"""
			Display one quotes, i being the id
		"""
		try:
			q = Quote.get(int(i))
		except:
			raise cherrypy.HTTPError(404)
		tmpl =  controllers.config.lookup.get_template("quotes_one.html")
		return tmpl.render(quote=q, env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def random(self):
		"""
			Display one quotes, i being the id
		"""
		q = random.choice(list(Quote.select()))
		return '{"quote": "'+q.quote+'", "author":"'+q.author+'", "id":"'+str(q.id)+'", "submitter": "'+q.submitter+'"}'
				
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access()
	def wall(self):
		"""
			Display the quotes, cycling
		"""
		tmpl =  controllers.config.lookup.get_template("quotes_wall.html")
		return tmpl.render(env=controllers.config.htmlEnv, user=cherrypy.session.get("username"), session=cherrypy.session)
