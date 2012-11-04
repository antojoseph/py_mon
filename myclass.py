#!/usr/bin/python3.2
import sqlite3
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
		db.execute('insert into test (fname, fhash) values (?,?)',(filename,filehash))
		db.commit()

	def show(self):
		result = db.execute('select * from test')
		for row in result:
			yield (row['primary'],row['fname'],row['fhash'])







