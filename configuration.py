#!/usr/bin/env python
# -*- config: utf-8 -*-

import yaml
import hashlib
import re

class Configuration:
	def __init__(self, cfile="config.yml"):
		try:
			self.confDict = yaml.load(open("config.yml", "r").read())
		except:
			self.confDict = {
				
			}
	
	def save(self, f="config.yml"):
		yaml.dump(self.confDict, open(f, "w"))

if __name__ == "__main__":
	c = Configuration()

	
