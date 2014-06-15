#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlobject as sql
from sqlobject.main import SQLObjectNotFound
import hashlib
import crypt
import random
import users

class Quote(sql.SQLObject):
	"""
		This object represents a quote. It stores
		- quote
		- author
		- submitter
		- upvotes
	"""
	quote = sql.StringCol(unique=True, notNone=True)
	author = sql.StringCol(default="")
	submitter = sql.StringCol(default="")
	upvotes = sql.RelatedJoin('User')
			
	def upvote(self, user):
		try:
			if users.User.byLogin(user) in self.upvote:
				pass
			else:
				self.addUser(users.User.byLogin(user))
		except Exception as e:
			print e
	
	def downvote(self, user):
		try:
			if not users.User.byLogin(user) in self.upvote:
				pass
			else:
				self.removeUser(users.User.byLogin(user))
		except Exception as e:
			print e
