"""
	This module used to process access-log file and record the number of enteries processed
	and also calculate the number of enteries that fails to process.

"""

# Counting total enteries
# Parameter: log: example.log file
import re

def count(log):
	number_of_entry = 0
	for line in log.xreadlines():
		number_of_entry = number_of_entry + 1
	print '--------------------Number of enteries: --------------------\n' + str(number_of_entry)
	return number_of_entry


# Total no of processing failures
# Parameter: log: example.log file
def failure(log):
	fails = 0
	
	try:
		# Find all the occurrences of HTTP Status code
		match = re.findall(r'GET\s.+\s\w+/.+"\s([\d]+)\s', log.read())
	except:
		raise TypeError("The file HTTP status format is different.")
		
	# Number of failures
	for x in match:
		if x != '200': 
			fails = fails + 1
	print '\n--------------------Processing Failures: --------------------\n' + str(fails)
	return fails
