# Name: Python Nginx Log Parser
# A program that analyses Nginx's access logs and produces statistics.

import time
import Httpstatuscode
import Logprocess, Uniquepagevisits, Pageviews
import StoreStatistics

LIST_SET = []


def main():
	start_time = time.time()
	
	# Reading log file 
	try:
		logfile = open('access.log', 'r')
	except IOError:
		raise IOError('The input file does not exist, please check the path.')
		

	# Counting total log enteries
	enteries = Logprocess.count(logfile)
	logfile.seek(0)
	
	# Processing faliures
	fails = Logprocess.failure(logfile)
	logfile.seek(0)
	
	# Number of log enteries by HTTP status code
	status = Httpstatuscode.frequency(logfile)
	logfile.seek(0)
	
	#URL and Unique visits
	visits = Uniquepagevisits.visits(logfile, 1)
	logfile.seek(0)

	views = Pageviews.views(logfile,1)
	
	logfile.close()
	print '\n--------------------Time Taken--------------------\n'
	print "--- %s seconds ---" % (time.time() - start_time)



	# Log ID will uniquely indenfy a log file, it should be changed for a different log file
	LogID = 111

	username = 'root'
	password = 'sha1'
	database = 'Logs_Statistics'


	# Now, store statistics in the database
	# Following call will open database connection
	StoreStatistics.openConnection(username,password,database)

	# This will store number of log entries and failures
	StoreStatistics.addToTable_Logs(LogID,enteries,fails)

	# This will store http status and thier frequency
	StoreStatistics.addToTable_httpstatus(LogID,status)

	# This will store unique visits and respective urls
	StoreStatistics.addToTable_UniqueVisits(LogID,visits)

	# This will store number of page views for a url
	StoreStatistics.addToTable_Pageviews(LogID,views)

	# Disconnect from the database
	StoreStatistics.disconnect()


if __name__ == '__main__':
	main()
