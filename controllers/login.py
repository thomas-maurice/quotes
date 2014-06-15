#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import yaml
import hashlib
from datetime import timedelta

import controllers.config as config
import models.users as users
from models.users import User

import tools.restrict_access

class Login:
	@cherrypy.expose
	def index(self):
		if cherrypy.session.get("log") == True:
			raise cherrypy.HTTPRedirect(config.mountPoint)
		else:
			tmpl = config.lookup.get_template("login.html")
			return tmpl.render(env=config.htmlEnv)
	
	@cherrypy.expose
	def login(self, username="", password=""):
		u = users.userExists(username)
		if u != None:
			if u.verifyPassword(password):
				cherrypy.session["log"] = True
				cherrypy.session["username"] = username
				cherrypy.session["admin"] = False
				for g in u.groups:
					print g.name
					if g.name == "admin":
						cherrypy.session["admin"] = True
						print "admin!"
				raise cherrypy.HTTPRedirect(config.mountPoint)
			else:
				raise cherrypy.HTTPRedirect(config.mountPoint + "/login")
		raise cherrypy.HTTPRedirect(config.mountPoint + "/login")
	
	@cherrypy.expose
	def profile(self):
		if cherrypy.session.get("log") == True:
			u = users.userExists(cherrypy.session["username"])
			tmpl = config.lookup.get_template("profile.html")
			return tmpl.render(env=config.htmlEnv, user=u, session=cherrypy.session)
		else:
			raise cherrypy.HTTPRedirect(config.mountPoint + "/login")
	
	@cherrypy.expose
	def chpass(self, password=None, npassword1=None, npassword2=None):
		if cherrypy.session["log"] != True or password==None or npassword1==None or npassword2 == None:
			return '{status: "fail", msg: "Champs vides."}'
		else:
			u = users.userExists(cherrypy.session["username"])
			if u.verifyPassword(password):
				if npassword1 != npassword2:
					return '{"status": "fail", "msg": "Les deux mots de passe ne correspondent pas !"}'
				if npassword1 == "" or npassword2 == "":
					return '{"status": "fail", "msg": "Le mot de passe ne peut pas être vide"}'
				else:
					try:
						u.changePassword(npassword1)
						return '{"status": "ok", "msg": "Mot de passe mis a jour !"}'
					except Exception as e:
						return '{"status": "fail", "msg": "'+str(e)+'"}'
			else:
				return '{"status": "fail", "msg": "Mot de passe incorrect."}'
	
	@cherrypy.expose
	def chreal(self, realname=None):
		if cherrypy.session["log"] != True or realname == None:
			return '{"status": "fail", "msg": "Champs vides."}'
		else:
			u = users.userExists(cherrypy.session["username"])
			if u != None:
				try:
					u.realName = realname
					return '{"status": "ok", "msg": "Nom mis a jour."}'
				except Exception as e:
					return '{"status": "fail", "msg": "'+str(e)+'"}'
			else:
				return '{"status": "fail", "msg": "Je n\'ai pas pu changer votre nom :("}'
	
	@cherrypy.expose
	def logout(self):
		cherrypy.lib.sessions.expire()
		raise cherrypy.HTTPRedirect(config.mountPoint)
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access(groups=['admin'])
	def users(self):
		tmpl = config.lookup.get_template("users.html")
		ulist = list(User.select())
		return tmpl.render(env=config.htmlEnv, users=ulist, session=cherrypy.session)
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access(groups=['admin'])
	def newuser(self, username=None, password=None, confpassword=None, realname=None):
		if password=="" or confpassword=="" or username == "" or realname == "":
			return '{"status": "fail", "msg": "Champs vides"}'
		else:
			if password != confpassword:
				return '{"status": "fail", "msg": "Les deux mots de passe ne correspondent pas !"}'
			u = users.userExists(username)
			if u != None:
				return '{"status": "fail", "msg": "Cet utilisateur existe deja"}'
			
			try:
				u = User(login=username,realName=realname)
				u.changePassword(password)
				u.addGroup("user")
				return '{"status": "ok", "msg": "Utilisateur <b>' + username + '</b> cree avec succes !"}'
			except Exception as e:
				return '{ "status": "fail", "msg": "'+str(e)+'"}'
	
	@cherrypy.expose
	@cherrypy.tools.restrict_access(groups=['admin'])
	def deluser(self, username=None):
		if username == "":
			return '{"status": "fail", "msg": "Aucun utilisateur"}'
		elif username == "admin":
			return '{"status": "fail", "msg": "Cet utilisateur ne peut etre enleve"}'
		else:
			u = users.userExists(username)
			if u == None:
				return '{"status": "fail", "msg": "Cet utilisateur n\'existe pas"}'
			else:
				if users.deleteUser(username):
					return '{"status": "ok", "msg": "Utilisateur <b>' + username + '</b> detruit avec succes !"}'
				else:
					return '{ "status": "fail", "msg": "Echec"}'
		
