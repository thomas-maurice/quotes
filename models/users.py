#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlobject as sql
from sqlobject.main import SQLObjectNotFound
import hashlib
import crypt
import random

class User(sql.SQLObject):
	"""
		This object represents a user. It stores
		- login
		- passHash
		- realName
		- groups
	"""
	login = sql.StringCol(alternateID=True, unique=True, notNone=True)
	passHash = sql.StringCol(default="")
	cryptPass = sql.StringCol(default="")
	realName = sql.StringCol(default="")
	groups = sql.RelatedJoin('UserGroup')
	
	def salt(self):
		"""Returns a string of 2 random letters"""
		letters = 'abcdefghijklmnopqrstuvwxyz' \
		'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
		'0123456789/.'
		return random.choice(letters) + random.choice(letters)
	
	def verifyPassword(self, password):
		"""
			Checks if the given password is the good one
		"""
		return (hashlib.sha1(password).hexdigest() == self.passHash)
	
	def changePassword(self, password):
		"""
			Changes the password
		"""
		self.passHash = hashlib.sha1(password).hexdigest()
		self.cryptPass = crypt.crypt(password, "$6$" + self.salt())
	
	def isInGroup(self, grp):
		"""
			Checks if the user is in the given group
		"""
		try:
			return UserGroup.byName(grp) in self.groups
		except:
			return False
	
	def addGroup(self, grp):
		"""
			Adds the user to a group. If the group does not exist it
			will NOT be created
		"""
		try:
			self.addUserGroup(UserGroup.byName(grp))
			return True
		except:
			return False
			
	def removeGroup(self, grp):
		"""
			Removes the user from the given group
		"""
		try:
			self.removeUserGroup(UserGroup.byName(grp))
			return True
		except:
			return False

class UserGroup(sql.SQLObject):
	"""
		This class implements a group. Which is just basically
		a name and a relation to users.
	"""
	name = sql.StringCol(alternateID=True, unique=True, notNone=True)
	users = sql.RelatedJoin('User')

def userGroupExists(grp):
	"""
		Checks if an user exists, returns it if yes.
		None otherwise.l
	"""
	try:
		g = UserGroup.byName(grp)
		return g
	except:
		return None

def userExists(login):
	"""
		Checks if an user exists, returns it if yes.
		None otherwise.
	"""
	try:
		u = User.byLogin(login)
		return u
	except:
		return None

def deleteUser(login):
	"""
		Removes a user
	"""
	try:
		User.byLogin(login).destroySelf()
		return True
	except:
		return False

if __name__ == "__main__":
	#loadDatabase("test.db")
	print User.byLogin("admin").isInGroup("user")
