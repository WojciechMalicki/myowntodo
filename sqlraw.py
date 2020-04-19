#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# create database connection
class dbcon():

	
	def __init__(self, filename):
		self.con = sqlite3.connect(filename)

# access to column by index and by name
con.row_factory = sqlite3.Row

# create cursor object
cur = con.cursor()

# create table
