#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import sqlobject as sql
from models.users import *
from models.quotes import *

def loadDatabase(database):
	"""
		Loads a database. If the database is non-existant, it shall be
		filled with two groups :
		 - admin
		 - user
		
		And an administrator :
		 - login: "admin", password: "password"
	"""
	exist = True
	try:
		f = open(database, "r")
		f.close()
	except:
		exist = False
		
	sql.sqlhub.processConnection = sql.connectionForURI('sqlite:'+database)
	
	# If the DB is inexistant
	if not exist:
		# Create the tables
		User.createTable()
		UserGroup.createTable()
		Quote.createTable()
		
		# Create an administrator
		adminUser = User(login="admin", realName="Amin Nistrator")
		adminUser.changePassword("password")
		
		# Create the groups
		admin = UserGroup(name="admin")
		user = UserGroup(name="user")
		
		# Add the new user to the groups
		adminUser.addUserGroup(admin)
		adminUser.addUserGroup(user)
		
		quote = Quote(quote="Il en faut plus pour me remplir la bouche", author="MGO", submitter="TME")
		quote = Quote(quote="Si Gauthier était Descartes, il aurait conclu qu'il n'existait pas", author="ADE", submitter="TME")
		quote = Quote(quote="J'ai pas eu le temps je me suis baladé !", author="GCN", submitter="TME")

cherrypy.tools.db = cherrypy.Tool('on_start_resource', loadDatabase)
