#!/usr/bin/python3.2
import sqlite3
from hasher import *
hashme= hashguru()
class dbhandler:
	def __init__(self,db_name):
		self.db =db_name
		global DBNAME
		DBNAME=self.db
		
	def mkdb(self):
		try:
			global db
			db=sqlite3.connect(DBNAME)
			db.row_factory =sqlite3.Row
			db.commit()
			print("")
			print("Database Name :{} Created Succesfully".format(DBNAME))
		except Exception as e:
			raise e

	def mktable(self):
		try:
			db.execute('CREATE TABLE "test" ("primary" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"fname" TEXT NOT NULL,"fhash" TEXT NOT NULL);') 

			db.commit()
		except Exception as e:
			raise e

	def insert(self,filename,filehash):
		self.filename=filename
		self.filehash=filehash
		try:
			db.execute('insert into test (fname, fhash) values (?,?)',(filename,filehash))
			db.commit()
		except:
			print("File Doesn't Exist or You don't have Sufficent Privilages !")


	def show(self):
		result = db.execute('select * from test')
		print ("")
		print ("Printing Contents of the DB !")    
		print ("")
		for row in result:
			print(row[0],row[1],row[2])
		print ("")
		print ("")

	def checkhash(self):
		result = db.execute('select * from test')
		for row in result:
			sum_now= hashme.hashit(row[1])
			if (sum_now == row[2]):
				print("file is not changed ")
			else:
				print("file has changed ")







