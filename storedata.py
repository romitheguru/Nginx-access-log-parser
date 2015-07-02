"""
	We will use MySQL to store statistics produces by log analyses.

	This module will take of creating tables to statistics, if not already created.
	Here, we will use different tables for different type of data.
	Further, it can be used to insert data into the corresponding tables

"""
try:
	import MySQLdb
except ImportError:
	raise ImportError('MySQLdb module didn\'t load')

db = None
cursor = None

# Open database connection
def openConnection(username,password,database):
	try:
		global db,cursor
		db = MySQLdb.connect('localhost',username,password,database)
		# In above query, enter your host_name,user_name, password, and database to be load

		# prepare a cursor object using cursor() method
		cursor = db.cursor()
	except:
		# In case of an error while openning the connection
		print 'Either connection is already established or can not open the connection'


# Create table to store logs details
def addToTable_Logs(LogID,enteries,fails):
	try:		
		query = '''
		create table logs(
		logID int primary key,
		total_entries int,
		processing_fails int )
		'''
		cursor.execute(query)
	except:
		pass

	cursor.execute('select logID from logs')
	a = cursor.fetchall()
	if LogID in a[0]: return
	query = "insert into logs(logID,total_entries,processing_fails) values('%d','%d','%d')" %(LogID,enteries,fails)

	try:
   		# Execute the SQL command
   		cursor.execute(query)
   		# Commit your changes in the database
   		db.commit()
	except:
   		# Rollback in case there is any error
   		db.rollback()


# create table to store Number Log entries by HTTP status code
def addToTable_httpstatus(LogID,status):
	try:   	
   		query = '''
		create table httpstatus(
		logID int,
		httpcode int,
		frequency int )
		'''

		cursor.execute(query)
	except:
		pass

	cursor.execute('select logID from httpstatus')
	a = cursor.fetchall()
	if LogID in a[0]: return
	for k in status:
		query = "insert into httpstatus(logID,httpcode,frequency) values('%d','%d','%d')" %(LogID,k,status[k])
		try:
   			# Execute the SQL command
   			cursor.execute(query)
   			# Commit your changes in the database
   			db.commit()
		except:
   			# Rollback in case there is any error
   			db.rollback()


# create table to store URLs and pageviews
def addToTable_Pageviews(LogID,views):
	try:
	   	query = '''
		create table Pageviews(
		logID int,
		URL varchar(100),
		pageviews int )
		'''
		cursor.execute(query)
	except:
		pass

	cursor.execute('select logID from Pageviews')
	a = cursor.fetchall()
	if LogID in a[0]: return
	for k in views:
		query = "insert into Pageviews(logID,URL,pageviews) values('%d','%s','%s')" %(LogID,k,views[k])
		try:
   			# Execute the SQL command
   			cursor.execute(query)
   			# Commit your changes in the database
   			db.commit()
		except:
   			# Rollback in case there is any error
   			db.rollback()



# create table to store URLs and unique visits
def addToTable_UniqueVisits(LogID,visits):
   	try:
   		query = '''
		create table UniqueVisits(
		logID int,
		URL varchar(100),
		pagevisits int )
		'''
		cursor.execute(query)
	except:
		pass

	cursor.execute('select logID from UniqueVisits')
	a = cursor.fetchall()
	if LogID in a[0]: return
	for k in visits:
		query = "insert into UniqueVisits(logID,URL,pagevisits) values('%d','%s','%s')" %(LogID,k,visits[k])
		try:
   			# Execute the SQL command
   			cursor.execute(query)
   			# Commit your changes in the database
   			db.commit()
		except:
   			# Rollback in case there is any error
   			db.rollback()



# disconnect from server
def disconnect():
	db.close()
